def mergeTwoLists(list1, list2):
    res = []
    p1, p2 = 0, 0

    # Loop until we reach the end of either list
    while p1 < len(list1) and p2 < len(list2):
        if list1[p1] == list2[p2]:
            res.append(list1[p1])
            res.append(list2[p2])
            p1 += 1
            p2 += 1
        elif list1[p1] < list2[p2]:
            res.append(list1[p1])
            p1 += 1
        else:
            res.append(list2[p2])
            p2 += 1

    # Append any remaining elements from list1
    while p1 < len(list1):
        res.append(list1[p1])
        p1 += 1

    # Append any remaining elements from list2
    while p2 < len(list2):
        res.append(list2[p2])
        p2 += 1

    return res

list1 = [1,2,4,4]
list2 = [1,3,5,9]

print(mergeTwoLists(list1, list2))

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        node.next = list1 or list2

        return dummy.next