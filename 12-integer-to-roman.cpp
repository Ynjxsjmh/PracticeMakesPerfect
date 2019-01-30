class Solution {
public:
    string intToRoman(int num) {
        string result;
        string ch[13] = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        int represent[13] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};

        for (int i = 0; i < 13; i++) {
            while (num >= represent[i]) {
                num -= represent[i];
                result += ch[i];
            }
        }

        return result;
    }
};