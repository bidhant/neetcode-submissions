class Solution:
    def trap(self, heights: List[int]) -> int:
        
        if not heights:
            return 0

        left, right = 0, len(heights)-1
        leftMax, rightMax = heights[left], heights[right]
        result = 0


        while left < right: 
            if leftMax < rightMax: 
                left +=1
                leftMax = max(leftMax, heights[left])
                result += leftMax - heights[left]

            else:
                right -=1
                rightMax = max(rightMax, heights[right])
                result += rightMax -heights[right]

        return result
