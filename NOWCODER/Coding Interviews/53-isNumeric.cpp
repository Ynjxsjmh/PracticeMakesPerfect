// 分类：字符串

bool isNumeric(char* string) {
    int sign = 0; // 符号位
    int dot = 0;  // 点是否出现
    int e = 0;    // e/E 是否出现

    for (int i = 0; i < strlen(string); i++) {
        if (string[i] == 'e' || string[i] == 'E') {
            if (string[i+1] == '\0') {
                // e 后面什么都没了
                return false;
            }

            if (e == 1) {
                // 不能出现两个e
                return false;
            }

            e = 1;
        } else if (string[i] == '+' || string[i] == '-') {
            if (sign == 1 && string[i-1] != 'e' && string[i-1] != 'E') {
                // 第二次出现符号位，则必须在e之后
                return false;
            }

            if (sign == 0 && i > 0 && string[i-1] != 'e' && string[i-1] != 'E') {
                // 第一次出现符号位，且不是在字符串开头，则也必须在e之后
                return false;
            }

            sign == 1;
        } else if (string[i] == '.') {
            // e后面不能接小数点，小数点不能出现两次
            if (e == 1 || dot == 1) {
                return false;
            }

            dot = 1;
        } else if (string[i] < '0' || string[i] > '9') {
            return false;
        }
    }

    return true;
}