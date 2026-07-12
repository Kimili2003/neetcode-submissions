# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ansListl1 = 0
        ansListl2 = 0
        factor1, factor2 = 1,1

        while l1 != None:
            ansListl1+=(l1.val) * factor1            
            l1 = l1.next
            factor1 *= 10

        while l2 != None:
            ansListl2+=(l2.val) * factor2
            l2 = l2.next
            factor2 *= 10
        
        ansListl = str(ansListl1 + ansListl2)
        prev, head = None, None

        for i in range(len(ansListl)-1, -1, -1):
            if prev == None:
                ans = ListNode(ansListl[i])
                ans.next = None
                prev = ans
                head = ans
            else:
                ans = ListNode(ansListl[i])
                prev.next = ans
                prev = ans
        return head

        
        
