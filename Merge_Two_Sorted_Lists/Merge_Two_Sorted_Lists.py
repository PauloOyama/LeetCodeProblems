class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1: ListNode, list2: ListNode):

        lst = ListNode()
        aux = lst

        while list1 and list2:

            if list1.val < list2.val:
                aux.next = list1
                list1 = list1.next
                aux = aux.next
            else:
                aux.next = list2
                list2 = list2.next
                aux = aux.next

        aux = aux.next

        if list1:
            aux.next = list1
        elif list2:
            aux.next = list2

        return lst


print(Solution().mergeTwoLists([1, 2, 3], [1, 3, 4]))
