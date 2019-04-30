#include <vector>
#include <cstdio>
#include <iostream>

using namespace std;

int main() {
    vector<int> fac(11, 1);

    for (int i = 1; i < fac.size(); i++) {
        fac[i] = fac[i-1] * i;
    }

    cout << "n e" << endl;
    cout << "- -----------" << endl;


    double sum = 0;  // float 精度不够。。
    for (int n = 0; n < 10; n++) {
        sum += (double)1/fac[n];

        if (n == 0) {
            printf("0 1\n");
        } else if (n == 1) {
            printf("1 2\n");
        } else if (n == 2) {
            printf("2 2.5\n");
        } else {
            printf("%d %.9f\n", n, sum);
        }

    }

    return 0;
}

/*
  #include <iostream>
  #include <cstdio>
  using namespace std;
  double make(int n)
  {
  double sum = 1.0;
  for(int i = 1; i <= n; i++)
  sum *= i;
  return 1.0/sum;
  }
  int main()
  {
  double sum = 2.5;
  printf("n e\n");
  printf("- -----------\n");
  printf("0 1\n");
  printf("1 2\n");
  printf("2 2.5\n");
  for(int i = 3; i <= 9 ; i ++)
  {
  sum += make(i);
  printf("%d %.9f\n",i,sum);
  }
  return 0;
  }
*/