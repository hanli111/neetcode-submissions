"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # if not intervals:
        #     return 0

        # intervals.sort(key=lambda i: i.start)
        # rooms = []                                  # end times in progress

        # for interval in intervals:
        #     if rooms and rooms[0] <= interval.start:
        #         heapq.heappop(rooms)                # that room freed up
        #     heapq.heappush(rooms, interval.end)

        # return len(rooms)

        if not intervals:
            return 0

        starts = sorted(i.start for i in intervals)
        ends = sorted(i.end for i in intervals)

        rooms = best = 0
        s = e = 0
        while s < len(starts):
            if starts[s] < ends[e]:
                rooms += 1
                best = max(best, rooms)
                s += 1
            else:
                rooms -= 1
                e += 1
        return best