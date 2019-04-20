bool Find(int target, vector<vector<int> > array) {
    int row = 0;
    int col = array[0].size() - 1;

    while (row <= array.size()-1 && col >= 0) {
        if (target == array[row][col]) {
            return true;
        } else if (target > array[row][col]) {
            row++;
        } else {
            col--;
        }
    }

    return false;
}

/*
利用二维数组由上到下，由左到右递增的规律，
那么选取右上角的元素a[row][col]与target进行比较，
当target小于元素a[row][col]时，那么target必定在元素a所在行的左边,
即col--；
当target大于元素a[row][col]时，那么target必定在元素a所在列的下边,
即row++；

左下角
当要查找数字比左下角数字大时。右移 col++
当要查找数字比左下角数字小时，上移 row--
 */