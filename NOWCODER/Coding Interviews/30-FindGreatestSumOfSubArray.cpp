int FindGreatestSumOfSubArray(vector<int> array) {
    int biggest = array[0];
    int MAX = array[0];

    for (int i = 1; i < array.size(); i++) {
        if (biggest + array[i] < array[i]) {
            biggest = array[i];
        } else {
            biggest += array[i];
        }

        if (MAX < biggest) {
            MAX = biggest;
        }
    }

    return MAX;
}