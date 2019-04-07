bool isHappy(int n) {
    int sum = 0;
    vector<int> past;

    while (sum != 1) {
        sum = 0;
        while (n) {
            int temp = n % 10;
            n /= 10;
            sum += temp * temp;
        }
        n = sum;

        if (find(past.begin(), past.end(), sum) != past.end()) {
            return false;
        }
        past.push_back(sum);
    }

    return true;
}