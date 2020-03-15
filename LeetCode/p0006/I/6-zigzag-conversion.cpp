class Solution {
public:
    string convert(string s, int numRows) {
        /* *
         * 4 rows
         *0 L0     D6      R12   0->6->12 = step = 2*rows-2 = 6
         *1 E1   O5E7   I11I13   5->11 step = 6;   5:step - 1
         *2 E2 C4  I8 H10  N14
         *3 T3     S9      G15
         * */
        if (numRows == 1)
            return s;

        string result;
        int step = 2 * numRows - 2;
        int col = s.size() / step;

        if (s.size()%step)
            col++;

        for (int i = 0; i < numRows; i++) {
            for (int j = 0; j < col; j++) {
                result += s[i+j*step];

                if (i != 0 && i != numRows - 1 && ((j+1)*step-i) < s.size()) {
                    result += s[(j+1)*step-i];
                }
            }
        }
        return result;
    }
};