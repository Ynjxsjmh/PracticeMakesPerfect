bool IsContinuous ( vector<int> numbers ) {
    if (numbers.size() < 5) {
        return false;
    }

    std::sort(numbers.begin(), numbers.end());

    int count = 0;
    // 统计有多少个大小王
    for (int num : numbers) {
        if (num == 0) {
            count++;
        }
    }

    for (int num : numbers) {
        std::cout << num << " ";
    }

    int begin = count;
    for (int i = begin; i < numbers.size()-1; i++) {
        if (numbers[i] == numbers[i+1]) {
            return false;
        }

        if (numbers[i]+1 != numbers[i+1]) {
            count -= numbers[i+1]-numbers[i]-1;
        }
    }

    return count >= 0;
}

