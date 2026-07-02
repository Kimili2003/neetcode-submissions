"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        Amap = {None : None}

        cur = head
        while cur:
            copy = Node(cur.val)
            Amap[cur] = copy
            cur = cur.next

        cur = head
        while cur:
            copy = Amap[cur]
            copy.next = Amap[cur.next]
            copy.random = Amap[cur.random]
            cur = cur.next
        
        return Amap[head]
