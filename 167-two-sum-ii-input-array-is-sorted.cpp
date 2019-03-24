vector<int> twoSum(vector<int>& numbers, int target) {

    int i, j;
    vector<int> res;

    for (i = 0; i < numbers.size()-1; i++) {
        j = bsearch(numbers, i, target-numbers[i]);
        if (j != -1) {
            break;
        }
    }

    res.push_back(i+1);
    res.push_back(j+1);

    return res;
}

int bsearch(vector<int>& numbers, int i, int target) {
    int l = i+1;
    int r = numbers.size() - 1;

    while (l <= r) {
        int mid = r - (r-l)/2;

        if (numbers[mid] == target) {
            return mid;
        } else if (numbers[mid] < target) {
            l = mid + 1;
        } else {
            r = mid - 1;
        }
    }

    return -1;
}