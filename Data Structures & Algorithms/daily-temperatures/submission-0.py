class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stacks = [] #[temp][index]

        for i, j in enumerate(temperatures):
            while stacks and (stacks[-1][1] < j):
                currI, currJ = stacks.pop()
                ans[currI] = i - currI
            stacks.append([i,j])
        return ans