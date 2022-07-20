# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        odd, even = head, head.next
        evenH = even

        while even != None and even.next:
            print(odd.val)
            odd.next = odd.next.next
            even.next = even.next.next

            even = even.next
            odd = odd.next
        odd.next = evenH

        return head
