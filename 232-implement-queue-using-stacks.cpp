class MyQueue {
public:
    stack<int> s;
    /** Initialize your data structure here. */
    MyQueue() {

    }

    /** Push element x to the back of queue. */
    void push(int x) {
        stack<int> helper;

        while (!s.empty()) {
            helper.push(s.top());
            s.pop();
        }

        helper.push(x);

        while (!helper.empty()) {
            s.push(helper.top());
            helper.pop();
        }
    }

    /** Removes the element from in front of queue and returns that element. */
    int pop() {
        int x = s.top();
        s.pop();
        return x;
    }

    /** Get the front element. */
    int peek() {
        return s.top();
    }

    /** Returns whether the queue is empty. */
    bool empty() {
        return s.empty();
    }
};