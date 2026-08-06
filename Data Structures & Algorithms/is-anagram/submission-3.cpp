class Solution {
public:
    bool isAnagram(string s, string t) {
        /*if (s.length() != t.length()) { return false; }

        sort(s.begin(), s.end());
        sort(t.begin(), t.end());

        return s == t;*/

        if (s.length() != t.length()) { return false; }
        
        map<char, int> countS;
        map<char, int> countT;

        for (int i = 0; i < s.length(); ++i) {
            ++countS[s[i]];
            ++countT[t[i]];
        }

        return countS == countT;
    }
};
