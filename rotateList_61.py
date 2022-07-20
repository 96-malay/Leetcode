# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return
        dummy = ListNode()
        dummy.next = head
        n = 1
        counter = head
        while counter.next:
            n += 1
            counter = counter.next
        if k % n == 0:
            return dummy.next

        move = n - k % n
        i = 1
        k = head
        while i < move:
            k = k.next
            i += 1

        temp = k.next
        k.next = None  # to mark the end
        dummy.next = temp  # Rotated list
        # Since counter is pointing to the ned of list, adding the list from head
        counter.next = head
        return dummy.next  # represents the rotated list
