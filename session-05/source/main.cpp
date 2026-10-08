#include <iostream>

double beatDurationMs(int bpm)
{
    double result = 60000 / bpm; // Deliberate arithmetic bug: investigate with the debugger.
    return result;
}

double twoBeatsMs(int bpm)
{
    double oneBeat = beatDurationMs(bpm);
    return 2.0 * oneBeat;
}

int main()
{
    int bpm = 137;
    double duration = twoBeatsMs(bpm);
    std::cout << duration << " ms\n";
}
