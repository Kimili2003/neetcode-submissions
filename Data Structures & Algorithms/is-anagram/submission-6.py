class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        return sorted(s) == sorted(t)


        tmap = {}
        smap = {}
        for ss in s:
            if ss in smap:
                smap[ss] += 1
            else:
                smap[ss] = 1
        for tt in t:
            if tt in tmap:
                tmap[tt] += 1
            else:
                tmap[tt] = 1
        for sm in smap:
            if (sm not in tmap) or (tmap[sm] != smap[sm]):
                return False
        for tm in tmap:
            if (tm not in smap) or (smap[tm] != tmap[tm]):
                return False
        
        return True
