class Solution:
    def candy(self, ratings: List[int]) -> int:
        # TWO PASSES
        arr = [1] * len(ratings)

        # Pass One: Skip first index since there's no left neighbor
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                arr[i] = arr[i - 1] + 1
        
        # Pass Two: Skip last index since there's no right neighbor
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                arr[i] = max(arr[i], arr[i + 1] + 1)
        
        return sum(arr)