void setZeroes(vector<vector<int>>& matrix) {
    vector<vector<int>> points;

    for (int i = 0; i < matrix.size(); i++) {
        for (int j = 0; j < matrix[0].size(); j++) {
            if (matrix[i][j] == 0) {
                vector<int> point;
                point.push_back(i);
                point.push_back(j);
                points.push_back(point);
            }
        }
    }

    for (vector<int> point : points) {
        for (int row = 0; row < matrix.size(); row++) {
            matrix[row][point[1]] = 0;
        }

        for (int col = 0; col < matrix[0].size(); col++) {
            matrix[point[0]][col] = 0;
        }
    }
}