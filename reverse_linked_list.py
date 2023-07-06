# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ReverseLinkedList:

    def reverseLinkedLink(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # to simplify, just reverse the lists in O(n) time complexity
        # no next lists created, just new links and a couple vars
        curr = head
        prev = None
        while(curr != None):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        return prev
        # remember the head is now the "end" of the list, so give it
        # prev to get the beginning
        # head = prev
        # return head
        # temp = head
