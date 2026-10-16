#include <iostream>

int main()
{
    const double bpm = 301;
    
    if (bpm <= 0) {
       std::cout << "invalid Tempo";
       return 1;
    }

    const double msPerBeat = 60000 / bpm;
    std::cout << msPerBeat << " ms/beat\n"; 
    if (bpm <= 60)
    {
        std::cout << "slow\n";
    }
    if (bpm <= 120 && bpm >= 60){
        std::cout << "moderate\n";
    }
    if (bpm <= 180 && bpm >= 120){
        std::cout << "fast\n";
    }
    else
    {
        if (bpm >= 300)
        {
            std::cout << "bpm >= 300\n";
        }
        std::cout << "high\n";
    }

    return 0;
}
