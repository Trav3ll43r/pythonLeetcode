class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head, x):
        left = ListNode()
        right = ListNode()
        ltail = left
        rtail = right

        while head:
            if head.val < x:
                ltail.next = head
                ltail = ltail.next
            else:
                rtail.next = head
                rtail = rtail.next
            head = head.next

        ltail.next = right.next
        rtail.next = None
        return left.next


def to_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res


if __name__ == "__main__":
    head = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))
    sol = Solution()
    new_head = sol.partition(head, 3)
    print(to_list(new_head))
