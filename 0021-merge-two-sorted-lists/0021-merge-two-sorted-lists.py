# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        firstNode = None

        if list1 and list2 and list1.val <= list2.val:
            firstNode = list1
            list1 = list1.next
        elif list1 and list2 and list1.val > list2.val:
            firstNode = list2
            list2 = list2.next
        elif list1 and not list2:
            firstNode = list1
            list1 = list1.next
        elif not list1 and list2:
            firstNode = list2
            list2 = list2.next
        
        currentNode = firstNode

        while list1 or list2:
            if list1 and list2 and list1.val <= list2.val:
                currentNode.next = list1
                list1 = list1.next
            elif list1 and list2 and list1.val > list2.val:
                currentNode.next = list2
                list2 = list2.next
            elif list1 and not list2:
                currentNode.next = list1
                list1 = list1.next
            elif not list1 and list2:
                currentNode.next = list2
                list2 = list2.next
            currentNode = currentNode.next
        return firstNode
