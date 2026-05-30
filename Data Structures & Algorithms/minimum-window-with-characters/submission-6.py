class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        #in this case, countT will always be constant. 
        countT, window = {}, {}
        
        for c in t:
            countT[c] = countT.get(c, 0) + 1
        #the counT is populated with the string in t 

        #in this case, the have count changes and the need_count is always constant
        have_count, need_count = 0, len(countT)

        result, result_length = [-1, -1], float("infinity")
        
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c,0) +1

            #this is to check if window and countT has the same variable or not
            if c in countT and window[c] == countT[c]:
                have_count +=1

            while have_count == need_count: 
                #this is to just check the minimum length
                if (r-l+1) < result_length: 
                    result = [l, r]
                    result_length = (r-l+1)

                #this part is to start starting popping from the left and mainttain the have_count
                window[s[l]] -=1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have_count -=1

                l +=1

        l,r = result
        return s[l:r+1] if result_length != float("infinity") else ''

