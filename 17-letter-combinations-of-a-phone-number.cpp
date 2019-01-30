class Solution {
public:
    vector<string> letterCombinations(string digits) {
        map<char, string> lookup;
        vector<string> result;

        lookup['2'] = "abc";
        lookup['3'] = "def";
        lookup['4'] = "ghi";
        lookup['5'] = "jkl";
        lookup['6'] = "mno";
        lookup['7'] = "pqrs";
        lookup['8'] = "tuv";
        lookup['9'] = "wxyz";

		for (int i = 0; i < lookup[digits[0]].size(); i++) {
			result.push_back(lookup[digits[0]].substr(i, 1));
		}

        for (int i = 1; i < digits.size(); i++) {
            vector<string> tempResult;
            for (int j = 0; j < lookup[digits[i]].size(); j++) {
                for (int k = 0; k < result.size(); k++) {
                    tempResult.push_back(result[k] + lookup[digits[i]][j]);
                }
            }
            result = tempResult;
        }

		return result;
    }
};