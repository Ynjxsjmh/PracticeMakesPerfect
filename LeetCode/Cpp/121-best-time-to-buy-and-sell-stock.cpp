#include <vector>
#include <iostream>
using namespace std;

int maxProfit(vector<int>& prices) {
    int result = 0;

    for (int i = 0; i < prices.size(); i++) {
        for (int j = prices.size()-1; j >= i; j--) {
            if (prices[j]-prices[i] > result) {
                result = prices[j] - prices[i];
            }
        }
    }

    return result;
}

int maxProfit2(vector<int>& prices) {
    // 前 i 天的最大收益 = max{前 i-1 天的最大收益，第 i 天的价格-前 i-1 天中的最小价格}
    if (prices.size() == 0) {
        return 0;
    }

    int minPrices = prices[0];
    int result = 0;

    for (int i = 0; i < prices.size(); i++) {
        result = max(result, prices[i]-minPrices);

        if (prices[i] < minPrices) {
            minPrices = prices[i];
        }
    }

    return result;
}