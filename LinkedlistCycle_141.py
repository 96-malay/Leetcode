# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow, fast = head, head
#       Slow pointer moves 1 node in each iteration.
#       Fast pointer moves 2 node in each iteration.
#       If slow and fast pointer meets at any node then there's a cycle.
        while fast and slow and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
