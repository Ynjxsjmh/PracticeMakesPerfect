void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
    vector<int> result(m+n);
    int i = 0, j = 0, z = 0;

    while (i < m && j < n) {
        if (nums1[i] < nums2[j]) {
            result[z++] = nums1[i++];
        } else {
            result[z++] = nums2[j++];
        }
    }

    while (i<m) {
        result[z++] = nums1[i++];
    }

    while (j<n) {
        result[z++] = nums2[j++];
    }

    return result;
}