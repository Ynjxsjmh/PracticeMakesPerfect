int GetNumberOfK(vector<int> data ,int k) {
    // 数组是排序的，增序 or 减序？

    int left = 0;
    int right = data.size();

    while (left < right) {
        int mid = left + (right - left)/2;

        if (data[mid] < k) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }

    int result = 0;

    while(left < data.size() && data[left++] <= k) {
        result++;
    }

    return result;
}