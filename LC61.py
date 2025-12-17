class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head, k):
        if not head:
            return head

        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        k %= length
        if k == 0:
            return head

        cur = head
        for _ in range(length - k - 1):
            cur = cur.next

        new_head = cur.next
        cur.next = None
        tail.next = head
        return new_head


def to_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    sol = Solution()
    new_head = sol.rotateRight(head, 2)
    print(to_list(new_head))
