# Session 01 — First program: edit, build, run

This teaching checkout includes the worked solution in `source/main.cpp`. The in-class exercises below describe the steps from an empty `main` function; use the starter state provided for class before following them. Follow the Git workflow agreed in class when keeping your changes.

## What you will learn

- Identify source code and the executable produced from it.
- Save, compile, link, and run a small C++ program.
- Read a variable, a calculation, and an output statement.

## In-class exercises

1. **Build the empty program.** Predict what will happen when you run it. Build and run it, then identify which file is the source and which is the executable.
2. **Print a message.** Add a line inside `main` that prints `Hello music!`. Save, build, and run. Confirm that the new output appears.
3. **Calculate one beat.** Add a `double` variable for a tempo of 120 BPM. Calculate one quarter-note beat in milliseconds using `60000.0 / bpm`, then print the value with a label and unit. Predict before running; the result should be 500 ms.
4. **Change, rebuild, compare.** Change the tempo to 60, save, and run the old executable without rebuilding. Record what happens. Rebuild and run again; explain why the result changes only after rebuilding. Restore 120 BPM.
5. **Read a compiler error.** Remove one semicolon, save, and build. Read the first compiler error, restore the semicolon, and build successfully. Do not run the old executable after a failed build.

## Individual checkpoint

Independently, explain why changing and saving `main.cpp` does not by itself change the executable. Describe what you need to do before running the updated program.

## Practice after class

Extend the same `source/main.cpp` at 120 BPM. Calculate and print the quarter, eighth, dotted-quarter, and dotted-eighth durations in clearly named variables. Expected values: 500, 250, 750, and 375 ms.

## Build and run

Open **this session folder** in VS Code. Run these commands from its terminal after saving your files. Rebuild after every source change; these direct commands compile and link the file each time.

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

The first command compiles and links; the next commands run the executable. Run only after a successful build. Debug information and disabled optimization prepare the program for Session 05's debugger exercise.

No CMake is used in this lesson. CMake is introduced in Session 07. The supplied VS Code build task runs the compiler directly.
