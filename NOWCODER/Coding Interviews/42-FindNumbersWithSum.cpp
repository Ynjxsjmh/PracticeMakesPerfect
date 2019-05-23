vector<int> FindNumbersWithSum(vector<int> array,int sum) {
    int left = 0;
    int right = array.size()-1;
    vector<int> result;

    while (left < right) {
        int curSum = array[left]+array[right];
        if (curSum == sum) {
            result.push_back(array[left]);
            result.push_back(array[right]);
            break;
        } else if (curSum > sum) {
            right--;
        } else {
            left++;
        }
    }

    return result;
}