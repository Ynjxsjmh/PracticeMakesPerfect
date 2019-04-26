int rectCover(int number) {
    if (number == 0) {
        return 0;
    }

    int result = 0;
    int a = 0;
    int b = 1;

    while (number--) {
        result = a+b;
        a = b;
        b = result;
    }

    return result;
}