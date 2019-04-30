#include <iostream>

using namespace std;

int main() {
    int n;

    while (cin >> n && n != 0) {
        int floor;
        int begin = 0;
        int sum = 0;
        while (n--) {
            cin >> floor;
            int up = floor - begin;
            if (up > 0) {
                sum += up * 6;
            } else {
                sum += (-up) * 4;
            }

            sum += 5;
            begin = floor;
        }

        cout << sum << endl;
    }

    return 0;
}