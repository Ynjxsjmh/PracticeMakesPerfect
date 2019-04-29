#include <map>
#include <string>
#include <iostream>

using namespace std;

int main() {
    int N;

    while (cin >> N && N != 0) {
        map<string, int> lookup;

        string cur;
        string most;
        int max = 0;

        for (int i = 0; i < N; i++) {
            cin >> cur;
            lookup[cur]++;

            if (lookup[cur] > max) {
                max = lookup[cur];
                most = cur;
            }
        }

        cout << most << endl;
    }

    return 0;
}