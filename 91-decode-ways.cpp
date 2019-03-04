#include <iostream>
using namespace std;
int numDecodings(string s) {
    if (s.length() == 0 || s.at(0) == '0') {
        return 0;
    }

    vector<int> dp(s.length()+1);

    dp[0] = 1;
    dp[1] = s.at(0) == '0' ? 0 : 1;

    for (int i = 2; i <= s.length(); i++) {
        if (stoi(s.substr(i-1,1)) >= 1 && stoi(s.substr(i-1,1)) <= 9) {
            dp[i] += dp[i-1];
        }

        if (stoi(s.substr(i-2,2)) >= 10 && stoi(s.substr(i-2,2)) <= 26) {
            dp[i] += dp[i-2];
        }
    }

    return dp[s.length()];
}


int numDecodings1(string s) {
    // 此法超时
    // 上楼梯
    int result = 0;

    if (s.at(0) == '0') {
        return 0;
    }

    if (s.length() <= 0) {
        return 0;
    }

    if (s.length() == 1) {
        return 1;
    }

    if (s.length() == 2) {
        if (stoi(s.substr(0,2)) > 26 && s.at(1) == '0') {  // "30"
            return 0;
        } else if (s.at(0) == '0' || s.at(1) == '0') {
            return 1;
        } else if (stoi(s.substr(0,2)) > 26) {
            return 1;
        } else {
            return 2;
        }
    }

    if (stoi(s.substr(0,1)) != 0) {
        result += numDecodings(s.substr(1));
    }

    if (stoi(s.substr(0,2)) >=10 && stoi(s.substr(0,2)) <= 26) {
        result += numDecodings(s.substr(2));
    }

    return result;
}