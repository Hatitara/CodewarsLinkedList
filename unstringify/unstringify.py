'''
Task 2
'''

class Node:
    '''
    Class for nodes.
    '''
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next

def linked_list_from_string(s: str) -> 'Node':
    '''
    unstringifier
    '''
    storage = [int(k) if all(c.isdigit() for c in k) else None \
               for k in s.split(' -> ')]
    bad = [k for k in storage if k is not None and k < 0]
    if storage[0] is None or not storage or bad:
        return None
    res = Node(None)
    current_node = res
    for pos, element in enumerate(storage):
        current_node.data = element
        if pos < len(storage) and storage[pos + 1] is None:
            break
        current_node.next = Node(None)
        current_node = current_node.next
    return res if res.data != 'None' and res.data is not None else 'None'

if __name__ == '__main__':
    x = linked_list_from_string("0 -> 1 -> 4 -> 9 -> 16 -> None")
    y = Node(0, Node(1, Node(4, Node(9, Node(16)))))
    print(x==y)
    print((y:=x.data), type(y))
    print((y:=x.next.data), type(y))
    print((y:=x.next.next.data), type(y))
    print((y:=x.next.next.next), type(y))
