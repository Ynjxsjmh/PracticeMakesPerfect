#include <vector>
#include <iostream>
using namespace std;

void recrusive(vector<string>& result, string oneSolution, int left, int right, int n) {
    if (oneSolution.size() == 2 * n) {
        result.push_back(oneSolution);
        return;
    }

    if (left < n) {
        recrusive(result, oneSolution+"(", left+1, right, n);
    }

    if (right < left) {
        recrusive(result, oneSolution+")", left, right+1, n);
    }
}

vector<string> generateParenthesis(int n) {
    vector<string> result;
    recrusive(result, "", 0, 0, n);
    return result;
}