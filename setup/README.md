# Before lesson 1: VS Code and C++ setup

We will use this sheet together in the first class. Bring your laptop; you do not need to complete the setup in advance. We will follow the section for your operating system and finish with the shared checks.

**Finished means:** you can configure, build, and run the supplied program with CMake. You do not need to understand all its code yet.

## Contents

- [Install VS Code](#1-install-vs-code)
- [Optional ChatGPT and Codex](#optional-chatgpt-and-codex)
- [Install platform tools](#2-install-the-tools-for-your-system): [macOS](#macos), [Windows](#windows), [Linux](#linux-ubuntudebian)
- [Install CMake](#3-install-cmake)
- [Install Git](#4-install-git)
- [Install Python](#5-install-python-3-for-the-root-session-launcher)
- [Open the project folder](#6-open-the-supplied-project-folder)
- [Configure, build, and run](#7-configure-build-and-run)
- [Troubleshooting](#troubleshooting)
- [Completion checklist](#completion-checklist)
- [References](#references)

## 1. Install VS Code

Download the desktop application from [Visual Studio Code](https://code.visualstudio.com/download). Use the version for your operating system and processor.

In VS Code, open **Extensions** from the left sidebar. Install **C/C++**, published by Microsoft (`ms-vscode.cpptools`). It provides C++ language support and the VS Code debugger configurations used on Windows/Linux. It does not include the compiler, linker, or native debugger; install those separately.

These are the only extensions required by the supplied course setup:

| Platform | Extension | Purpose |
| --- | --- | --- |
| All platforms | [C/C++ by Microsoft](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools) (`ms-vscode.cpptools`) | C++ language support and the debugger configuration used on Windows/Linux |
| macOS | [LLDB DAP by LLVM](https://marketplace.visualstudio.com/items?itemName=llvm-vs-code-extensions.lldb-dap) (`llvm-vs-code-extensions.lldb-dap`) | LLDB debugger adapter used by the supplied macOS launch configuration |

These extensions do not install the compiler, linker, or system debugger; install those using the operating-system steps below. No extra extension is required for CMake or Git: the supplied VS Code tasks call CMake directly, and VS Code has built-in Git support. The C/C++ Extension Pack, CMake Tools, GitLens, and syntax-theme extensions are optional and are not needed for this course setup.

## Optional: ChatGPT and Codex

Some course activities may use an AI agent to inspect or edit a project. ChatGPT's Free plan currently includes limited Codex access for quick coding tasks, subject to account, platform, rollout, and usage limits. Start at [ChatGPT](https://chatgpt.com); no paid plan or API key is required to try the included access. See [current ChatGPT plan details](https://learn.chatgpt.com/docs/pricing).

For an agent to edit local course files, use a Codex feature that has access to the project folder. A regular browser chat can discuss code, but it does not directly change files on your computer. ChatGPT/Codex is optional; the course compiler and debugger setup works without it. Do not buy a subscription or install another VS Code extension just for this setup check.

## 2. Install the tools for your system

### macOS

Open the macOS Terminal and run:

```bash
xcode-select --install
```

Finish the installation dialog. If the tools are already installed, proceed. Full Xcode is not needed for this exercise.

Check:

```bash
clang++ --version
```

You should see Apple Clang version information. We use `clang++` explicitly: the usual Apple-provided `g++` command also invokes Clang.

Install **LLDB DAP**, published by LLVM (`llvm-vs-code-extensions.lldb-dap`). The course launch configurations use Homebrew's LLDB DAP 21 or newer so program output can appear in VS Code's integrated Terminal. Install Homebrew LLDB:

```bash
brew install lldb
```

If it is already installed, update it with:

```bash
brew upgrade lldb
```

Homebrew's LLDB includes `lldb-dap`. Check its version and installation path:

```bash
"$(brew --prefix lldb)/bin/lldb-dap" --version
brew --prefix lldb
```

The supplied macOS launch configuration runs a small script in the workspace's `.vscode` folder. It finds Homebrew on either Apple Silicon or Intel Macs and starts that installation's `lldb-dap`; no per-computer launch-path edit is needed. The configuration uses `"console": "integratedTerminal"` and retains `runInTerminal` for compatibility with older LLDB DAP versions.

### Windows

Install **Build Tools for Visual Studio** from [Visual Studio downloads](https://visualstudio.microsoft.com/downloads/). In the installer, select **Desktop development with C++**, including the MSVC compiler and a Windows SDK. If you already have Visual Studio with that workload, use it.

After installation:

1. Close **all** VS Code windows and quit VS Code.
2. Open **Developer Command Prompt for Visual Studio** from the Start menu.
3. Run `cl`. It should print the Microsoft compiler banner and usage information.
4. In that prompt, navigate to the supplied `setup` folder. For example, replacing the path with yours:

```bat
cd /d "C:\Users\YourName\Documents\JUCE-Cpp-1\setup"
code .
```

Launch VS Code this way for these exercises so it inherits the compiler's environment. A normal terminal may not find `cl`, headers, or libraries. If `code` is not found, rerun the VS Code installer with **Add to PATH**, then reopen the developer prompt.

### Linux (Ubuntu/Debian)

Open a terminal and run:

```bash
sudo apt update
sudo apt install build-essential gdb
g++ --version
gdb --version
```

Both version commands should succeed. Other distributions require equivalent GCC/G++ and GDB packages through their own package manager. The supplied Linux debugger configuration expects GDB at `/usr/bin/gdb`; check with `command -v gdb` and ask for help if it is elsewhere.

## 3. Install CMake

CMake prepares the build and invokes your installed compiler and linker. We supply the configuration; you do not need to write CMake code yet.

- **macOS:** install the macOS package from [CMake downloads](https://cmake.org/download/) and place CMake in Applications. Open CMake and follow **Tools → How to Install For Command Line Use**. If you already use Homebrew, `brew install cmake` is an alternative.
- **Windows:** install CMake from [CMake downloads](https://cmake.org/download/), selecting **Add CMake to the system PATH** (for your user is sufficient). Then close VS Code and reopen it from a new Developer Command Prompt. Check `nmake /?` in that prompt; NMake is included with the MSVC tools.
- **Ubuntu/Debian:** run `sudo apt install cmake`. GNU Make is already included in `build-essential`.

In a new terminal, check:

```bash
cmake --version
```

Use CMake **3.22 or newer** for the course so the same installation can build the later JUCE lessons. If your package manager supplies an older version, use the official CMake download.

This project uses Make on macOS/Linux and NMake on Windows. You do not need Ninja or the VS Code CMake Tools extension for this supplied setup.

## 4. Install Git

Git records changes to your code. Install it now; repository and commit workflows will be introduced in class. A GitHub account is not needed to use Git locally.

- **macOS:** Apple's Command Line Tools from step 2 include Git. Check the version below; no separate installation is normally needed.
- **Windows:** install [Git for Windows](https://git-scm.com/downloads/win). Keep the option that makes Git available from the command line and third-party software. Restart VS Code from a new Developer Command Prompt after installation.
- **Ubuntu/Debian:** run `sudo apt install git`. On other distributions, install Git using your package manager.

In VS Code's terminal, run:

```bash
git --version
```

You should see a Git version number. VS Code has built-in Git support; no extra Git extension is required.

## 5. Install Python 3 for the root session launcher

Python 3 is used only by the course-root launcher, which selects a session and runs that session's existing VS Code build task. Individual session folders can still be built with their own tasks without Python.

- **macOS:** check `python3 --version`. If it is unavailable, install Python 3 from [python.org](https://www.python.org/downloads/macos/).
- **Windows:** install Python 3 from [python.org](https://www.python.org/downloads/windows/), enable the Python launcher, and check `py -3 --version` in a new terminal.
- **Ubuntu/Debian:** run `sudo apt install python3`, then check `python3 --version`.

## 6. Open the supplied project folder

Copy the entire `setup` folder to your own writable course folder, including the hidden `.vscode` directory. Do not copy only `main.cpp`.

On macOS/Linux, choose **File → Open Folder** in VS Code and select **setup itself**, not the parent course folder. On Windows, use the developer-prompt procedure above. If prompted about workspace trust, trust this supplied folder after confirming it is the course material.

The Explorer should show:

```text
setup/
  .vscode/
    launch.json
    tasks.json
  .gitignore
  CMakeLists.txt
  main.cpp
  README.md
```

The supplied configuration already connects the build commands and debuggers. Do not generate another configuration using “build active file”.

## 7. Configure, build, and run

Choose **Terminal → New Terminal**. Its working directory should be `setup`. Save `main.cpp` before building.

**Configure on macOS/Linux:**

```bash
cmake -S . -B build -G "Unix Makefiles" -DCMAKE_BUILD_TYPE=Debug
```

**Configure on Windows** (in VS Code launched from the developer prompt):

```powershell
cmake -S . -B build -G "NMake Makefiles" -DCMAKE_BUILD_TYPE=Debug
```

**Build on all platforms:**

```bash
cmake --build build
```

Only after a successful build, run on **macOS/Linux**:

```bash
./build/setup-check
```

Or on **Windows**:

```powershell
.\build\setup-check.exe
```

Expected output:

```text
Setup works!
```

Configure creates the build files in `build/`; build compiles and links; running starts the executable. The Debug configuration includes the information needed for breakpoints. After editing, save and repeat the build and run commands. Unchanged code normally does not need recompiling.

Do not copy `build/` between machines or reuse a build directory created with a different generator. If CMake reports an old path or generator mismatch, rename that generated folder to `build-old` (or another unused name), then configure again.

## Troubleshooting

| Problem | Check |
| --- | --- |
| `clang++`, `g++`, or `cl` not found | Finish the toolchain installation. On Windows, quit all VS Code windows and launch from the developer prompt again. |
| `cmake` not found | Complete the CMake command-line installation and restart VS Code. Check `cmake --version` in its terminal. |
| `git` not found | Finish installing Git and restart VS Code. On Windows, ensure Git was added to PATH, then reopen VS Code from a new Developer Command Prompt. |
| Make/NMake not found | Check the platform toolchain installation; on Windows launch VS Code from the developer prompt. |
| Standard headers such as `iostream` missing | The development tools/SDK installation is incomplete, or Windows is missing the developer environment. |
| No “Setup” debug configurations | Open `setup` as the folder and confirm `.vscode/launch.json` was copied. |
| macOS debugger type `lldb-dap` unavailable | Install or enable LLDB DAP (`llvm-vs-code-extensions.lldb-dap`) and Homebrew LLDB (`brew install lldb`), then reopen the folder. |
| macOS program output appears in Debug Console | Confirm Homebrew LLDB is installed with `brew install lldb`, and that you opened the supplied folder with its `.vscode` directory. The launch configuration uses that folder's script to locate LLDB on Apple Silicon or Intel Macs. |
| Linux debugger type `cppdbg` unavailable | Install or enable Microsoft C/C++ (`ms-vscode.cpptools`) and confirm GDB is installed. |
| Windows debugger type `cppvsdbg` unavailable | Install or enable Microsoft C/C++ (`ms-vscode.cpptools`) and confirm the Visual Studio C++ workload is installed. |
| Breakpoint does not stop | Use the supplied configuration, save the file, and verify the build succeeds with debug information. Put the breakpoint on the `std::cout` statement. |
| Executable not found | Check the compiler output. The executable is created only after a successful build. |
| Old output after editing | Save and rebuild. Do not run an older executable after a failed build. |
| macOS asks for developer-tool permission | Allow the debugger when macOS prompts, then retry. Bring the exact message if launch still fails. |

## Completion checklist

- [ ] VS Code opens the `setup` folder.
- [ ] My compiler prints version/usage information.
- [ ] `git --version` prints a version number in VS Code's terminal.
- [ ] `python3 --version` (or `py -3 --version` on Windows) works for the root session launcher.
- [ ] `cmake --version` succeeds and CMake configures the project.
- [ ] Compiling succeeds and the program prints `Setup works!`.

If something fails, bring your operating system, the command you ran, and the exact error text. Do not spend the first lesson reinstalling tools without knowing which check failed.

## References

- [VS Code: C/C++ extension](https://code.visualstudio.com/docs/languages/cpp)
- [VS Code: Clang on macOS](https://code.visualstudio.com/docs/cpp/config-clang-mac)
- [VS Code: Microsoft C++ on Windows](https://code.visualstudio.com/docs/cpp/config-msvc)
- [VS Code: GCC/GDB on Linux](https://code.visualstudio.com/docs/cpp/config-linux)
- [CMake downloads](https://cmake.org/download/)
- [Git downloads](https://git-scm.com/downloads)
- [LLDB DAP extension](https://marketplace.visualstudio.com/items?itemName=llvm-vs-code-extensions.lldb-dap)

Prepared 29 September 2026. This folder is only a setup check; CMake is used now with a supplied configuration; its details and JUCE are introduced later.
