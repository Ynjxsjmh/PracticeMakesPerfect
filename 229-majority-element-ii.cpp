vector<int> majorityElement(vector<int>& nums) {
    int count1 = 0, count2 = 0;
    int num1 = 0, num2 = 0;
    int n = nums.size();

    for (int i = 0; i < n; i++) {
        if (nums[i] == num1) {
            count1++;
        } else if (nums[i] == num2) {
            count2++;
        } else if (count1 == 0) {
            count1 = 1;
            num1 = nums[i];
        } else if (count2 == 0) {
            count2 = 1;
            num2 = nums[i];
        } else {
            count1--;
            count2--;
        }
    }

    std::cout<<num1<<" "<<num2;

    vector<int> result;

    if (count(nums.begin(), nums.end(), num1) > n/3) {
        result.push_back(num1);
    }

    if (num1 == num2) { // [0,0,0]
        return result;
    }

    if (count(nums.begin(), nums.end(), num2) > n/3) {
        result.push_back(num2);
    }

    return result;
}
