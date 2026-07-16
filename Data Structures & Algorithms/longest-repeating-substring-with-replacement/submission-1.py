# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
#         # first we need to move the pointer from the left to right 
#         left, right = 0,0
#         count = {}
#         result = 0
#         while right < len(s):
#             count[s[right]] == 1 + count.get(s[right],0)

#             while (right-left+1) - max(count.values()) > k:
#                 count[s[left]] -=1
#                 left +=1

#             result = max(result, left-right-1)

#         return result



class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        count = {}
        result = 0
        
        while right < len(s):
            # 1. Expand Window: Safely update frequency of incoming character
            count[s[right]] = 1 + count.get(s[right], 0)

            # 2. Shrink Window: While replacement budget is exceeded
            while (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1  # Decrement the OUTGOING left character
                left += 1            # Contract the window
            
            # 3. Capture Results: Use the correct window length formula
            result = max(result, right - left + 1)
            
            # 4. Advance: Manually move the right pointer forward
            right += 1

        return result

                
