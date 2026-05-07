"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start) 

        last_end_time = 0

        for i in intervals: 
            if last_end_time > i.start:
                return False 
            else:
                last_end_time = i.end

        return True

