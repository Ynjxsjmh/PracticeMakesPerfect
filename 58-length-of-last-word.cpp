int lengthOfLastWord(string s) {
    int count = 0;
    int k = s.size() - 1;

    while(s.size()) {
        if(s[s.size()-1] == ' ') s.erase(s.size()-1); //remove all trailing whitespace
        else break;
    }

    for (k = s.size() - 1; k >= 0; k--) {
        if (s[k] != ' ') {
            count++;
        } else {
            break;
        }
    }

    return count;
}