vector<int> printMatrix(vector<vector<int> > matrix) {
    vector<int> result;

    if (matrix.size() <= 0) {
        return result;
    }

    int hBegin = 0;  // horizontal
    int hEnd = matrix.size()-1;
    int vBegin = 0;  // vertical
    int vEnd = matrix[0].size() - 1;

    while (hBegin <= hEnd && vBegin <= vEnd) {
        for (int col = vBegin; col <= vEnd; col++ ) {
            result.push_back(matrix[hBegin][col]);
        }
        hBegin++;

        if (hBegin > hEnd) {
            break;
        }

        for (int row = hBegin; row <= hEnd; row++) {
            result.push_back(matrix[row][vEnd]);
        }
        vEnd--;

        if (vBegin > vEnd) {
            break;
        }

        for (int col = vEnd; col >= vBegin; col--) {
            result.push_back(matrix[hEnd][col]);
        }
        hEnd--;

        if (hBegin > hEnd) {
            break;
        }

        for (int row = hEnd; row >= hBegin; row--) {
            result.push_back(matrix[row][vBegin]);
        }
        vBegin++;

        if (vBegin > vEnd) {
            break;
        }
    }

    return result;
}