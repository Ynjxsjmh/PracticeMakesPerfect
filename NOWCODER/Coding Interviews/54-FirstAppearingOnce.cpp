// 分类：字符串

class Solution {
public:
    int hash[256] = {0}; // Ascii 码有 256 个
    int last_one = 0;
    string s;

    //Insert one char from stringstream
    void Insert(char ch) {
        s += ch;
        hash[ch]++;
    }

    //return the first appearence once char in current stringstream
    char FirstAppearingOnce() {
        for (int i = last_one; i < s.size(); i++) {
            if (hash[s[i]] == 1) {
                last_one = i;
                return s[i];
            }
        }

        return '#';
    }
};