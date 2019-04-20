#include <iostream>
using namespace std;

class Solution {
public:
    string longestPalindrome(string s) {
        int maxLength = 0;
        string result;

        for (int i=0; i<s.size(); i++) {
            for (int j=i; j<s.size(); j++) {
                int begin = i;
                int end = j;
                while(begin <= end) {
                    if (s[begin] == s[end]) {
                        begin++;
                        end--;
                    } else {
                        break;
                    }
                }

                if (begin > end && (j-i+1)>maxLength) {
                    maxLength = j-i+1;
                    result = s.substr(i, j-i+1);
                }
            }
        }

        return result;
    }
};