class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        a = 0
        n = len(nums)

        while a < n - 2:
            
            if nums[a] > 0:
                break

            
            if a > 0 and nums[a] == nums[a - 1]:
                a += 1
                continue

            b = a + 1
            c = n - 1

            while b < c:
                total = nums[a] + nums[b] + nums[c]

                if total == 0:
                    ans.append([nums[a], nums[b], nums[c]])

                    b += 1
                    c -= 1

                    # 跳过重复的 b
                    while b < c and nums[b] == nums[b - 1]:
                        b += 1

                    # 跳过重复的 c
                    while b < c and nums[c] == nums[c + 1]:
                        c -= 1

                elif total < 0:
                    b += 1
                else:
                    c -= 1

            a += 1

        return ans