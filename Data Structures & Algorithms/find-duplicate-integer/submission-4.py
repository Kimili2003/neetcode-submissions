class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # machine = set()
        # for i in nums:
        #     if i in machine:
        #         return i
        #     else:
        #         machine.add(i)
        
        # return -1

        nums.sort()
        record = 0
        for i in nums:
            if i != record:
                record = i
            else:
                return i
            