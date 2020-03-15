#include <string>
#include <iostream>
using namespace std;

string countAndSay(int n) {
    string result = "1";

    while (n > 1) {
        result = count(result);
        n--;
    }

    return result;
}

string count(string numbers) {
    string result = "";
    for (int i = 0; i < numbers.size(); i++) {
        int count = 1;
        while (i < numbers.size()-1 && numbers[i] == numbers[i+1]) {
            count++;
            i++;
        }
        result += std::to_string(count) + numbers[i];
    }
    return result;
}
