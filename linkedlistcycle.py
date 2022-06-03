#141. Linked List Cycle
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        aux = set()
        llst=head
        while llst:
            if llst in aux:
                return True
            aux.add(llst)
            llst = llst.next
        return False   
