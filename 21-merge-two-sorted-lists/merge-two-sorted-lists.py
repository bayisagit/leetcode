# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        newtail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                newtail.next = list1
                list1 = list1.next
            else:
                newtail.next = list2
                list2 = list2.next
            newtail = newtail.next
        if list1:
            newtail.next = list1
        if list2:
            newtail.next = list2
        return dummy.next
        