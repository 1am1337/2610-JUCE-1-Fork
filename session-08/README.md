# Session 08 — One small class

A supplied starting point, not a completed exercise. All tasks use only this session’s files.

## What you will learn

Distinguish a class from instances; use a constructor, private member, public method, and const member function.

## Tasks

1. Run the program with two Tempo instances and observe each stored BPM.
2. Add double beatDurationMs() const to Tempo, calculated from its private bpm member.
3. Print each object’s beat duration without exposing its private data.
4. Change only the second constructor argument and show that the first instance is unaffected.
5. Explain how both objects use the same methods but store separate data. Assume positive constructor inputs for this exercise.

## Check your result

Tempo(120) gives 500 ms; Tempo(60) gives 1000 ms. Changing one object’s input does not alter the other.

## Individual checkpoint

Create a third instance at 100 BPM and explain its 600 ms result.

## Optional extension

Add a setter that ignores nonpositive BPM and verify it preserves the previous valid value.

## Practice after class

Add `setBpm(double newBpm)` to `Tempo`. Accept only positive values; for zero or a negative value, preserve the current BPM. Try changing the first object and show that the second object's BPM and beat duration remain unchanged.

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
