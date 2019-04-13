vector<int> grayCode(int n) {
    vector<int> result;
    vector<int> gray;

    for (int i = 0; i < n; i++) {
        gray.push_back(0);
    }

    result.push_back(0);

    while (result.size() < pow(2,n)) {
        /*
         * 第一步，改变最右边的位元值；
         * 第二步，改变右起第一个为1的位元的左边位元；
         * 第三步，第四步重复第一步和第二步，直到所有的格雷码产生完毕
         */

        gray[gray.size()-1] = 1 - gray[gray.size()-1];
        result.push_back(conversion(gray));

        if (result.size() < pow(2,n)) {
            for (int i = gray.size()-1; i >= 0; i--) {
                if (gray[i] == 1) {
                    gray[i-1] = 1 - gray[i-1];
                    break;
                }
            }

            result.push_back(conversion(gray));
        }
    }

    return result;
}

int conversion(vector<int> code) {
    int sum = 0;
    for (int i = 0; i < code.size(); i++) {
        sum = sum*2 + code[i];
    }
    return sum;
}