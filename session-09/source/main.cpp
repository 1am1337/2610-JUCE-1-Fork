#include <iostream>
#include <memory>

struct Tempo
{
    explicit Tempo(double initialBpm) : bpm(initialBpm)
    {
        std::cout << "Construct " << bpm << "\n";
    }
    ~Tempo() { std::cout << "Destroy " << bpm << "\n"; }
    double bpm;
};

void setTempo(Tempo value)
{
    value.bpm = 60.0;
}

int main()
{
    Tempo original(120.0);
    setTempo(original);
    std::cout << "Original: " << original.bpm << "\n";
}
