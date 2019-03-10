#include <vector>
#include <iostream>
using namespace std;

int maxProfit(vector<int>& prices) {
    // finding next local minimum and next local maximum
    int result = 0;
    int i = 0;

    while (i < prices.size()) {
        // find next local minimum
        while (i < prices.size()-1 && prices[i+1] <= prices[i]) {
            i++;
        }

        // need increment to avoid infinite loop for "[1]"
        int min = prices[i++];

        // find next local maximum
        while (i < prices.size()-1 && prices[i+1]>= prices[i]) {
            i++;
        }

        result += i < prices.size() ? prices[i] - min : 0;
        i++;
    }

    return result;
}