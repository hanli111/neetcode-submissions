class Solution {
public:
    int maxArea(vector<int>& heights) {
        /*int result = 0;

        for (int i = 0; i < heights.size(); ++i) {
            for (int j = i + 1; j < heights.size(); ++j) {
                result = max(result, min(heights[i], heights[j]) * (j - i));
            }
        }

        return result;*/

        int result = 0;
        int l = 0;
        int r = heights.size() - 1;

        while (l < r) {
            int area = (r - l) * min(heights[l], heights[r]);
            result = max(result, area);

            if (heights[l] <= heights[r]) {
                l++;
            } else {
                r--;
            }
        }

        return result;
    }
};
