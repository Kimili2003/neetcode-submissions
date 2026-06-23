class Solution:
    def maxArea(self, heights: List[int]) -> int:

        currentWaterMax = 0

        for right in range(len(heights) - 1, 0, -1):
            left = 0
            continerLength = right - left
            while left < right:
                ava = min(heights[right], heights[left])
                currentWaterMax = max(ava * continerLength, currentWaterMax)
                left += 1
                continerLength -= 1

        return currentWaterMax
        