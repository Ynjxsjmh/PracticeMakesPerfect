#include <vector>
#include <iostream>
using namespace std;

int  NumberOf1(int n) {
    if (n == -2147483648) {
        return 1;
    }

    int flag = 1;
    int count = 0;
    vector<int> result;

    if (n < 0) {
        flag = -1;
        n = -n;
    }

    while (n) {
        result.insert(result.begin(), n%2);
        n /= 2;
    }

    while (result.size() != 32) {
        result.insert(result.begin(), 0);
    }

    if (flag == -1) {
        bool first = true;
        for (int i = result.size()-1; i >= 0; i--) {
            if (result[i] != 1 && first) {
                continue;
            } else if (result[i] == 1 && first) {
                first = false;
                continue;
            } else {
                result[i] = 1 - result[i];
            }
        }
    }

    for (int i = 0; i < result.size(); i++) {
        if (result[i] == 1) {
            count++;
        }
    }

    return count;
}

int main() {
    int n = -2147483648;
    std::cout << NumberOf12(n) << std::endl;
    return 0;
}