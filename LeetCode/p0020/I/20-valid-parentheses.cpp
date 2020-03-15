#include <stack>
#include <map>
#include <iostream>
using namespace std;

bool isValid(string s) {
    map<char, char> lookup;
    lookup[')'] = '(';
    lookup[']'] = '[';
    lookup['}'] = '{';

    stack<char> left;
    for (int i = 0; i < s.size(); i++) {
        if (s[i] == '('|| s[i] == '[' || s[i] == '{') {
            left.push(s[i]);
        } else {
            if (!left.empty() && left.top() == lookup[s[i]]) {
                left.pop();
				continue;
            } else {
                return false;
            }
        }
    }

    if (left.empty()) {
        return true;
    }

    return false;
}

int main() {
    string test = "[]";
    cout<<isValid(test)<<endl;
}