int evalRPN(vector<string>& tokens) {
    stack<int> s;
    int val1, val2, val;
    for (int i = 0; i < tokens.size(); i++) {
        // 标点符号 +, -, *, /
        if (tokens[i] == "+" || tokens[i] == "-" || tokens[i] == "*" || tokens[i] == "/") {
            val2 = s.top(); s.pop();
            val1 = s.top(); s.pop();
            if (tokens[i] == "+") val = val1 + val2;
            else if(tokens[i] == "-") val = val1 - val2;
            else if (tokens[i] == "*") val = val1 * val2;
            else val = val1 / val2;
            s.push(val);
        } else {
            s.push(atoi(tokens[i].c_str()));
        }
    }
    return s.top();
}

