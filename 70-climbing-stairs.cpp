int climbStairs-non(int n) {
    int result = 0;
    int a = 0;
    int b = 1;

    for (int i = 0; i < n; ++i) {
        result = a + b;
        a = b;
        b = result;
    }

    return result;
}

int climbStairs(int n) {
    // 43 超时
    if (n == 2) {
        return 2;
    }

    if (n == 1) {
        return 1;
    }

    return climbStairs(n-1) + climbStairs(n-2);
}