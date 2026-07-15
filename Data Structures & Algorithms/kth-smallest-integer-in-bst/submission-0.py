# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = -1
        self.tro = k
        
        def dfs(root):
            nonlocal ans
            if not root or ans != -1:
                return
            
            dfs(root.left)
            self.tro -= 1
            if self.tro == 0:
                ans = root.val
                return
            dfs(root.right)
            
        dfs(root)
        
        return ans
