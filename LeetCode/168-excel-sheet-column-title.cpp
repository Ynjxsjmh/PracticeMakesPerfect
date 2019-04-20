string convertToTitle(int n) {
    string result = "";

    while (n > 0) {
        result = (n % 26 + 'A') + result;
        n /= 26;
    }

    return result;
}