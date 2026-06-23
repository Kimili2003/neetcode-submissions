class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mmap = {}
        ans = []
        for n in nums:
            if n in mmap:
                mmap[n] += 1
            else:
                mmap[n] = 1
        for i in range(k):
            curr = 0
            currN = None
            for n in mmap:
                if mmap[n] > curr:
                    curr = mmap[n]
                    currN = n
            ans.append(currN)
            mmap[currN] = 0

        return ans