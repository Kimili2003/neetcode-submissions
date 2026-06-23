class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        tmax = 0
        left = -1
        for right in range(0, len(nums)):
            if (nums[right] == 0):
                tmax = max(tmax, right-left-1)
                left = right
        tmax = max(tmax, len(nums)-left-1)
        return tmax