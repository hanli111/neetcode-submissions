import heapq
class MedianFinder:

    def __init__(self):
        self.large, self.small = [], [] # large = min heap, small = max heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)

        # make sure every number in small is <= every number in large
        if self.small and self.large and -1 * self.small[0] > self.large[0]:
            heapq.heappush(self.large, -1 * heapq.heappop(self.small))

        # make sure the difference in size does not exceed 1
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -1 * heapq.heappop(self.small))
        if len(self.large) > len(self.small) + 1:
            heapq.heappush(self.small, -1 * heapq.heappop(self.large))

    def findMedian(self) -> float:
        # check for odd lengths
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (-1 * self.small[0] + self.large[0]) / 2.0