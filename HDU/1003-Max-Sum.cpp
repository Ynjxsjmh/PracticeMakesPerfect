#include <stdio.h>

// 状态转移方程：sum[i] = max{sum[i-1]+a[i],a[i]}. (sum[i] 记录以a[i] 为子序列末端的最大连续和.)
int main() {
    int cases;
    scanf("%d", &cases);

    for (int k = 1; k <= cases; k++) {
        int num;
        int sum = -1001; // 不能为 INT_MIN，可能会溢出？
        int maxSum = -1001;
        int cur;
        int begin, end;  // 记录当前连续子序列的起始、结束位置
        int A, B;

        scanf("%d", &num);

        for (int i = 1; i <= num; i++) {
            scanf("%d", &cur);

            if (sum + cur < cur) {
                sum = cur;
                begin = end = i;
            } else {
                sum += cur;
                end++;
            }

            if (maxSum < sum) {
                maxSum = sum;
                A = begin, B = end;
            }
        }

        printf("Case %d:\n%d %d %d\n",k,maxSum,A,B);
        if(k-cases) puts("");
    }

    return 0;
}