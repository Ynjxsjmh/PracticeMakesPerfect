string LeftRotateString(string str, int n) {
    string result = "";

    for (int i = n ; i < str.size() + n; i++) {
        result += str[i%str.size()];
    }

    return result;
}