# Session 03 — Loops and small collections

A supplied starting point, not a completed exercise. All tasks use only this session’s files.

## What you will learn

Repeat an operation; distinguish an index from a value; traverse a fixed-size std::array safely.

## Tasks

1. Build the supplied `source/main.cpp` and run it. Predict its output first; it prints only the first note.
2. Use a range-based for loop to print every note in the supplied four-note array.
3. Print each note transposed up by 12. Keep the stored notes unchanged.
4. Use a counting loop to print beat numbers 1 through 4. Explain where it starts and stops.
5. Change one array element and show that the loop still handles all four entries.

## Check your result

Original notes: 60 62 64 65. Transposed output: 72 74 76 77. Exactly four beat numbers: 1 2 3 4.

## Individual checkpoint

Explain why notes[4] is outside this array. Do not run an out-of-bounds example.

## Optional extension

Count how many notes are at least 64. Introduce a vector only after the core task is secure.

## Practice after class

Write a three-note array and predict its octave-transposed output.

## Build and run

Open **this session folder** in VS Code. Run these commands from its terminal after saving your files. Work in your own copy; keep the teaching checkout unchanged.

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
