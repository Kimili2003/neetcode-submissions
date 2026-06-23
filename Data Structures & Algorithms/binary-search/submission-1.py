class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lef, right = 0, len(nums)-1

        while lef <= right:
            mid = (lef + right) // 2

            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                lef = mid + 1
            else:
                return mid

        return -1