#include <iostream>
#include <vector>

using namespace std;

int GetUglyNumber_Solution(int index) {
    int a2 = 0;
    int a3 = 0;
    int a5 = 0;

    if (index == 0) {
        return 0;
    }

    int temp = 0;
    vector<int> dp(index, 1);

    for (int i = 1; i < index; i++) {
        while (dp[a2]*2 <= dp[i-1]) a2++;
        while (dp[a3]*3 <= dp[i-1]) a3++;
        while (dp[a5]*5 <= dp[i-1]) a5++;

        temp = dp[a2]*2;
        if (temp > dp[a3]*3) temp=dp[a3]*3;
        if (temp > dp[a5]*5) temp=dp[a5]*5;

        dp[i] = temp;
    }

    return dp[index-1];
}

int main() {

    cout<<GetUglyNumber_Solution(2);

    return 0;
}