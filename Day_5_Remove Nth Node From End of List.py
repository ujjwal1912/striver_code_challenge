# Given the head of a linked list, remove the nth node from the end of the list and return its head.

def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
  l = 0
  curr = head
  while curr:
      l+=1
      curr = curr.next
  rem = l-n-1
  curr = head
  if rem>=0:
      fi = curr
  else:
      fi = curr.next
  while curr:
      if rem<=0:
          if curr.next:
              curr.next = curr.next.next
          else:
              curr.next = None
          rem=99999
      else:
          rem-=1
          # print(curr)
          curr = curr.next
  return fi
