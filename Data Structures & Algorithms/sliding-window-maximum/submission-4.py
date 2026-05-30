class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # let me get my idea straight 
        # we have a queue which keeps track of the index.
        # the queue will be placed in a decreasing order so biggest number will always be at the top
        # the first part is that if the new element being added is larger than the last part of the queue, 
        # then it will keep on doing pop. and then in the end append to it. 

        # now we check if the the left pointer range has passed, 





        output = []
        q = deque()  # This will store INDEXES, maintaining a decreasing order of values
        left = right = 0

        while right < len(nums):
            # FIX: We must look up the value using the index -> nums[q[-1]]
            # If the new number is larger than the numbers at the back of the queue,
            # those smaller numbers can never be the maximum. We pop them out.
            while q and nums[q[-1]] < nums[right]:
                q.pop()

            # Safely add the current element's index to the back of the queue
            q.append(right)

            # "TOO OLD" RULE: Check if the maximum element (at the front of the queue)
            # has fallen out of the left boundary of our sliding window.
            if left > q[0]:
                q.popleft()  # Evict it from the front

            # "TAKE A PICTURE" RULE: Once our window reaches size k,
            # the maximum value is always at nums[q[0]]. Record it and slide left.
            if (right + 1) >= k:
                output.append(nums[q[0]])
                left += 1  # Shrink the left side to prepare for the next window

            # Always move the right pointer forward to expand the window
            right += 1

        return output


