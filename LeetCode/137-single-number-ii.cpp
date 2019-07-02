// 标签：位运算

int singleNumber(vector<int>& nums) {
    int a = 0;
    int b = 0;
    int temp;

    for (int c : nums) {
        temp = (~a&b&c) | (a&~b&~c);
        b = (~a&~b&c) | (~a&b&~c);
        a = temp;
    }

    // we need find the number that is 01,10 => 1, 00 => 0.
    return a | b;
}