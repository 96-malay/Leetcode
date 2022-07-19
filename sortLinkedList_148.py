# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def split(self, head):
        # Return the middle node
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print('mid', slow.val)
        return slow

    def mergeSort(self, l, r):
        # Sort and merge two lists
        dummy = n = ListNode(0)
        while l and r:
            if l.val < r.val:
                n.next = l
                l = l.next
            else:
                n.next = r
                r = r.next
            n = n.next
        if l:
            n.next = l
        if r:
            n.next = r
        return dummy.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        middle = self.split(head)
        temp = middle.next
        middle.next = None
        # recursively break into left and right sub list
        left = self.sortList(head)
        right = self.sortList(temp)
        # recursively sort and merge the left and right list
        return self.mergeSort(left, right)
