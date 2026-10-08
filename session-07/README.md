# Session 07 — CMake and a personal Git workflow

A supplied starting point, not a completed exercise. All tasks use only this session’s files.

## What you will learn

Write a minimal CMake project; distinguish configure/build/run; inspect, commit, and undo a small change in a personal repository.

## Tasks

1. Build the supplied project. Explain minimum version, project, executable target, and its source list.
2. In a new practice folder in your own repository, recreate this small project and CMakeLists.txt with notes allowed. Build it in a fresh build directory.
3. Build again without editing; observe no recompilation. Edit source/main.cpp and rebuild.
4. In your own work repository, run git status and git diff. Make a baseline commit before editing the session. If Git asks, configure your own author name/email for this repository.
5. Change only the printed label. Inspect the diff, build/run, and either commit or discard just that change.

## Check your result

### Git command reference — your own work only

Run these from your personal course repository, never the teaching checkout. If it is not a repository yet, run `git init` in that personal course folder. Add `build/`, `build-*/`, and generated executables to its `.gitignore` before committing.

If author details are missing, set them for this repository using your own values:

```bash
git config user.name "Your Name"
git config user.email "your-chosen-email@example.com"
```

From your copied session folder, create a baseline before editing:

```bash
git status
git add CMakeLists.txt source/main.cpp
git commit -m "Save session 7 baseline"
```

After an edit, inspect `git diff -- source/main.cpp`. To keep it, add the file and commit again. To discard only that uncommitted edit, use `git restore -- source/main.cpp` **after confirming the diff is disposable**. Do not run restore on work you want to keep. No remote or push is needed for this exercise.

A clean configure/build succeeds; no-edit rebuild does not recompile; only the requested label changes. The baseline commit allows recovery.

## Individual checkpoint

Explain CMake versus compiler versus build tool. Show a diff and explain each changed line.

## Optional extension

Add one additional source file explicitly to the target, without file globbing.

## Practice after class

Write a three-command configure/build/run guide for your own platform.

## Build and run

Open **this session folder** in VS Code, not the course root. Work in your own copy; keep the teaching checkout unchanged. Complete [setup](../setup/README.md) first. These are supplied build commands until session 7 explains CMake.

Configure on macOS/Linux:

```bash
cmake -S . -B build -G "Unix Makefiles" -DCMAKE_BUILD_TYPE=Debug
```

Configure on Windows (VS Code launched from a Developer Command Prompt):

```powershell
cmake -S . -B build -G "NMake Makefiles" -DCMAKE_BUILD_TYPE=Debug
```

Build on all platforms:

```bash
cmake --build build
```

Run on macOS/Linux: `./build/bin/main`. On Windows: `.\build\bin\main.exe`.

Run only after a successful build. If you move the project, use a fresh build directory. For lesson 5 onwards, select **Lesson — your platform** in Run and Debug, then F5; the supplied task builds before launch. Save changes first. C++/debugger extensions are described in the setup sheet.
