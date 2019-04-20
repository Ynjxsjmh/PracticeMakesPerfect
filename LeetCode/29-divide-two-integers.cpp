int divide(int dividend, int divisor) {
    int sign = -1;
    if ((dividend < 0 && divisor < 0) || (dividend > 0 && divisor > 0)) {
        sign = 1;
    }

    long ldividend = abs((long)dividend);
    long ldivisor = abs((long)divisor);

    if (ldivisor == 0) {
        return INT_MAX;
    }

    if (ldividend == 0 || ldividend < ldivisor) {
        return 0;
    }

    long lans = recurseDivide(ldividend, ldivisor);

    int ans;
    if (lans > INT_MAX) {
        ans = (sign==1) ? INT_MAX : INT_MIN;
    } else {
        ans = lans * sign;
    }

    return ans;
}

long recurseDivide(long dividend, long divisor) {
    if (dividend < divisor) {
        return 0;
    }

    long sum = divisor;
    long mutiply = 1;

    while (sum+sum <= dividend) {
        sum += sum;
        mutiply += mutiply;
    }

    return mutiply + recurseDivide(dividend-sum, divisor);
}