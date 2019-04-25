int jumpFloorII(int number) {
    if (number == 0) {
        return 1;
    }

    int count = 0;

    for (int i = 1; i <= number; i++) {
        count += jumpFloorII(number-i);
    }

    return count;
}