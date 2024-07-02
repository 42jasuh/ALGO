# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        arr = []
        n = ListNode()
        firstHead = head
        firstNode = n
        while head:
            arr.append(head.val)
            head = head.next
        length = len(arr)-1
        while length > 0:
            n.val = arr.pop()
            n.next = ListNode()
            n = n.next
            length -= 1
        if arr:
            n.val = arr[0]
        return firstNode
            
        
            
            
            
        