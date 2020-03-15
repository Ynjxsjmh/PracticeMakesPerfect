#include <cstring>
#include <iostream>
using namespace std;


// 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

// Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.


//  超时

class Solution1 {
public:

    string longestPalindrome(string s) {
        int longest = -1;
        string result = "";

        if (s.length() <= 1) {
            return s;
        }

        for (int i = 0; i < s.length(); i++) {
            for (int j = i; j < s.length(); j++) {
                if ((j-i+1) > longest && isPalindrome(s.substr(i, j-i+1))) {
                    longest = j - i + 1;
                    result = s.substr(i, j-i+1);
                }
            }
        }

        return result;
    }

    bool isPalindrome(string s) {
        int l = 0;
        int r = s.length() - 1;

        while (l < r) {
            if (s[l] != s[r]) {
                return false;
            }

            l++;
            r--;
        }

        return true;
    }
};

int main() {
    string s = "ac";

    string ret = Solution().longestPalindrome(s);

    cout << ret << endl;

    return 0;
}
