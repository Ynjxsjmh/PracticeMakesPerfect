bool IsPopOrder(vector<int> pushV,vector<int> popV) {
    if (pushV.size() == 0) {
        return false;
    }

    stack<int> s;
    int popIndex = 0;

    for (int i=0; i < pushV.size(); i++) {
        s.push(pushV[i]);

        while (!s.empty() && s.top() == popV[popIndex]) {
            s.pop();
            popIndex++;
        }
    }

    return s.empty();
}