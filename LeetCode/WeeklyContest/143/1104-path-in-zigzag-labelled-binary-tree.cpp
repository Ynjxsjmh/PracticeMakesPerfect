// 标签：二叉树

vector<int> pathInZigZagTree(int label) {
    vector<int> num;
    vector<int> result;

    int i = 1;
    int count = 0;
    int range = pow(10, 6);

    // 首先算出每一层有多少个节点
    while (2*i-1 < range) {
        num.push_back(i);
        count++;
        i = pow(2, count);
    }
    num.push_back(2*i);

    int last;
    for (int i = 0; i < num.size(); i++) {
        if (label == 1) {
            result.insert(result.begin(), label);
            break;
        }

        if (label < num[i]) {
            result.insert(result.begin(), label);
            last = num[i];
            label = (last-1-label)/2 + last/4; // last/4 是上一层的起始节点，last-1是这一层的最后一个节点，(last-1-label)/2是父节点与其对应层起始节点的偏移
            i = 0;
        }
    }

    return result;
}