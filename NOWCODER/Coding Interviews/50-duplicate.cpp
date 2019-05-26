bool duplicate(int numbers[], int length, int* duplication) {
    // 首先这题给出一个条件是所有数都在 0~n-1 内
    for (int i = 0; i < length; i++) {
        int index = numbers[i]%length;  // 保证范围在 0~n-1 内

        if (numbers[index] >= length) {
            *duplication = index;
            return true;
        }

        numbers[index] += length; // 标记这个被索引到的数已经被一个数索引到了
    }

    return false;
}