"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return
        q = deque([root])
        while q:
            length, temp = len(q), []
            for i in range(length):
                n = q.popleft()
                temp.append(n)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            i = 0
            while i < len(temp)-1:  # Populating each next pointer to point to its next right node
                temp[i].next = temp[i+1]
                i += 1
            temp[-1].next = None

        return root
