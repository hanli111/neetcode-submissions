class MedianFinder:

    def __init__(self):
        # small heap = max heap, large heap = min heap
        # since we want max element from the smaller heap and
        # min element from the bigger heap to find median
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush_max(self.small, num)

        # fix the lengths of the 2 heaps if they become uneven
        if len(self.small) > len(self.large) + 1:
            # pop max from small and add to large
            val = heapq.heappop_max(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            # pop min from large and add to small
            val = heapq.heappop(self.large)
            heapq.heappush_max(self.small, val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        # otherwise average the top elements
        return (self.small[0] + self.large[0]) / 2.0