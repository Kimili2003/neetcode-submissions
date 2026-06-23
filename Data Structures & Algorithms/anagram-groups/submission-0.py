class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mmap = {}

        for ss in strs:
            key = "".join(sorted(ss))

            if key not in mmap:
                mmap[key] = []

            mmap[key].append(ss)

        return list(mmap.values())