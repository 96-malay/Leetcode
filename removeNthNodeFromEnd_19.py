# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # In one Pass
        node = ListNode(0)
        node.next = head
        slow, fast = node, node.next

        # Move fast pointer n times
        for i in range(n):
            fast = fast.next
        # To bring slow pointer at position from where we can remove the nth node
        while fast:
            slow = slow.next
            fast = fast.next
        # Noe slow pointer is just beore the node which we want to remove
        slow.next = slow.next.next

        return node.next

        # In Two Pass
#         l = 1
#         b = head
#         while b:
#             b = b.next
#             l+=1
#         i = 1
#         b = head
#         while i < l - n +1:
#             b = b.next
#             i+=1
#         b.next = b.next.next
#         return head
