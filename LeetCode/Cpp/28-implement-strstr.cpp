int strStr(string haystack, string needle) {
    if (haystack.size() == 0 && needle.size() == 0) {
        return 0;
    }

    for (int i = 0; i < haystack.size(); i++) {
        int indexI = i;
        int indexJ = 0;
        while (indexI < haystack.size() && indexJ < needle.size()) {
            if (haystack[indexI] == needle[indexJ]) {
                indexI++;
                indexJ++;
            } else {
                break;
            }
        }

        if (indexJ == needle.size()) {
            return i;
        }
    }
    return -1;
}