/**
 * Description
 *
 *
 * Example
 * Input:
 * Output:
 * Explanation:
 *
 * @author Ynjxsjmh
 * @email  ynjxsjmh@gmail.com
 * @since  2020-04-30 19:23
 * @tag    stack
 * @repeat
 */


class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        map<char, char> lookup = {{'{', '}'},
                                  {'[', ']'},
                                  {'(', ')'}};

        for (size_t i = 0; i < s.size(); i++) {
            if (s[i] == '(' || s[i] == '{' || s[i] == '[') {
                st.push(s[i]);
            }

            if (s[i] == ')' || s[i] == '}' || s[i] == ']') {
                if (st.empty() || lookup[st.top()] != s[i]) {
                    return false;
                }
                st.pop();
            }
        }

        return st.empty();
    }
};
