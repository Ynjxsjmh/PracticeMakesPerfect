vector<vector<string>> partition(string s) {
    vector<vector<string>> result;
    vector<string> part;

    partite(s, 0, s.size()-1, result, part);

    return result;
}

bool isPartition(string s) {
    if (s.size() == 0) {
        return false;
    }

    if (s.size() == 1) {
        return true;
    }

    if (s.size() == 2) {
        return s[0] == s[s.size()-1];
    }

    return s[0] == s[s.size()-1] && isPartition(s.substr(1, s.size()-2));
}

void partite(string s, int begin, int end, vector<vector<string>>& result, vector<string> part) {
    if (begin > end) {
        result.push_back(part);
        return;
    }

    for (int i = begin; i <= end; i++) {
        string temp = s.substr(begin, i-begin+1);
        if (isPartition(temp)) {
            part.push_back(temp);
            partite(s, i+1, end, result, part);
            part.pop_back();
        }
    }
}