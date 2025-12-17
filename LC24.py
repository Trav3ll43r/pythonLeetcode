class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head):
        dummy = ListNode(0, head)
        prev, curr = dummy, head

        while curr and curr.next:
            nextP = curr.next.next
            second = curr.next

            second.next = curr
            curr.next = nextP
            prev.next = second

            prev = curr
            curr = nextP

        return dummy.next


def to_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    sol = Solution()
    new_head = sol.swapPairs(head)
    print(to_list(new_head))
