"""
Note: How to reverse a linked list
"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mid(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow, fast

    def reverse(self, nextN, head):

        if head.next == None:
            head.next = nextN
            return head
        temp = head.next
        head.next = nextN
        return self.reverse(head, temp)

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head.next == None:
            pass
        elif head.next.next == None:
            pass
        else:

            mid, last = self.mid(head)
            print(mid.val)
    # #         reverse the 2nd half
            l2 = self.reverse(None, mid.next)
            mid.next = None
            while l2:
                temp = head.next
                temp1 = l2.next
                head.next = l2
                l2.next = temp
                l2 = temp1
                head = temp
