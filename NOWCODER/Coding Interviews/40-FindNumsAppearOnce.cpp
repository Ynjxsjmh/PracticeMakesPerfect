void FindNumsAppearOnce(vector<int> data, int* num1, int *num2) {
    map<int, int> m;

    for (int num : data) {
        m[num] += 1;
    }

    int count = 1;
    for (map<int, int>::iterator it=m.begin(); it != m.end(); it++) {
        if (it->second == 1) {
            if (count == 1) {
                *num1 = it->first;
                count++;
            } else {
                *num2 = it->first;
            }
        }
    }
}