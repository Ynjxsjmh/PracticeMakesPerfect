#include <vector>
#include <map>
#include <iostream>
using namespace std;

vector<int> findSubstring(string s, vector<string>& words) {
	if (words.size() <= 0) {
		return {};
	}

    int wordLen = words[0].size();
    int wordNum = words.size();
    vector<int> result;
    map<string, int> exsist, temp;

    for (int i = 0; i < wordNum; i++) {
        exsist[words[i]]++;
    }

    for (int i = 0; i < s.size()-wordLen*wordNum+1; i++) {
        temp.clear();

        int j = 0;
        for (j = 0; j < wordNum; j++) {
            string substr = s.substr(i+j*wordLen, wordLen);
            if (exsist.find(substr) == exsist.end()) {
                break;
            }
            temp[substr]++;
            if (exsist[substr] < temp[substr]) {
                break;
            }
        }

        if (j >= wordNum) {
            result.push_back(i);
        }
    }
    return result;
}