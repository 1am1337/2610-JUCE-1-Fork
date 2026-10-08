#!/usr/bin/env python3
"""Run the selected session's own VS Code build tasks from the course root."""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
PLATFORM = "windows" if sys.platform == "win32" else "osx" if sys.platform == "darwin" else "linux"
PLATFORM_LABEL = {"windows": "Windows", "osx": "macOS", "linux": "Linux"}[PLATFORM]
WORKSPACE_TOKEN = "${workspaceFolder}"


def fail(message: str) -> None:
    raise RuntimeError(message)


def load_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        fail(f"Cannot read {path}: {error}")


def merge_platform(task: dict[str, Any]) -> dict[str, Any]:
    result = dict(task)
    result.update(task.get(PLATFORM, {}))
    return result


def resolve(value: str, session_dir: Path) -> str:
    value = value.replace(WORKSPACE_TOKEN, str(session_dir))
    return re.sub(
        r"\$\{env:([^}]+)\}",
        lambda match: os.environ.get(match.group(1), ""),
        value,
    )


def task_cwd(task: dict[str, Any], session_dir: Path) -> Path:
    options = task.get("options", {})
    raw_cwd = options.get("cwd", WORKSPACE_TOKEN)
    cwd = Path(resolve(raw_cwd, session_dir))
    return cwd if cwd.is_absolute() else (session_dir / cwd).resolve()


def run_task(
    label: str,
    tasks: list[dict[str, Any]],
    session_dir: Path,
    dry_run: bool,
    completed: set[str],
    in_progress: set[str],
) -> None:
    if label in completed:
        return
    if label in in_progress:
        fail(f"Circular task dependency involving {label!r}.")

    matches = [task for task in tasks if task.get("label") == label]
    if len(matches) != 1:
        fail(f"Expected one task labeled {label!r}, found {len(matches)}.")
    task = merge_platform(matches[0])
    in_progress.add(label)

    dependencies = task.get("dependsOn", [])
    if isinstance(dependencies, str):
        dependencies = [dependencies]
    for dependency in dependencies:
        run_task(dependency, tasks, session_dir, dry_run, completed, in_progress)

    if task.get("type", "process") != "process":
        fail(f"Unsupported task type {task.get('type')!r} in {session_dir.name}.")

    command = resolve(str(task["command"]), session_dir)
    args = [resolve(str(argument), session_dir) for argument in task.get("args", [])]
    cwd = task_cwd(task, session_dir)
    environment = os.environ.copy()
    environment.update(
        {str(key): resolve(str(value), session_dir) for key, value in task.get("options", {}).get("env", {}).items()}
    )
    printable = subprocess.list2cmdline([command, *args]) if os.name == "nt" else " ".join(
        subprocess_list_quote(part) for part in [command, *args]
    )
    print(f"[{session_dir.name}] {label}: {printable}\n  in {cwd}", flush=True)
    if not dry_run:
        try:
            subprocess.run([command, *args], cwd=cwd, env=environment, check=True)
        except FileNotFoundError:
            fail(f"Could not find {command!r}. Check the compiler/CMake installation and terminal environment.")
        except subprocess.CalledProcessError as error:
            fail(f"Task {label!r} failed with exit code {error.returncode}.")

    in_progress.remove(label)
    completed.add(label)


def subprocess_list_quote(value: str) -> str:
    # Display-only quoting; execution passes a safe argument list directly.
    import shlex

    return shlex.quote(value)


def selected_launch_program(session_dir: Path) -> Path:
    launch = load_json(session_dir / ".vscode" / "launch.json")
    configs = launch.get("configurations", [])
    matches = [config for config in configs if str(config.get("name", "")).endswith(PLATFORM_LABEL)]
    if len(matches) != 1:
        fail(f"Expected one {PLATFORM_LABEL} launch configuration in {session_dir.name}.")
    raw_program = resolve(str(matches[0]["program"]), session_dir)
    return Path(raw_program)


def copy_debug_artifacts(source: Path, destination: Path) -> None:
    if not source.is_file():
        fail(f"The build task succeeded, but the configured executable was not found: {source}")

    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)

    source_pdb = source.with_suffix(".pdb")
    destination_pdb = destination.with_suffix(".pdb")
    if source_pdb.is_file():
        shutil.copy2(source_pdb, destination_pdb)
    elif destination_pdb.exists():
        destination_pdb.unlink()

    source_dsym = Path(str(source) + ".dSYM")
    destination_dsym = Path(str(destination) + ".dSYM")
    if source_dsym.is_dir():
        if destination_dsym.exists():
            shutil.rmtree(destination_dsym)
        shutil.copytree(source_dsym, destination_dsym)
    elif destination_dsym.exists():
        shutil.rmtree(destination_dsym)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("session", help="setup or a session folder, for example session-07")
    parser.add_argument("--dry-run", action="store_true", help="show the session tasks without running them")
    arguments = parser.parse_args()

    if arguments.session != "setup" and not re.fullmatch(r"session-0[1-9]", arguments.session):
        fail("The root launcher currently supports setup and session-01 through session-09.")

    session_dir = ROOT / arguments.session
    if not session_dir.is_dir():
        fail(f"Session folder does not exist: {session_dir}")

    tasks_data = load_json(session_dir / ".vscode" / "tasks.json")
    tasks = tasks_data.get("tasks", [])
    build_task = "Build setup" if arguments.session == "setup" else "Build lesson"
    run_task(build_task, tasks, session_dir, arguments.dry_run, set(), set())

    if not arguments.dry_run:
        source = selected_launch_program(session_dir)
        suffix = ".exe" if os.name == "nt" else ""
        destination = ROOT / ".vscode" / "launch-bin" / f"main{suffix}"
        copy_debug_artifacts(source, destination)
        print(f"Ready to debug: {destination}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except RuntimeError as error:
        print(f"Build launcher error: {error}", file=sys.stderr)
        raise SystemExit(1)
