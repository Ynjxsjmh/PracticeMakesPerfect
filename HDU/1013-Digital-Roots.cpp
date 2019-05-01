#include <iostream>
using namespace std;

int main() {
    string digit;

    while (cin >> digit && digit != "0") {
        int sum = 0;

        for (int i = 0; i < digit.size(); i++) {
            sum += digit[i] - '0';
        }

        while (sum >= 10) {
            sum = sum % 10 + sum/10;
        }

        cout << sum << endl;
    }

    return 0;
}