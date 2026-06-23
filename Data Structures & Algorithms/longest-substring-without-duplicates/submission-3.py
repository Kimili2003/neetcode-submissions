class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        for l in range (len(s)):
            di = set()
            for r in range(l, len(s)):
                if s[r] in di:
                    break
                di.add(s[r])
                maxlen = max(r-l+1, maxlen)
        
        return maxlen
