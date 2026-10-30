# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        groupprev = dummy

        while True:
            kth = groupprev

            for _ in range(k):
                kth = kth.next
                
                if kth is None:
                    return dummy.next

                
            groupnext = kth.next

            prev = groupnext
            current = groupprev.next


            while current != groupnext:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node

            tmp = groupprev.next
            groupprev.next = kth
            groupprev = tmp