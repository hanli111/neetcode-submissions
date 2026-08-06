class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int result = 0;
        int l = 0;
        unordered_set<char> charSet;

        for (int i = 0; i < s.length(); ++i) {
            while (charSet.find(s[i]) != charSet.end()) {
                charSet.erase(s[l]);
                l++;
            }
            charSet.insert(s[i]);
            result = max(result, i - l + 1);
        }

        return result;
    }
};
