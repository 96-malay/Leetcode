# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Short and readable code
        # Time: O(l1+l2)
        node = n = ListNode(-1)
        carry = 0
        while l1 or l2 or carry:
            v1, v2 = 0, 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, rem = divmod(v1+v2+carry, 10)
            n.next = ListNode(rem)
            n = n.next
        return node.next


#       Works good
#         ans = ListNode()
#         prev = ans
#         carry,rem = 0,0
#         def cal(v1,v2):
#             nonlocal carry , rem , prev
#             total = v1 + v2 + carry
#             if total > 9:
#                 carry = total // 10
#                 rem = total % 10
#             else:
#                 rem = total
#                 carry = 0
#             tmp = ListNode(val=rem)
#             prev.next = tmp
#             prev = prev.next

#         while l1 and l2:
#             cal(l1.val,l2.val)
#             l1 = l1.next
#             l2=l2.next
#         while l1:
#             cal(l1.val,0)
#             l1 = l1.next
#         while l2:
#             cal(l2.val,0)
#             l2 = l2.next
#         print(carry)
#         if carry != 0:
#             tmp = ListNode(val=carry)
#             prev.next = tmp
#         return ans.next
