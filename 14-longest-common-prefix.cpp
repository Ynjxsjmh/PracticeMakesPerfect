class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        /* 两两字符串比较，利用传递性 */
        if (strs.size() == 0) return "";
        int maxLength = strs[0].size();

        for (int i = 0; i < strs.size()-1; i++) {
            int len1 = strs[i].size();
            int len2 = strs[i+1].size();
            int tempLength = 0;
            int j = 0;

            while (j < len1 && j < len2) {
                if (strs[i][j] != strs[i+1][j]) {
                    break;
                } else {
                    tempLength++;
                    j++;
                }
            }

            maxLength = tempLength < maxLength ? tempLength : maxLength;
        }

        return strs[0].substr(0, maxLength);
    }
};