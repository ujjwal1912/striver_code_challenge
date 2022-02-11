# Given the head of a singly linked list, return true if it is a palindrome.

def isPalindrome(self, head: Optional[ListNode]) -> bool:
  prev = None
  slow = fast = head

  while fast and fast.next:
      fast = fast.next.next
      prev, prev.next, slow = slow, prev, slow.next

  if fast:
      slow = slow.next
  while prev and slow:
      if prev.val!=slow.val:
          return False
      prev = prev.next
      slow = slow.next

  return True
