class Solution {
public:
    int maxProfit(vector<int>& prices) {
        /*int profit = 0;

        for (int i = 0; i < prices.size(); ++i) {
            int buy = prices[i];
            for (int j = i + 1; j < prices.size(); ++j) {
                int sell = prices[j];
                profit = max(profit, sell - buy);
            }
        }

        return profit;*/

        int l = 0;
        int r = 1;
        int maxP = 0;

        while (r < prices.size()) {
            if (prices[l] < prices[r]) {
                int profit = prices[r] - prices[l];
                maxP = max(maxP, profit);
            } else {
                l = r;
            }
            r++;
        }

        return maxP;
    }
};
