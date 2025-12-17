from liststructure import print_list,build_list,ListNode


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dum = ListNode(0)
        current = dum
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            carry, sum_v = divmod(val1 + val2 + carry, 10)

            current.next = ListNode(sum_v)
            current = current.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dum.next

if __name__=="__main__":
    sol=Solution()
    l1= build_list([2,4,3])
    l2= build_list([3,4,5])

    result=sol.addTwoNumbers(l1,l2)
    print_list(result)