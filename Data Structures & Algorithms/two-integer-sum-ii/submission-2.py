class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        result = []

        while left < right: 
            if numbers[left] + numbers[right] == target:
                result = [left+1, right+1]

            if numbers[left]+numbers[right] > target:
                right -=1
            
            else:
                left +=1

        return result
                

        