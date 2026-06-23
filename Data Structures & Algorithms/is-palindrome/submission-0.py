import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = s.translate(str.maketrans("", "", string.punctuation + " ")).lower()
        left = 0
        right = len(cleaned) - 1

        while left < right:
            if cleaned[left] != cleaned[right]:
                return False
            else:
                left += 1
                right -= 1

        return True

