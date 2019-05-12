void permutate(int pos, string str, vector<string> & result) {
    if (pos == str.size()) {
        result.push_back(str);
        return;
    }

    unordered_set<char> st;

    for (int i = pos; i < (int)str.size(); i++) {
        if (st.count(str[i]) == 1) { continue; }
        st.insert(str[i]);

        swap(str[pos], str[i]);
        permutate(pos+1, str, result);
        swap(str[pos], str[i]);
    }
}

vector<string> Permutation(string str) {
    vector<string> result;

    if (str.size() <= 0) {
        return result;
    }

    permutate(0, str, result);
    sort(result.begin(), result.end()); // 得排下序
    return result;
}