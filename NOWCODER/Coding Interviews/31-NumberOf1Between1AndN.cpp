int NumberOf1Between1AndN_Solution(int n) {
    int count = 0;

    for (int i = 1; i <= n; i++) {
        int temp = i;
        while (temp) {
            if (temp%10 == 1) {
                count++;
            }

            temp /= 10;
        }
    }

    return count;
}