vector<int> GetLeastNumbers_Solution(vector<int> input, int k) {
    priority_queue<int> q;
    vector<int> result;

    if (input.size() < k) {
        return result;
    }

    for (int num : input) {
        q.push(num);

        if (q.size() > k) {
            q.pop();
        }
    }

    while (!q.empty()) {
        result.push_back(q.top());
        q.pop();
    }

    return result;
}
