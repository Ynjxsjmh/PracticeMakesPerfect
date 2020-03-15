/**
 * Description
 * Given a string, find the length of the longest substring without repeating characters.
 *
 *
 * @author Ynjxsjmh
 * @email  ynjxsjmh@gmail.com
 * @since  2020-03-11 15:02
 * @tag    Hash Table, Two Pointers, String, Sliding Window
 * @repeat
 */

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> lookup;
        int len = s.size();
        int result = 0;
        int i = 0;
        int j = 0;

        while (i < len && j < len) {
            if (lookup.find(s[j]) == lookup.end()) {
                lookup.insert(s[j++]);
                result = max(result, j-i);
            } else {
                lookup.erase(s[i++]);
            }
        }

        return result;
    }
};
