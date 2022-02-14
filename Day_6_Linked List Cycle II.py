# Given the head of a linked list, return the node where the cycle begins. 
# If there is no cycle, return null.

def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        found = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                found = True
                break
        if found:
            fast = head
            while fast:
                if slow == fast:
                    return slow
                fast = fast.next
                slow = slow.next
        return None
