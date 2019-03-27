#include <stack>
#include <iostream>
using namespace std;

string simplifyPath(string path) {
    stack<string> s;
    string extend = path + '/';
    int i = 0;

    string temp = "";

    for (i = 0; i < path.size(); i++) {
        // std::cout<<i<<" "<<temp<<std::endl;
        if (extend[i] == '/') {
            continue;
        }

        temp = "";
        while (i < path.size() && path[i] != '/') {
            temp += path[i];
            i++;
        }

        if (temp == ".") {
            continue;
        } else if (temp == "..") {
            if (!s.empty()) {
                s.pop();
            }

        } else {
            // std::cout<< i << " " << extend[i]<<std::endl;
            if (temp != "") {
                s.push(temp);
            }
        }
    }

    // std::cout<<i<<std::endl;
    // std::cout<<path[i]<<std::endl;

    string result = "";
    while (!s.empty()) {
        result = "/" + s.top() + result;
        s.pop();
    }

    if (result == "") {
        result = '/';
    }

    return result;
}
