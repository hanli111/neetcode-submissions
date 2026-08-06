class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        if (strs.size() == 0) { return {}; }

        map<string, vector<string>> m;
        for (const auto &it : strs) {
            string sorted = it;
            sort(sorted.begin(), sorted.end());
            m[sorted].push_back(it);
        }

        vector<vector<string>> answer;
        for (auto &it2 : m) {
            answer.push_back(it2.second);
        }

        return answer;
    }
};
