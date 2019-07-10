string reverseWords(string s) {
    string result = "";
    string word = "";

    for (int i = s.size()-1; i >= 0; i--) {
        if (s[i] == ' ') {
            result += word;
            if (word.size() != 0) {
                result += ' ';
            }
            word = "";
        } else {
            word.insert(0, 1, s[i]);
        }

        if (i == 0) {
            result += word;
            word = "";
        }
    }

    if (result[result.size()-1] == ' ') {
        result.erase(result.begin()+result.size()-1);
    }

    return result;
}