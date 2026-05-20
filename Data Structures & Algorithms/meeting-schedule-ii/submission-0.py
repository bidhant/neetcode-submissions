"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        beginning = sorted([i.start for i in intervals])
        ending = sorted([i.end for i in intervals])

        result, count = 0, 0

        start, end = 0, 0 
        while start < len(intervals):
            if beginning[start] < ending[end]:
                count +=1
                start +=1
            else:
                count -= 1
                end +=1
            result = max(count, result)

        return result       