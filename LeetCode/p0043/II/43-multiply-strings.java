// 标签：字符串、相乘

class Solution {
    public String multiply(String num1, String num2) {
        int m = num1.length();
        int n = num2.length();

        int[] pos = new int[m+n];

        for (int i = m - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                int product = (num1.charAt(i) - '0') * (num2.charAt(j) - '0');

                int pos1 = i + j;
                int pos2 = i + j + 1;

                int sum = product + pos[pos2];

                pos[pos1] += sum / 10;
                pos[pos2] = sum % 10;
            }
        }

        String result = "";

        int idx = 0;

        while (idx < m+n && pos[idx] == 0) {
            // 找到第一个不为0的位置
            idx += 1;
        }

        if (idx == m+n) {
            return "0";
        } else {
            for (int i = idx; i < m + n; i++) {
                result += pos[i];
            }
        }

        return result;
    }
}
