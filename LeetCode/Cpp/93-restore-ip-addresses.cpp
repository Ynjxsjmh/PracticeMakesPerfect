vector<string> restoreIpAddresses(string s) {
    vector<string> result;

    split(s, 0, result, "", 0);

    return result;
}

void split(string s, int begin, vector<string>& result, string part, int count) {
    // count 用来表示是ip的第几部分，如果是最后一个部分，不用加 .
    if (count > 4) {
        // 避免超时
        return;
    }

    if (begin == s.size() && count == 4) {
        result.push_back(part);
        return;
    }

    for (int i = 1; i <= 3; i++) {
        if (begin+i > s.size()) {
            break;
        }

        // std::cout<<"begin="<<begin<<" "<<"i="<<i<<std::endl;
        string sub = s.substr(begin, i);  // [begin, begin+i)

        if((sub[0] == '0' && sub.size() > 1) || (i == 3 && stoi(sub) >= 256)) {
            // 不是合法 ip 范围（0~255）
            // 1. 开头为0，但不是0
            // 2. 比255大
            continue;
        }

        split(s, begin+i, result, part+sub+(count==3?"":"."), count+1);
    }
}