int findMin(vector<int> rotateArray) {
    if (rotateArray.size() == 0) {
        return 0;
    }

    int left = 0;
    int right = rotateArray.size() - 1;

    while (left < right) {
        int mid = left + (right - left) / 2;

        //确认子数组是否是类似1,1,2,4,5,..,7的非递减数组
        if (rotateArray[left] < rotateArray[right]) return rotateArray[left];

        if (rotateArray[mid] > rotateArray[left]) {
            // 左半部分有序
            left = mid + 1;
        } else if (rotateArray[mid] < rotateArray[right]) {
            // 右半部分有序
            right = mid;
        } else {
            left++;
        }
    }

    return rotateArray[left];
}