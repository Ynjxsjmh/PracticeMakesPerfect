int FirstNotRepeatingChar(string str) {
    map<char, int> lookup;

    for (char ch : str) {
        lookup[ch]++;
    }

    for (int i = 0; i < str.size(); i++) {
        if (lookup[str[i]] == 1) {
            return i;
        }
    }

    return -1;
}