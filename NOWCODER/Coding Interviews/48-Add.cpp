#include <iostream>
using namespace std;

/*
   第一步：相加各位的值，不算进位，并将该值作为 num1。二进制每位相加就相当于各位做异或操作

   第二步：计算进位值，并将该值作为 num2。相当于各位做与操作，再向左移一位（如 01&01=1，左移得 10，10 为进位值）

   第三步：重复上述两步直到进位值为 0（为什要不断重复？因为不能用加法，还得继续用位运算模拟加法）

   计算二进制值相加： 101（5）+111（7）

loop1
   101 + 111 不算进位得 010

   101 & 111 得 101，左移得 1010

loop2
   010 + 1010 不算进位得 1000

   010 & 1010 得 10，左移得 100

loop3
   1000 + 100 不算进位得 1100

   1000 & 100 得 0，终止。上一步的 1100 为最终结果。
*/

int Add(int num1, int num2) {
    while (num2 != 0) {
        int temp = num1^num2;
        num2 = (num1&num2)<<1;
        num1 = temp;
    }

    return num1;
}

int main(int argc, char *argv[]) {
    Add(2, 3);
    return 0;
}