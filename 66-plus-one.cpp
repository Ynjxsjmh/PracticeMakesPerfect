vector<int> plusOne(vector<int>& digits) {
    int carry = 0;
    int len = digits.size() - 1;

    digits[len] += 1;

    if (digits[len] >= 10) {
        for (int i = len; i >= 0; i--) {
            digits[i] += carry;
            if (digits[i] >= 10) {
                carry = 1;
                digits[i] -= 10;
            } else {
                carry = 0;
            }
        }

        if (carry == 1) {
            digits.insert(digits.begin(), 1);
        }
    }

    return digits;
}