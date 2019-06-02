// 分类：中位数

class Solution {
public:
    vector<int> v;
    void Insert(int num) {
        int index;

        for (int i = 0; i < v.size(); i++) {
            if (v[i] > num) {
                index = i;
                break;
            }
        }

        v.insert(v.begin()+index, num);
    }

    double GetMedian() {
        int len = v.size();
        if (len % 2 == 1) {
            return v[len/2];
        } else {
            return (v[len/2]+v[len/2-1])*1.0/2;
        }
    }

};