import heapq
from typing import List

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # 1. Sort intervals by their start time
        intervals.sort(key=lambda x: x[0])
        
        minHeap = []
        result = {}
        i = 0

        # 2. Process queries in sorted order to maintain the two-pointer progression
        for q in sorted(queries):
            # Add all intervals that start before or at the query point
            while i < len(intervals) and intervals[i][0] <= q:
                left, right = intervals[i]
                heapq.heappush(minHeap, (right - left + 1, right))
                i += 1

            # Remove intervals from the top of the heap that end before the query point
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)

            # 3. Store the result (peek at the top of the heap, don't pop it!)
            result[q] = minHeap[0][0] if minHeap else -1

        # Return results mapped back to the original queries order
        return [result[q] for q in queries]