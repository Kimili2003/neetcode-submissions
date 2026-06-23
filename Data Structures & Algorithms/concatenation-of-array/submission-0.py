class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        newList = [0] * (len(nums)*2)
        for i in range(len(nums)):
            newList[i] = nums[i]
            newList[i+len(nums)] = nums[i]
        return newList