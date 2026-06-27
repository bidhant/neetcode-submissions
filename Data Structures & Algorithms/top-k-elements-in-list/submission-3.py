class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        result = [0]*len(nums)

        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i],0)

        bucket = [[] for i in range(len(nums)+1)]

        for key, value in count.items():
            bucket[value].append(key)

        ans = []
        for i in range(len(nums),-1,-1):
            for num in bucket[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans




        