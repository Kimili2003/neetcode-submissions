class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for n in nums:
            temp = target - n
            first = nums.index(n)
            if temp in nums:
                second = nums.index(temp)
                if second == first:
                    nums[first] = ""
                    if temp in nums:
                        return [first, nums.index(temp)]
                    else:
                        continue
                else:
                    return [first, nums.index(temp)]