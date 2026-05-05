class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        
        for i in range(len(intervals)):
            # Case 1: newInterval is strictly before the current interval
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                return result + intervals[i:]
            
            # Case 2: newInterval is strictly after the current interval
            elif newInterval[0] > intervals[i][1]:
                result.append(intervals[i])
            
            # Case 3: Overlap! Merge them into newInterval
            else: 
                newInterval = [
                    min(newInterval[0], intervals[i][0]), 
                    max(newInterval[1], intervals[i][1])
                ]

        # Don't forget to add the last merged interval
        result.append(newInterval)    
        return result