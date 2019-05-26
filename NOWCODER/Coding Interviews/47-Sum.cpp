int Sum_Solution(int n) {
    int sum = 0;
    bool ans = (n > 0) && ((sum = n + Sum_Solution(n-1))>0);
    return sum;
}