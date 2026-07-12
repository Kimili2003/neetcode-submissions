class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        machine = {}
        seen = {}
        l, r = 0, 0
        for s in s1:
            if s in machine:
                machine[s] += 1
            else:
                machine[s] = 1
        
        for r in range(len(s2)):
            char = s2[r]
            if char in seen:
                seen[char] += 1
            else:
                seen[char] = 1
            
            if r >= len(s1):
                left_char = s2[l]
                if seen[left_char] == 1:
                    seen.pop(left_char)
                else:
                    seen[left_char] -= 1
                l += 1
                
            if seen == machine:
                return True
        
        return False
