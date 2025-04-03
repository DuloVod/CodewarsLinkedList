class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    def _reverse(current, previous):
        if not current:
            return previous
        next_node = current.next
        current.next = previous
        return _reverse(next_node, current)

    return _reverse(head, None)
