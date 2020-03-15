#include <map>
#include <iostream>
using namespace std;

class Solution {
public:
    int romanToInt(string s) {
        map<string, int> lookup;
        lookup["M"] = 1000;
        lookup["CM"] = 900;
        lookup["D"] = 500;
        lookup["CD"] = 400;
        lookup["C"] = 100;
        lookup["XC"] = 90;
        lookup["L"] = 50;
        lookup["XL"] = 40;
        lookup["X"] = 10;
        lookup["IX"] = 9;
        lookup["V"] = 5;
        lookup["IV"] = 4;
        lookup["I"] = 1;

        int result = 0;

        for (int i = s.size()-1; i >= 0; i--) {
            if (i>0 && lookup[s.substr(i-1, 2)]) {
                result += lookup[s.substr(i-1, 2)];
                i--;
            } else {
                result += lookup.at(s.substr(i, 1));
            }
        }

        return result;
    }
};