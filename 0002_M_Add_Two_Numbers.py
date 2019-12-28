# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)  # 建立ListNode()實例
        result_tail = result
        # result & result_tail 為不同物件，存在不同記憶體空間
        carry = 0
        while l1 or l2 or carry:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            carry, out = divmod(val1 + val2 + carry, 10)
            # divmod(被除數, 除數)= 商數, 餘數

            result_tail.next = ListNode(out)  # result_tail 連接 ListNode(out)
            result_tail = result_tail.next  # 進位

            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)

        return result.next


def createListNode(list):
    i = 0
    result = ListNode(0)
    result_tail = result
    # result & result_tail 為不同物件，存在不同記憶體空間
    while True:
        if i != len(list):
            result_tail.next = ListNode(list[i])
            result_tail = result_tail.next
            i += 1
        else:
            break
    return result.next

c = [2, 4, 3]
d = [5, 6, 4]

lc = createListNode(c)
ld = createListNode(d)
nk = Solution().addTwoNumbers(lc,ld)
nlk = [nk.val, nk.next.val, nk.next.next.val]
print(nlk)

# a = [2, 4, 3]
# b = [5, 6, 4]
#
# l1 = ListNode(2)
# l2 = l1.next = ListNode(4)
# l3 = l2.next = ListNode(3)
#
# l4 = ListNode(5)
# l5 = l4.next = ListNode(6)
# l6 = l5.next = ListNode(4)
#
# k = Solution().addTwoNumbers(l1,l4)
# lk = [k.val, k.next.val, k.next.next.val]
# print(lk)  # [7, 0, 8]