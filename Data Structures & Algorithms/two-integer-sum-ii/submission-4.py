class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numbers.sort()
        right = len(numbers) - 1
        left = 0
        while True:
            if (target - numbers[right]) < numbers[left]:
                right -= 1
            elif (target - numbers[right]) > numbers[left]:
                left += 1
            else:
                return [left+1, right+1]