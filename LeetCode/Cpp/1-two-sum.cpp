#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
    	vector<int> result;
        for (int i = 0; i < nums.size(); i ++) {
            if ((nums[i] > target && nums[i] > 0) || (nums[i] < target && nums[i] < 0)) {
                continue;
            }

            for (int j = i+1; j < nums.size(); j++) {
                if ((nums[i] + nums[j]) == target) {
                    result.push_back(i);
                    result.push_back(j);
                }
            }
        }
        return result;
    }
};

int main() {
    Solution* solution = new Solution;
    int inputArray[4] = {2, 7, 11, 15};
    vector<int> inputVector;

    for (int i=0; i<sizeof(inputArray)/sizeof(inputArray[0]); i++) {
    	inputVector.push_back(inputArray[i]);
	}

	for (int i=0; i<solution->twoSum(inputVector, 9).size(); i++) {
		cout<<solution->twoSum(inputVector, 9)[i];
	}
}
