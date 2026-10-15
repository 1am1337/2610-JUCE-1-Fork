# Session 05 — Debugging with breakpoints

A supplied starting point, not a completed exercise. All tasks use only this session’s files.

## What you will learn

Launch a debugger; set a breakpoint; inspect locals and watches; use Step Over, Step Into, Step Out, Continue, and the call stack.

## Tasks

1. Open this session folder in VS Code. Select Lesson — your platform in Run and Debug. Use the supplied Debug build.
2. Put a breakpoint on the call to twoBeatsMs inside main. Start with F5 and confirm execution stops before that line runs.
3. Step Into twoBeatsMs, then Step Into beatDurationMs. Inspect bpm and add bpm to Watch.
4. Step Over the calculation. Inspect result; explain why the value is wrong for 137 BPM. Inspect Call Stack and select each of the three frames.
5. Step Out to the caller, then Step Over the remaining statement. Continue to print the result. Stop and repair the arithmetic bug.
6. Start a new debug run and verify the corrected result. Each student must operate the debugger themselves.

## Check your result

The supplied `source/main.cpp` prints 874 ms for two beats at 137 BPM; corrected output is approximately 875.912 ms. At 120 BPM both versions give 1000, so that case alone does not reveal the bug.

## Individual checkpoint

Individually stop inside beatDurationMs, show bpm, identify the caller, and explain the fix independently.

## Optional extension

Try a conditional breakpoint for bpm == 137 if time remains; ordinary breakpoints are the required outcome.

## Practice after class

After fixing the integer-division bug, add `threeBeatsMs` using `beatDurationMs`. Print its result at 120 and 137 BPM, then debug the 137 BPM call: stop inside `beatDurationMs` and inspect the input and returned value.

## Build and run

Open **this session folder** in VS Code. Run these commands from its terminal after saving your files. Follow the Git workflow agreed in class when keeping your changes.

**macOS:**

```bash
clang++ -std=c++17 -g -O0 source/main.cpp -o main
./main
```

Apple's Command Line Tools supply `clang++`; the Apple-provided `g++` usually invokes the same compiler.

**Linux:**

```bash
g++ -std=c++17 -g -O0 source/main.cpp -o main
./main
```

**Windows** (VS Code launched from a Developer Command Prompt):

```powershell
cl /EHsc /std:c++17 /Zi /Od source/main.cpp /Fe:main.exe /link /DEBUG
.\main.exe
```

The first command compiles and links; the second runs the executable. Run only after a successful build. Recompile after saving changes: these direct commands compile every time. Debug information and disabled optimization prepare the program for session 5's debugger exercise.

No CMake is used in this lesson. It is introduced in session 7. The supplied VS Code build task runs the compiler directly. For session 5 onwards, select **Lesson — your platform** in Run and Debug and press F5 to build and launch under the debugger.
