'''
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.

Example:
    Input: 1->2->4, 1->3->4
    Output: 1->1->2->3->4->4
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Runtime: 28 ms, faster than 95.18% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Merge Two Sorted Lists.

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_list = self.createNodeList(l1)
        l2_list = self.createNodeList(l2)
        list_ = l1_list + l2_list
        list_.sort()
        return self.createListNode(list_)

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

'''
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:        
        if l1 is None : return l2
        if l2 is None : return l1
        head = tail = ListNode(None)
        
        while l1 and l2:          
            if l1.val >= l2.val:
                tail.next = l2
                l2=l2.next
            else:
                tail.next = l1
                l1=l1.next
            tail = tail.next 
            
        if l1 : tail.next =l1
        if l2 : tail.next =l2
        return (head.next)
'''