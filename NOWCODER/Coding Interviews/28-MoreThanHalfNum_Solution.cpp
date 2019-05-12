int MoreThanHalfNum_Solution(vector<int> numbers) {
    int count = 0;
    int candidate;

    for (int i = 0; i < numbers.size(); i++) {
        if (count == 0) {
            candidate = numbers[i];
            count = 1;
        } else if (candidate == numbers[i]) {
            count++;
        } else {
            count--;
        }
    }

    count = 0;
    for (int i = 0; i < numbers.size(); i++) {
        if (candidate == numbers[i]) {
            count++;
        }
    }

    return count > numbers.size()/2 ? candidate : 0;
}