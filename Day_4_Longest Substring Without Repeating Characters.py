# Given a string s, find the length of the longest substring without repeating characters.

def lengthOfLongestSubstring(self, s: str) -> int:
        m=[]
        l, r, n = 0, 0, len(s)
        maxi=0
        while l<n and r<n:
            if s[r] not in m:
                m.append(s[r])
                r+=1
            else:
                l+=1
                m.pop(0)
            maxi=max(maxi, r-l)
        return maxi
