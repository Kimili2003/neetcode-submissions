class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r

        while l <= r:
            spent = 0
            mid = (l+r) // 2
            for ba in piles:    
                spent += math.ceil(ba/mid)
                if(spent > h):
                    l = mid+1
                    continue
            if(spent <= h):
                res = min (res, mid)
                r = mid - 1
                

        
        return res

