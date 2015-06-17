#Reverse a singly linked list.
#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
# @param {ListNode} head
# @return {ListNode}
def reverseList(self, head):
    Previous = None
    while head:
        current = head
        head = head.next
        current.next = Previous
        Previous = current
    return Previous  

#Given a sorted linked list, delete all duplicates 
def deleteDuplicates(self, head):
    if head == None:
        return head
            
    node = head
    while node.next:
        if node.val == node.next.val:
            node.next = node.next.next
        else:
            node = node.next
    return head        
                

       
        
