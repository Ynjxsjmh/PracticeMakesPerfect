// 分类：回溯

int movingCount(int threshold, int rows, int cols) {
    vector<int> v(rows*cols, 0);
    int count = 0;

    helper(v, threshold, rows, cols, 0, 0);

    for (int i = 0; i < v.size(); i++) {
        if (v[i] == 1) {
            count++;
        }
    }

    return count;
}

int count_x_y(int x, int y) {
    int sum = 0;

    while (x) {
        sum += x%10;
        x /= 10;
    }

    while (y) {
        sum += y%10;
        y /= 10;
    }

    return sum;
}

void helper(vector<int>& v, int threshold, int rows, int cols, int x, int y) {
    if (count_x_y(x, y) > threshold) {
        // 不符合要求
        return ;
    }

    if (v[x*cols+y] == 1) {
        // 已经走过
        return ;
    }

    if (x >= rows || x < 0 || y >= cols || y < 0) {
        // 越界
        return ;
    }

    v[x*cols+y] = 1; // 可以到达

    helper(v, threshold, rows, cols, x+1, y);
    helper(v, threshold, rows, cols, x-1, y);
    helper(v, threshold, rows, cols, x, y+1);
    helper(v, threshold, rows, cols, x, y-1);
}