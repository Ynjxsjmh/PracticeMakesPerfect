int StrToInt(string str) {
    int result = 0;
    int flag = 1;
    int first = 0;

    for (int i = 0; i < str.size(); i++) {
        if (str[i] == ' ') {
            continue;
        } else if (str[i] == '-' && first == 0) {
            flag = -1;
            first = 1;
        } else if (str[i] == '+' && first == 0) {
            flag = 1;
            first = 1;
        } else if ('0' <= str[i] && str[i] <= '9') {
            result = result*10 + str[i]-'0';
        } else {
            return 0;
        }
    }

    return result * flag;
}