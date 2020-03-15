#include <vector>
#include <queue>
#include <cstring>
#include <iostream>
using namespace std;

int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
    if (find(wordList.begin(), wordList.end(), endWord) == wordList.end()) {
        return 0;
    }

    int minChange = 0;
    queue<string> q;
    q.push(beginWord);

    while (!q.empty()) {
        int count = q.size();
        minChange++;

        for (int i = 0; i < count; i++) {
            std::string pattern = q.front();
            q.pop();

            vector<string>::iterator it = wordList.begin();

            while(it != wordList.end()) {
                if (isOnlyOneDiff(pattern, *it)) {
                    if (endWord.compare(*it) == 0) {
                        return minChange+1;
                    }
                    q.push(*it);
                    it = wordList.erase(it);
                } else {
                    it++;
                }
            }
        }
    }
    return 0;
}

bool isOnlyOneDiff(string pattern, string aim) {
    // if pattern and aim has only one difference, return true
    int sameNum = 0;
    for (int i = 0; i < pattern.length(); i++) {
        if (pattern[i] == aim[i]) {
            sameNum ++;
        }
    }

     return sameNum == pattern.length()-1 ? true : false;
}
