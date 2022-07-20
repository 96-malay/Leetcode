# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = n = ListNode()
        dummy.next = head

        while head and head.next:
            firstnode = head
            secondnode = head.next

            firstnode.next = secondnode.next
            n.next = secondnode
            secondnode.next = firstnode
            head = firstnode.next
            n = secondnode.next
            print('2nd next', secondnode.next.val, n.val)
        return dummy.next
