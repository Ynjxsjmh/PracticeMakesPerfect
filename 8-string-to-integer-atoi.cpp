int myAtoi(string str) {
    long sum = 0;
    int sign = 1;

    for (int i = 0; i < str.size(); i++) {
        while (i < str.size() && str[i] == ' ') {
            // if begin with a series of spaces, skip them
            i++;
        }

        // judge the sign
        if (i < str.size() && str[i] == '-') {
            sign = -1;
            i++;
        } else if (i < str.size() && str[i] == '+') {
            sign = 1;
            i++;
        }

        // handle the sumber
        while (i < str.size() && str[i] >= '0' && str[i] <= '9') {
            if (sign * sum * 10 > INT_MAX || sign * (sum * 10 + str[i] - '0') > INT_MAX) {
                return INT_MAX;
            }

            if (sign * sum * 10 < INT_MIN || sign * (sum * 10 + str[i] - '0') < INT_MIN) {
                return INT_MIN;
            }

            sum = sum * 10 + str[i] - '0';
            i++;
        }

        break;
    }

    return sign * sum;
}