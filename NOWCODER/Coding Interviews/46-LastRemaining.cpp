int LastRemaining_Solution(int n, int m) {
    if (m == 0 || n == 0) {
        return -1;
    }

    list<int> l;

    for (int i = 0; i < n; i++) {
        l.push_back(i);
    }

    int index = 0;

    while (l.size() > 1) {
        index = (index+m-1)%l.size();
        list<int>::iterator it = l.begin();
        std::advance( it, index );
        l.erase(it);
    }

    return l.front();
}