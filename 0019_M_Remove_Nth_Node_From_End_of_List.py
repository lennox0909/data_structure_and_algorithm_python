'''
Given a linked list, remove the n-th node from the end of list and return its head.

Example:
    Given linked list: 1->2->3->4->5, and n = 2.
    After removing the second node from the end,
    the linked list becomes 1->2->3->5.

Note:
    Given n will always be valid.

Follow up:
    Could you do this in one pass?
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        list_ = self.createNodeList(head)
        del list_[-n]
        node_ = self.createListNode(list_)
        return node_

    def createListNode(self, list_) -> ListNode:
        i = 0
        result = ListNode(0)
        result_tail = result
        # result & result_tail 為不同物件，存在不同記憶體空間
        while True:
            if i != len(list_):
                result_tail.next = ListNode(list_[i])
                result_tail = result_tail.next
                i += 1
            else:
                break
        return result.next

    def createNodeList(self, node_) -> list:
        node_list = []
        while node_ != None:
            val = node_.val
            node_list.append(val)
            node_ = node_.next
        return node_list


a = [1, 2, 3, 4, 5]  # 1->2->3->4->5  # 54321
Node_a = Solution().createListNode(a)
Node_n = Solution().removeNthFromEnd(Node_a, 3)
list_n = Solution().createNodeList(Node_n)

print(list_n)

