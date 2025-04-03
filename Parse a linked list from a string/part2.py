class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


def linked_list_from_string(s):
    if s == "null":
        return None

    elements = s.split(" -> ")

    values = [int(x) for x in elements[:-1]]

    if not values:
        return None

    head = Node(values[0])
    current = head

    for value in values[1:]:
        current.next = Node(value)
        current = current.next

    return head