# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse(self, prev, curr, d):
        #         d is the distance between left and right pointers
        #         prev is the node to which the curr node will point
        if d == 0:
            temp = curr.next
            curr.next = prev
            # here we also need to return the next of this last node so that it can be joined back in the end
            return (curr, temp)
        temp = curr.next
        curr.next = prev
        d -= 1
        # after reversing the direction of curr node, we pass curr node as prev for next recurssion
        # in next recurssion, temp will be curr node
        # passing d to track the distance
        return self.reverse(curr, temp, d)

        pass

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right or not head.next:
            return head

        dummy = n = ListNode()
        dummy.next = head
        i = 1

        while i < left:
            n = n.next  # To store the head
            head = head.next
            i += 1

        n.next, last = self.reverse(None, head, right-left)
        while n.next:
            n = n.next
        n.next = last
        return dummy.next
