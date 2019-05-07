bool VerifySquenceOfBST(vector<int> sequence) {
    // 最后一个是根，如果序列能划分为一个左边全比根小，右边全比根的大，则是。同时判断子序列。
    if (sequence.size() == 0) {
        return false;
    }

    return helper(sequence, 0, sequence.size()-1);
}

bool helper(vector<int>& sequence, int begin, int end) {
    if (begin > end) {
        return true;
    }

    int root = sequence[end];
    int index = begin;

    for (; index < end; index++) {
        if (sequence[index] > root) {
            break;
        }
    } // 到这里已经确保 index 前面的全比 root 小

    // 下面判断是否 index 后面都比 root 大
    for (int i = index; i < end; i++) {
        if (sequence[i] < root) {
            return false;
        }
    }

    return helper(sequence, begin, index-1) and helper(sequence, index, end-1);
}