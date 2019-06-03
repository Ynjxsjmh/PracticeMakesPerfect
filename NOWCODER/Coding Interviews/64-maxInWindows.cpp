// 分类：队列

vector<int> maxInWindows(const vector<int>& num, unsigned int size) {
    vector<int> result;
    deque<int> s;  // 存储num中的下标，最前面的是最大的那个

    if (size > num.size() || size <= 0) {
        return result;
    }

    for (int i = 0; i < num.size(); i++) {
        while (!s.empty() && num[s.back()] <= num[i]) {
            // 从后往前弹出比现在还要小的索引，保证s里的节点是可能最大的
            // 因为之前的若比还小，则不可能称为最大
            s.pop_back();
        }

        while (!s.empty() && i-s.front()+1>size) {
            // 控制具有最大值的索引和当前索引之差在size内
            // 控制窗口大小
            s.pop_front();
        }

        s.push_back(i);

        if (i+1 >= size) {
            result.push_back(num[s.front()]);
        }
    }

    return result;
}
