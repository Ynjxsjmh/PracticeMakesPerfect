#include <algorithm>
#include <vector>
#include <iostream>
using namespace std;

void combination(vector<int>& candidates, int target, vector< vector<int> >& result, vector<int>& tempResult, int begin) {
    if (target == 0) {
        result.push_back(tempResult);
        return ;
    }

    for (int i = begin; i < candidates.size(); i++) {
        if (candidates[i] <= target && (i == begin || candidates[i] != candidates[i - 1])) {
            // if i = 0, i-1 will exceed. In that case, i == begin is a necessary
            tempResult.push_back(candidates[i]);
            combination(candidates, target-candidates[i], result, tempResult, i+1);
            tempResult.pop_back();
        }
    }
}

vector< vector<int> > combinationSum2(vector<int>& candidates, int target) {
    vector< vector<int> > result;
    vector<int> tempResult;

    sort(candidates.begin(), candidates.end());

    combination(candidates, target, result, tempResult, 0);

    return result;
}

int main() {
    vector<int> candidates;
    int arr[] = {10,1,2,7,6,1,5};
    int target = 8;

    for (int i = 0; i < 7; i++) {
        candidates.push_back(arr[i]);
    }

    combinationSum2(candidates, target);

    return 0;
}