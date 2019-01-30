#include <set>
#include <iostream>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int maxLength = 0;
        for (int i = 0; i < s.size(); i++) {
            int j = i+1;
            set<char> exsist;
            exsist.insert(s[i]);
            while (j<s.size()) {
                if (exsist.find(s[j]) == exsist.end()) {
                    exsist.insert(s[j]);
                    j++;
                } else {
                    break;
                }
            }
            if (maxLength < exsist.size()) {
                maxLength = exsist.size();
            }
        }
        return maxLength;
    }
};