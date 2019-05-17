#include<bits/stdc++.h>

using namespace std;

/* 暴力超时
   int InversePairs(vector<int> data) {
   int count = 0;
   for (int i = 0; i < data.size()-1; i++) {
   for (int j = i + 1; j < data.size(); j++) {
   if (data[i] > data[j]) {
   count++;
   }
   }
   }

   return count%1000000007;
   }
*/

int mergeSort(vector<int> &data, vector<int> &copy, int left, int right) {
    if (left >= right) {
        return 0;
    } else {
        int mid = (right + left) / 2;
        long long res = 0;
        res += mergeSort(data, copy, left, mid);
        res += mergeSort(data, copy, mid + 1, right);

        int l = left, r = mid + 1, loc = left;
        while (l <= mid && r <= right) {
            if (data[l] <= data[r]) {
                copy[loc++] = data[l++];
            } else {
                copy[loc++] = data[r++];
                res += mid - l + 1;
            }
        }
        while (l <= mid) {
            copy[loc++] = data[l++];
        }
        while (r <= right) {
            copy[loc++] = data[r++];
        }
        for (int i = left; i <= right; i++) {
            data[i] = copy[i];
        }

        return res % 1000000007;
    }
}

int InversePairs(vector<int> data) {
    vector<int> copy(data);
    return mergeSort(data, copy, 0, data.size() - 1);
}
