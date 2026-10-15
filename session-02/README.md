# Session 02 — Types, arithmetic, and conditions

A supplied starting point, not a completed exercise. All tasks use only this session’s files.

## What you will learn

Choose integer versus floating-point arithmetic; use const and an if/else; reject invalid input before dividing.

## Tasks

1. Build the supplied `source/main.cpp` and run the program with its fixed positive tempo. Identify the type, name, and value of bpm.
2. Calculate the duration of one beat and print it.
3. Add an if/else so zero and negative tempos print 'Invalid tempo' and do not perform the division.
4. Try 120, 100, 0, and -20. Save and rebuild for every change.
5. Compare 60000 / 137 with 60000.0 / 137. Explain why the first loses the fractional part.

## Check your result

120 gives 500 ms; 100 gives 600 ms; 0 and -20 produce Invalid tempo, not a duration.

## Individual checkpoint

Explain why the check must happen before division. Repair a supplied incorrect <= condition independently.

## Optional extension

Print a warning above 300 BPM without treating it as invalid.

## Practice after class

Extend the program to print a BPM classification: `slow` below 60, `moderate` from 60 to below 120, `fast` from 120 through 180, and `high` above 180. Keep nonpositive BPM invalid and do not calculate a duration for it. Test the boundary values 0, 59, 60, 119, 120, 180, and 181 BPM.

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
