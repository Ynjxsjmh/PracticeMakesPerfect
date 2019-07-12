// 标签：二叉树

vector<int> pathInZigZagTree(int label) {
    vector<int> num = {1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576};
    vector<int> result;

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