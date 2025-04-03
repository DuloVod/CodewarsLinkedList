def stringify(node):
    res = []
    while node:
        res.append(str(node.data))
        node = node.next
    res.append('None')
    return ' -> '.join(res)
