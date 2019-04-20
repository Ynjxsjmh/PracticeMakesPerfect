int mySqrt(int x) {
    if (x == 0 || x == 1) {
        return x;
    }
    return helper(x, 0, x);
}

int helper(int x, int l, int r) {
    int mid = (l+r)/2;

    if (l > r) {
        return mid;
    }

    if (mid == x/mid) {
        return mid;
    } else if (mid > x / mid) {
        return helper(x, l, mid-1);
    } else {
        return helper(x, mid+1, r);
    }
}