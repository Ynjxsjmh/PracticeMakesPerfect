#include <cmath>
#include <iostream>
using namespace std;

// 快速幂
double Power(double base, int exponent) {
    double result = 1;
    int p = exponent;
    exponent = abs(exponent);
    while (exponent) {
        if (exponent & 1) {
            result *= base;
        }
        base *= base;
        exponent >>= 1;
    }

    return p < 0 ? 1/result : result;
}

int main() {
    std::cout << Power(3, 3) << std::endl;
    return 0;
}