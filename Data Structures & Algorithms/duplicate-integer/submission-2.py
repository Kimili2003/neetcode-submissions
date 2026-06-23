class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        amap = {}
        for num in nums:
            if num in amap:
                return True
            else:
                amap[num] = 1

        return False
