# Session 04 — Functions and scope

A supplied starting point, not a completed exercise. All tasks use only this session’s files.

## What you will learn

Follow arguments, parameters, return values, and local variables; reuse one function from several calls.

## Tasks

1. Run the direct calculation in main.
2. Move the calculation into double beatDurationMs(double bpm), defined above main.
3. Call it for 60, 120, and 150 BPM and print each returned value.
4. Add double twoBeatsMs(double bpm) that calls beatDurationMs and doubles its result.
5. Explain why a local variable inside the function is not directly accessible from main. Keep the contract positive bpm.

## Check your result

beatDurationMs(60) = 1000; (120) = 500; (150) = 400. twoBeatsMs(120) = 1000.

## Individual checkpoint

Independently, write a call for 100 BPM and explain how its argument reaches the parameter.

## Optional extension

Write fourBeatsMs using an existing function.

## Practice after class

Add `barDurationMs(bpm, beatsPerBar)`, implemented by calling `beatDurationMs`. Print the duration of 3/4 and 4/4 bars at 120 BPM and check the results: 1500 ms and 2000 ms.

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
