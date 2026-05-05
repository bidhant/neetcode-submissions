class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #first we sort them
        #handle the edge case 
        #second we then use start,end to update the end or add it into the list or something 

        #sorting 
        intervals.sort()

        output = [intervals[0]]

        for start, end in intervals[1:]: 
            lastend = output[-1][1]
            if start <= lastend: 
                output[-1][1] = max(lastend, end)
            else:
                output.append([start, end])
        return output



