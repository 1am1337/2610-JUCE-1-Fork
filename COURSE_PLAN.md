# JUCE C++ 1 — Student Roadmap

This course at Musikhochschule Karlsruhe moves from small C++ console programs to a simple JUCE desktop application. The roadmap shows the topics we expect to cover; we may adjust the pace or emphasis as we learn what the group needs.

We will set up VS Code and the C++ tools together in class. You do not need to install JUCE before we begin. CMake is used by the setup check, then introduced for lesson projects in Session 07.

## Sessions

- **Session 01 — First program:** write, build, and run a small C++ program; calculate and print musical durations.
- **Session 02 — Types, arithmetic, and conditions:** work with integer and floating-point calculations, constants, and conditions for handling tempo values.
- **Session 03 — Loops and small collections:** use loops and a fixed-size array to process a short sequence of musical notes.
- **Session 04 — Functions and scope:** pass values to functions, return results, and understand local variables.
- **Session 05 — Debugging with breakpoints:** launch the debugger, stop at a breakpoint, inspect values, step through code, and use the call stack.
- **Session 06 — Includes, headers, and the linker:** split a small program across source and header files; understand translation units, object files, and linking.
- **Session 07 — CMake and Git:** build a multi-file project with CMake, observe that a change to one source file does not require rebuilding every object file, and use Git to review and manage your own changes.
- **Session 08 — One small class:** define a class with private data and public methods, then create and use instances.
- **Session 09 — References, pointers, and lifetime:** compare values, references, and pointers; follow object lifetimes and automatic ownership.
- **Session 10 — JUCE Core as a dependency:** add JUCE to a CMake project and use a JUCE Core class in a console program.
- **Session 11 — First JUCE window:** follow application startup, create a window, and identify the main component.
- **Session 12 — Components and layout:** add controls and position them as the window changes size.
- **Session 13 — Callbacks and a working calculator:** connect a control to a calculation and update what the user sees.
- **Session 14 — Create a JUCE project from scratch:** use documentation to create and build a simple project in a new folder.
- **Session 15 — One personal feature:** specify and implement one small feature in your own application.
- **Session 16 — Verify, debug, and hand over:** check requirements, reproduce the build, debug problems, and report what you tested.
- **Session 17 — Demonstration and independent change:** demonstrate your application, explain how it works, and make a small change on your own.

## How we will work

- Keep programs small enough to understand and explain.
- Use the Git workflow agreed in class for your experience level; this may be a personal repository or a branch in the course repository. Your implementation does not need to match the teacher's line for line.
- Build and run your program to check its behavior. A successful build alone does not prove the result is correct.

The final application will be intentionally modest: one window, one or two controls, and one result. Audio processing and plugin development are outside this course's scope.
