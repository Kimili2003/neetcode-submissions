# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        curr = root
        store = []
        ans = []

        while store or curr:
            if curr:
                ans.append(curr.val)
                if curr.right:
                    store.append(curr.right)
                curr = curr.left
            else:
                curr = store.pop()
        
        return ans