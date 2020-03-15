string multiply(string num1, string num2) {
    int m = num1.size();
    int n = num2.size();
    string sum(m+n, '0');

    for (int i = m-1; i >= 0; i--) {
        int carry = 0;
        for (int j = n-1; j >=0; j--) {
            carry += (sum[i+j+1] - '0') + (num1[i] - '0') * (num2[j] - '0');
            sum[i+j+1] = carry % 10 + '0';
            carry /= 10;
        }
        sum[i] += carry;
    }

    for (int i = 0; i < m + n; i++) {
        if (ans[i] != '0') {
            return ans.substr(i);
        }
    }

    return "0";
}