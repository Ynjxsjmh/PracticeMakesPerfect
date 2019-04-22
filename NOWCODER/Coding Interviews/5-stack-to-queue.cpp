class Solution
{
public:
    void push(int node) {
        while(!stack2.empty()) {
            stack1.push(stack2.top());
            stack2.pop();
        }
        stack1.push(node);

        while(!stack1.empty()) {
            stack2.push(stack1.top());
            stack1.pop();
        }
    }

    int pop() {
        int a = stack2.top();
        stack2.pop();
        return a;
    }

private:
    stack<int> stack1;
    stack<int> stack2;
};