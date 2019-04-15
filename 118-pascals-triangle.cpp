vector<vector<int>> generate(int numRows) {
    vector<vector<int>> result;

    for (int curRow = 0; curRow < numRows; curRow++) {
        vector<int> tempResult(curRow+1, 1);

        if (curRow > 1) {
            for (int col = 1; col < curRow; col++) {
                tempResult[col] = result[curRow-1][col-1] + result[curRow-1][col];
            }
        }

        result.push_back(tempResult);
    }

    return result;
}