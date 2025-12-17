class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):
        oldtonew = {None: None}
        cur = head
        while cur:
            oldtonew[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            copy = oldtonew[cur]
            copy.next = oldtonew[cur.next]
            copy.random = oldtonew[cur.random]
            cur = cur.next
        return oldtonew[head]


def to_list(head):
    res = []
    idx = {}
    cur = head
    i = 0
    while cur:
        idx[cur] = i
        cur = cur.next
        i += 1
    cur = head
    while cur:
        res.append([cur.val, idx[cur.random] if cur.random else None])
        cur = cur.next
    return res


if __name__ == "__main__":
    n1 = Node(7)
    n2 = Node(13)
    n3 = Node(11)
    n4 = Node(10)
    n5 = Node(1)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    n2.random = n1
    n3.random = n5
    n4.random = n3
    n5.random = n1

    sol = Solution()
    copied = sol.copyRandomList(n1)

    print(to_list(n1))
    print(to_list(copied))
