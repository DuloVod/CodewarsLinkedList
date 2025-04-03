def swap_pairs(head):
    dummy = Node(0)
    dummy.next = head
    prev = dummy
    current = head

    while current and current.next:
        # Nodes to be swapped
        first = current
        second = current.next

        # Swapping
        prev.next = second
        first.next = second.next
        second.next = first

        # Move to the next pair
        prev = first
        current = first.next

    return dummy.next

class Node:
    def __init__(self, next=None):
        self.next = next
