# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. 
# If the two linked lists have no intersection at all, return null.

def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
  if headA is None or headB is None:
      return None
  pa = headA
  pb = headB
  while pa is not pb:
      pa = headB if pa is None else pa.next
      pb = headA if pb is None else pb.next
  return pa
