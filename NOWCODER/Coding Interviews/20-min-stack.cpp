class Solution {
public:
    stack<pair<int, int>> st;

    void push(int value) {
        int smallest;

        if (st.empty()) {
            smallest = value;
        } else {
            smallest = std::min(st.top().second, value);
        }

        st.push({value, smallest});
    }

    void pop() {
        st.pop();
    }

    int top() {
        return st.top().first;
    }

    int min() {
        return st.top().second;
    }
};