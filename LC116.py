class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root):
        cur = root
        nxt = root.left if root else None
        while cur and nxt:
            cur.left.next = cur.right
            if cur.next:
                cur.right.next = cur.next.left
            cur = cur.next
            if not cur:
                cur = nxt
                nxt = cur.left
        return root


def level_next(root):
    res = []
    while root:
        cur = root
        row = []
        while cur:
            row.append(cur.val)
            cur = cur.next
        res.append(row)
        root = root.left
    return res


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    sol = Solution()
    sol.connect(root)
    print(level_next(root))
