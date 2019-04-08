int calculate(string s) {
    s.erase(remove_if(s.begin(), s.end(), isspace(), s.end()));

    int result = 0;
    int number = 0;
    int sign = 1;

    for (int i = 0; i < s.size(); i++) {
        char c = s[i];
        if (c.isDigit()) {
            number = 10 * number + (c - '0');
        } else if (c == '+') {
            result += sign * number;
            number = 0;
            sign = 1;
        } else if (c == '-') {
            result += sign * number;
            number = 0;
            sign = -1;
        } else if (c == '(') {
            stack.push(result);
            stack.push(sign);
            sign = 1;
            result = 0;
        } else if (c == ')') {
            result += sign * number;
            number = 0;
            result *= stack.pop();  //stack.pop() is the sign before the parenthesis
            result += stack.pop();  //stack.pop() now is the result calculated before the parenthesis
        }
    }

    if (number != 0) {
        result += sign * number;
    }

    return result;
}