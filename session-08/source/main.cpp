#include <iostream>

class Tempo
{
public:
    explicit Tempo(double initialBpm) : bpm(initialBpm) {}
    double getBpm() const { return bpm; }
    // TODO: add a const method that returns beat duration in milliseconds.
private:
    double bpm;
};

int main()
{
    Tempo first(120.0);
    Tempo second(60.0);
    std::cout << first.getBpm() << " BPM\n";
    std::cout << second.getBpm() << " BPM\n";
}
