int reverse(int x) {
    long sum = 0;

    while (x) {
        int rest = x % 10;

        if (sum*10 > 2147483647 || sum*10 < -2147483648) {
            return 0;
        }
        sum = sum*10 + rest;
        x = x / 10;
    }

    return sum;
}