vector<vector<int> > FindContinuousSequence(int sum) {
    vector<vector<int> > result;
    int small = 1;
    int big = 2;
    int mid = (1+sum)/2;

    while (small < mid) {
        int curSum = (small + big) * (big - small + 1) / 2;
        if (curSum == sum) {
            store(result, small, big);
            small++;
        } else if (curSum < sum) {
            big++;
        } else {
            small++;
        }

    }

    return result;
}

void store(vector<vector<int> >& result, int small, int big) {
    vector<int> temp;

    for (int i = small; i <= big; i++) {
        temp.push_back(i);
    }

    result.push_back(temp);
}