#include <vector>
#include <iostream>
using namespace std;

int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
    int gasNum = gas.size();
    int start = -1;

    for (int i = 0; i < gasNum; i++) {
        if (gas[i] < cost[i]) {
            continue;
        }

        if (canComplete(gas, cost, i)) {
            start = i;
            break;
        }
    }

    return start;
}

bool canComplete(vector<int>& gas, vector<int>& cost, int start) {
    int left = 0;
    int gasNum = gas.size();
    for (int i = start; i < gasNum+start; i++) {
        left += gas[i%gasNum] - cost[i%gasNum];
        if (left < 0) {
            return false;
        }
    }
    return true;
}