#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    int maxArea(vector<int>& height) {
        int maxArea = 0;
        int currentArea = 0;
        int l=0;
        int r=height.size()-1;
        while (l<r) {
            currentArea = (height.at(l) < height.at(r) ? height.at(l) : height.at(r)) * (r-l);
            if (currentArea>maxArea) {
                maxArea = currentArea;
            }

            if (height.at(l) > height.at(r)) {
                r--;
            } else {
                l++;
            }
        }
        return maxArea;
    }
};