#include <cstdio>
#include <string>
#include <iostream>

using namespace std;

int main() {
    /*
      1. 每盒奶只喝五天
      2. 小于200ml的奶直接忽略
      3. 算每天的平均花费而不是每毫升的平均花费
      4. 倘若两种奶的日花销相同，那么就只挑量大的那盒买
    */
    int T, N;

    scanf("%d", &T);

    for (int i = 0; i < T; i++) {
        scanf("%d", &N);

        string S;
        int P, V;

        float average;
        string brand;
        int vol;

		cin >> S;
        scanf("%d%d", &P, &V);

        brand = S;
        int day = V/200 > 5 ? 5 : V/200;
        if (day != 0) {
            average = float(P)/day;
            vol = V;
        }

        for (int j = 1; j < N; j++) {
            cin >> S;
            scanf("%d%d", &P, &V);
            day = V/200 > 5 ? 5 : V/200;

            if (day != 0) {
                float tempAverage = float(P)/day;

                if (tempAverage < average) {
                    average = tempAverage;
                    brand = S;
                    vol = V;
                }

                if (tempAverage - average < 0.0000000001 && V > vol) {
                    average = tempAverage;
                    brand = S;
                    vol = V;
                }
            }
        }

        cout<<brand<<endl;
    }

    return 0;
}
