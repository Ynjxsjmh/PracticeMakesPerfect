#include <vector>
#include <iostream>
using namespace std;

vector<vector<int>> combine(int n, int k) {
    vector<vector<int> > result;
    vector<int> tempResult;

    combination(n, k, result, tempResult, 1);

    return result;
}

void combination(int n, int k, vector<vector<int> >& result, vector<int>& tempResult, int begin) {
    if (k == 0) {
        result.push_back(tempResult);
        return ;
    }

    for (int i = begin; i <= n; i++) {
        tempResult.push_back(i);
        combination(n, k-1, result, tempResult, i+1);
        tempResult.pop_back();
    }
}