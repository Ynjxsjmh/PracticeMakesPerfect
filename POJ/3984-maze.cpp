#include <cstdio>
#include <vector>

using namespace std;

int maze[5][5];

int direction[4][2] = { { -1, 0 }, { 0, 1 }, { 1, 0 }, { 0, -1 } };

void bfs(int x, int y, vector<pair<int, int> >& tempResult, vector<vector<pair<int, int> > >& result) {
    if (maze[x][y] == 1) {
        return ;
    }

    if (!(0 <= x && x < 5 && 0 <= y && y < 5)) {
        return ;
    }

    if (x == 4 && y == 4) {
        result.push_back(tempResult);
        return ;
    }

    tempResult.push_back({x, y});
    maze[x][y] = 1; // 已访问过的置 1

    for (int i = 0; i < 3; i++) {
            int nx = x + direction[i][0];
            int ny = y + direction[i][1];
            bfs(nx, ny, tempResult, result);
    }

    maze[x][y] = 0;
    tempResult.pop_back();

    return ;
}

int main(int argc, char *argv[]) {
    vector<pair<int, int> > tempResult;
    vector<vector<pair<int, int> > > result;

    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            scanf("%d", &maze[i][j]);
        }
    }

    bfs(0, 0, tempResult, result);

    int min_index;
    int min_size = 9999999;
    for (int i = 0; i < result.size(); i++) {  // 可能有多个解，找到最小的那个
        if (result[i].size() < min_size) {
            min_size = result[i].size();
            min_index = i;
        }
    }

    for (int i = 0; i < result[min_index].size(); i++) {
        printf("(%d, %d)\n", result[min_index][i].first, result[min_index][i].second);
    }

    printf("(4, 4)\n");

    return 0;
}
