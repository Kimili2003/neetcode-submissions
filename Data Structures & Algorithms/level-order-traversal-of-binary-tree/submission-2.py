# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        ans = []
        anss= []

        if root:
            queue.append(root)
        
        

        while(len(queue)):
                    
            anss = []
            for i in range (len(queue)):

                curr = queue.popleft()
                anss.append(curr.val)
                
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            
            if (anss != []):
                ans.append(anss)
                
                
                

        return ans

            
        