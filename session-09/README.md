# Session 09 — References, pointers, and lifetime

A supplied starting point, not a completed exercise. All tasks use only this session’s files.

## What you will learn

Distinguish a value copy, reference, and pointer; predict local destruction order; recognize automatic ownership with unique_ptr.

## Tasks

1. Predict what the supplied program prints: does changing the argument by value change original.bpm? Then build and run `source/main.cpp` to check.
2. Change setTempo to take Tempo& and verify that it updates the original.
3. Create a pointer to original and print its bpm through ->. Explain why the pointer does not own the local object.
4. Use an inner brace scope with a Tempo object. Watch the constructor/destructor messages; explain reverse destruction order.
5. With the teacher, create a std::unique_ptr<Tempo> in an inner scope using std::make_unique. Observe automatic destruction; do not write delete.

## Check your result

Value parameter leaves original.bpm at 120. Reference parameter changes it to 60. Inner objects die at their closing brace; unique_ptr destroys its owned object when it leaves scope.

## Individual checkpoint

Identify which variable owns storage and which only refers to it. Explain why a dangling pointer must not be dereferenced.

## Optional extension

Use const Tempo& in a read-only print helper and explain why it cannot modify bpm.

## Practice after class

Write `makeTempo(double bpm)` to return a `std::unique_ptr<Tempo>` created with `std::make_unique`. Call it from an inner scope, print the owned object's BPM, and observe the destructor message when the scope ends. Do not access the object after its owner is destroyed.

## Build and run

Open **this session folder** in VS Code, not the course root. Save your changes in this session folder and follow the Git workflow agreed in class. Complete [setup](../setup/README.md) first. These are supplied build commands until session 7 explains CMake.

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
