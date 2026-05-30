class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # let me get my idea straight 
        # we have a queue which keeps track of the index.
        # the queue will be placed in a decreasing order so biggest number will always be at the top
        # the first part is that if the new element being added is larger than the last part of the queue, 
        # then it will keep on doing pop. and then in the end append to it. 

        # now we check if the the left pointer range has passed, 





        #KEEP IN MIND WE ARE TRACKING ONLY INDEX IN QUEUE. THAT ALSO IN DESCENDING ORDER.
        output = []
        q = deque()
        left, right = 0, 0

        while right < len(nums):
            #this is remove any element that is smaller than the new element i.e. nums[right]
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            q.append(right)


            if left > q[0]:
                q.popleft()

            if (right+1) >=k:
                output.append(nums[q[0]])
                left+=1
            right +=1

        return output


