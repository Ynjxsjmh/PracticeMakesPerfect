void reOrderArray(vector<int> &array) {
    vector<int> temp = array;

    int odd = 0;
    for (int i = 0; i < array.size(); i++) {
        if (temp[i] % 2 == 1) {
            array[odd] = temp[i];
            odd++;
        }
    }

    int even = odd;
    for (int i = 0; i < array.size(); i++) {
        if (temp[i] % 2 == 0) {
            array[even] = temp[i];
            even++;
        }
    }
}