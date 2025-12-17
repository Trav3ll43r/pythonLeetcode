class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head, left, right):
        dummy = ListNode(0, head)
        lp, cur = dummy, head

        for _ in range(left - 1):
            lp = cur
            cur = cur.next

        prev = None
        for _ in range(right - left + 1):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        lp.next.next = cur
        lp.next = prev
        return dummy.next


def to_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    sol = Solution()
    new_head = sol.reverseBetween(head, 2, 4)
    print(to_list(new_head))
