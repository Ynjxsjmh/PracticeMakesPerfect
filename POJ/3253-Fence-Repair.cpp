#include <cstdio>
#include <algorithm>
#include <iostream>

using namespace std;


// 一开始以为是从大到小排个序，然后切最大的，理解错了。
int main(int argc, char *argv[]) {
    int n;
    long long sum;

    while (~scanf("%d", &n)) {
        long long length[n];

        for (int i = 0; i < n; ++i) {
            scanf("%I64d", &length[i]);
        }

        sort(length, length+n);
        int i = 0;
        sum = 0;

        while (i < n-1) {
            // 每次取最小的两个数
            length[i+1] = length[i] + length[i+1];
            sum += length[i+1];
            for (int j = i + 1; j < n-1; j++) {
                // 因为之前已经排好序，因此现在只有 i+1 不是顺序的，交换成排好序的即可
                if (length[j] > length[j+1]) {
                    swap(length[j], length[j+1]);
                }
            }
            i++;
        }

        printf("%I64d\n", sum);
    }

    return 0;
}


/*
#include <cstdio>
#include <vector>
#include <algorithm>
#include <functional>
#include <iostream>

using namespace std;

bool cmp(long long a, long long b) {
    return a > b;
}

int main(int argc, char *argv[]) {
    int N;
//    long long a[20010];
    vector<long long> a(20010);
    long long sum = 0;
    long long cost = 0;

    scanf("%d", &N);

    for (int i = 0; i < N; i++) {
        scanf("%I64d", &a[i]);
        sum += a[i];
    }

    std::sort(a.begin(), a.begin()+N, std::greater<long long>());
//    std::sort(a, a+N, std::greater<long long>());
//    std::sort(a, a+N, cmp);

    if (N == 1) {
        printf("%I64d\n", a[0]);
    } else {
        for (int i = 0; i < N-1; i++) {
            cost += sum;
            sum -= a[i];
        }

        printf("%I64d\n", cost);
    }

    return 0;
}
*/
