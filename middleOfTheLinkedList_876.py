# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        #       Basic Approach
        #         count = 1
        #         temp = head
        #         while head.next != None:
        #             count+=1
        #             head = head.next

        #         count //= 2
        #         while count >0:
        #             temp = temp.next
        #             count-=1
        #         return temp

        #     Fast & slow Pointer method
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
