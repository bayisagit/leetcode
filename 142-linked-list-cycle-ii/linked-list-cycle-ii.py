# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        slow = head
        fast = head
        nocycle = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                nocycle = True
                break
        if not nocycle:
            return None
        newptr = head
        oldptr = slow
        while newptr != oldptr:
            newptr = newptr.next
            oldptr = oldptr.next
        return newptr

        
        