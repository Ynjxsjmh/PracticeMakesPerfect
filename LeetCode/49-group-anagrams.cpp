vector<vector<string>> groupAnagrams(vector<string>& strs) {
    vector<vector<string>> result;

    vector<string> lookup;

    for (int i = 0; i < strs.size(); i++) {
        string tempStr = strs[i];
        sort(tempStr.begin(), tempStr.end());
        vector<string>::iterator it = find(lookup.begin(), lookup.end(), tempStr);
        if (it == lookup.end()) {
            // 如果 lookup 里没有出现当前字符串
            lookup.push_back(tempStr);
            vector<string> one;
            one.push_back(strs[i]);
            result.push_back(one);
        } else {
            result[distance(lookup.begin(), it)].push_back(strs[i]);
        }
    }

    return result;
}