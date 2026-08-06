class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        /*sort(numbers.begin(), numbers.end());

        for (int i = 0; i < numbers.size(); ++i) {
            for (int j = i + 1; j < numbers.size(); ++j) {
                if (numbers[i] + numbers[j] == target) {
                    return {i + 1, j + 1};
                }
            }
        }

        return {};
        */

        int left = 0;
        int right = numbers.size() - 1;

        while (numbers[left] + numbers[right] != target) {
            if (numbers[left] + numbers[right] > target) {
                right--;
            }

            if (numbers[left] + numbers[right] < target) {
                left++;
            }
        }
        return {left + 1, right + 1};
    }
};
