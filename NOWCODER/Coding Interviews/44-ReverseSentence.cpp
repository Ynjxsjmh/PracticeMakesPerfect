string ReverseSentence(string str) {
    string result = "";
    string tempResult = "";

    for (int i = 0; i < str.size(); i++) {
        if (str[i] != ' ') {
            tempResult += str[i];
        } else {
            result = tempResult + ' ' + result;
            tempResult = "";
        }
    }

    result = tempResult + ' ' + result;

    return result.substr(0, str.size());
}