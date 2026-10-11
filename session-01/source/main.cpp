#include <iostream>

int main (int argc, char* argv[])
{
    // type name = value
    double  bpm  = 120.0;

    // type     name{ value };
    // double   bpm{ 120.0 };

    double msQuarter = 60000.0 / bpm;
    double msEighth = msQuarter / 2.;
    double msDottedQuarter = msQuarter * 1.5;
    double msDottedEighth = msEighth * 1.5;

    std::cout << "Hello Music!" << "\n";
    std::cout << "msQuarter = " << msQuarter << " ms\n";
    std::cout << "msEighth = " << msEighth << " ms\n";
    std::cout << "msDottedQuarter = " << msDottedQuarter << " ms\n";
    std::cout << "msDottedEighth = " << msDottedEighth << " ms\n";

    return 0;
}
