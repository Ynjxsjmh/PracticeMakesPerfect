#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

void permutation2(vector<int>&  nums, vector<vector<int> >& result, vector<int>& tempResult) {

    if (nums.size() == tempResult.size()) {
        result.push_back(tempResult);
        return ;
    }

    for (int i = 0; i < nums.size(); i++) {
        if (std::find(tempResult.begin(), tempResult.end(), nums[i]) != tempResult.end()) {
            continue;
        }

        tempResult.push_back(nums[i]);
        permutation(nums, result, tempResult);
        tempResult.pop_back();
    }
}

void permutation(vector<int>  nums, vector<vector<int> > & result, vector<int> & tempResult) {
    if (nums.size() <= 0) {
        result.push_back(tempResult);
        return ;
    }

    for (int i = 0; i < nums.size(); i++) {
        vector<int> tempNums(nums);
        tempResult.push_back(nums[i]);
        tempNums.erase(tempNums.begin()+i); // This line sucks. I take tempResult as tempNums, that confuses me nearly two hours.
        permutation(tempNums, result, tempResult);
        tempResult.pop_back();
    }
}

vector<vector<int> > permute(vector<int>& nums) {
    vector<vector<int> > result;
    vector<int> tempResult;

    permutation(nums, result, tempResult);

    return result;
}


int main() {
    int arr[] = {1, 2, 3};
    vector<int> nums;

    for (int i = 0; i < 3; i++) {
        nums.push_back(arr[i]);
    }

    permute(nums);

    return 0;
}
