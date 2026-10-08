# JUCE C++ 1 — Musikhochschule Karlsruhe

A practical introduction to C++ and JUCE for Music Informatics students. The course roadmap covers 17 sessions; topics and pacing may be adjusted as we learn what the group needs.

## Start here

We will set up VS Code and the C++ tools together in class. Bring your laptop. Use the [setup sheet](setup/README.md) during class, then begin with [Session 01](session-01/README.md). The full list of planned topics is in the [student roadmap](COURSE_PLAN.md).

JUCE itself is introduced later, so you do not need to install it before the first class.

## How the course works

- You will build your own small programs and keep your own code changes. Use the teacher's course files as a reference; your solution does not need to match them line for line.
- The course begins with console programs and later builds one modest JUCE application: one window, one or two controls, and one result.

To build and debug from the course root, open this folder in VS Code, choose **Build and launch a course session** in Run and Debug, and press **F5**. The build task prompts you to select Session 01–09, runs that session's own build task, and launches the result: direct compiler commands for Sessions 01–06 and CMake for Sessions 07–09. This root launcher requires Python 3; Windows users should start VS Code from a Developer Command Prompt. You can also open an individual session folder and use its own Run and Debug configuration.

Audio processing and plugin development are outside the required scope of this introductory course.
