#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;

    for (int k = 1; k <= n; k++) {
        string a, b;
        vector<int> result;

        cin >> a >> b;

        string c = a;
        string d = b;

        if(a.size() < b.size()) {
            swap(a,b);
        }

		int la = a.size();
        int lb = b.size();

		reverse(a.begin(), a.end());
		reverse(b.begin(), b.end());

        int carry = 0;
        for (int i = 0; i < lb; i++) {
            int sum = (a[i] - '0') + (b[i] - '0') + carry;

            if (sum >= 10) {
                carry = 1;
                sum -= 10;
            } else {
                carry = 0;
            }

            result.push_back(sum);
        }

        for (int i = lb; i < la; i++) {
            int sum = (a[i] - '0') + carry;

            if (sum >= 10) {
                carry = 1;
                sum -= 10;
            } else {
                carry = 0;
            }

            result.push_back(sum);
        }

        if (carry == 1) {
            result.push_back(carry);
        }

        cout<<"Case " <<k<<":"<<endl;
        cout<<c<<" + "<<d<<" = ";
        for (int i = result.size()-1; i >= 0; i--) {
            cout<<result[i];
        }

        cout<<endl;
        if (k != n) {
            cout<<endl;
        }
    }

    return 0;
}