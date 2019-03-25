bool isPalindrome(string s) {
    for (int i = 0, len = s.size(); i < len; i++)
    {
        // check whether parsing character is punctuation or not
        if (ispunct(s[i])|| std::isspace(s[i]))
        {
            s.erase(i--, 1);
            len = s.size();
        }
    }

    int l = 0;
    int r = s.size() - 1;

    while (l<r) {
        if (tolower(s[l]) == tolower(s[r])) {
            l++;
            r--;
        } else {
            return false;
        }
    }

    return true;
}