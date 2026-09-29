"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals: return 0
        intervals.sort(key=lambda x: x.start)
        rooms = [] # holds end times of every meeting currently running
        for interval in intervals:
            if rooms and rooms[0] <= interval.start:
                heapq.heappop(rooms)
            heapq.heappush(rooms, interval.end)
        return len(rooms)