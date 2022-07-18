# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            slow = head
            history = set()
            while slow:
                if slow in history:
                    return slow
                history.add(slow)
                slow = slow.next
        return
