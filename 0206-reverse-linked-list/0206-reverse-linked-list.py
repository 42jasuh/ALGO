# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        while current:
            next_node = current.next  # 다음 노드를 저장
            current.next = prev  # 현재 노드의 next를 이전 노드로 변경
            prev = current  # 이전 노드를 현재 노드로 변경
            current = next_node  # 현재 노드를 다음 노드로 변경
        return prev
            
        
            
            
            
        