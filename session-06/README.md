# Session 06 — Includes, headers, and the linker

A supplied starting point, not a completed exercise. All tasks use only this session’s files.

## What you will learn

Distinguish declarations from definitions; explain includes, translation units, object files, and unresolved references.

## Tasks

1. Build the supplied two-source-file project. Identify the declaration in Tempo.h and definition in Tempo.cpp.
2. Temporarily remove #include "Tempo.h" from main.cpp. Build, read the compiler diagnostic, and restore it.
3. Temporarily omit source/Tempo.cpp from the terminal compiler command below. Build and identify the linker error, then restore it to the command.
4. Add double twoBeatsMs(double bpm): declare it in Tempo.h, define it in Tempo.cpp, call it from main.cpp.
5. Explain why the header is included but not compiled as a separate executable, and why including a .cpp is not our solution.

## Check your result

Initial program prints 500. Completed program also prints 1000 for two beats at 120 BPM. Both deliberate failures disappear after restoration.

## Individual checkpoint

Draw main.cpp → main.o and Tempo.cpp → Tempo.o, then both objects → executable. Distinguish an object file from a class instance.

## Optional extension

Compile the two .cpp files separately with -c (or /c), then link the two objects manually.

## Practice after class

Add `barDurationMs(double bpm, int beatsPerBar)` to `Tempo.h` and `Tempo.cpp`, implemented using `beatDurationMs`. Call it from `main.cpp` for 3/4 and 4/4 at 120 BPM; expect 1500 ms and 2000 ms.

## Build and run

Open **this session folder** in VS Code. Run these commands from its terminal after saving your files. Follow the Git workflow agreed in class when keeping your changes.

**macOS:**

```bash
clang++ -std=c++17 -g -O0 source/main.cpp source/Tempo.cpp -o main
./main
```

Apple's Command Line Tools supply `clang++`; the Apple-provided `g++` usually invokes the same compiler.

**Linux:**

```bash
g++ -std=c++17 -g -O0 source/main.cpp source/Tempo.cpp -o main
./main
```

**Windows** (VS Code launched from a Developer Command Prompt):

```powershell
cl /EHsc /std:c++17 /Zi /Od source/main.cpp source/Tempo.cpp /Fe:main.exe /link /DEBUG
.\main.exe
```

The first command compiles and links; the second runs the executable. Run only after a successful build. Recompile after saving changes: these direct commands compile every time. Debug information and disabled optimization prepare the program for session 5's debugger exercise.

No CMake is used in this lesson. It is introduced in session 7. The supplied VS Code build task runs the compiler directly. For session 5 onwards, select **Lesson — your platform** in Run and Debug and press F5 to build and launch under the debugger.

### Compile the two files separately

On macOS:

```bash
clang++ -std=c++17 -g -O0 -c source/main.cpp -o main.o
clang++ -std=c++17 -g -O0 -c source/Tempo.cpp -o Tempo.o
clang++ main.o Tempo.o -o main
```

On Linux, replace `clang++` with `g++`. On Windows:

```powershell
cl /EHsc /std:c++17 /Zi /Od /c source/main.cpp source/Tempo.cpp
cl main.obj Tempo.obj /Fe:main.exe /link /DEBUG
```

Each source produces one object file. The final command links both objects. Omit Tempo.o (or Tempo.obj) from that final command to observe an unresolved-function linker error, then restore it.
