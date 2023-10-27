# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newList = head
        if newList:
            evenListHead = head.next

            listOddPointer = head
            listEvenPointer = head.next
            counter = 0
            while listOddPointer and listEvenPointer:
                listOddPointer.next = listEvenPointer.next 
                prevOddPointer = listOddPointer
                listOddPointer = listEvenPointer.next

                if listOddPointer:
                    listEvenPointer.next = listOddPointer.next 
                    listEvenPointer = listOddPointer.next
            if listOddPointer:
                listOddPointer.next = evenListHead
            else:
                prevOddPointer.next = evenListHead
            return head 
        else:
            return head
    