bool searchMatrix(vector<vector<int>>& matrix, int target) {
    if (matrix.size() == 0 || matrix[0].size() == 0 || target < matrix[0][0] || target > matrix[matrix.size()-1][matrix[0].size()-1]){
        return false;
    }

    int row = matrix.size()-1;
    for (int i = 0; i < matrix.size(); i++) {
        if (target < matrix[i][0]) {
            row = i-1;
            break;
        }
    }

    return helper(matrix[row], target, 0, matrix[row].size()-1);
}

bool helper(vector<int> check, int target, int l, int r) {
    if (l > r) {
        return false;
    }

    int mid = r - (r-l)/2;

    if (check[mid] == target) {
        return true;
    } else if (check[mid] > target) {
        return helper(check, target, l, mid-1);
    } else {
        return helper(check, target, mid+1, r);
    }
}

