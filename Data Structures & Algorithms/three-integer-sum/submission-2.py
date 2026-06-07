class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result = [] 

        for i, num in enumerate(nums):
            #this gives in 0,-4  1,-1  2, 1
            if num > 0:
                break 

            #this is to avoid the loop
            if i >0 and num == nums[i-1]:
                continue

            left, right = i+1, len(nums)-1

            while left < right: 
                if num + nums[left] + nums[right] == 0:
                    result.append([num, nums[left], nums[right]])
                    #this is here just to check for the other poosibilities.
                    left +=1
                    while left<right and nums[left] == nums[left-1]:
                        left +=1
                elif num + nums[left] + nums[right] < 0:
                    left +=1

                else:
                    right -=1
        return result

            



        