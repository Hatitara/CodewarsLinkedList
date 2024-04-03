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
    current_node = None
    for element in s.split(' -> ')[-2::-1]:
        current_node = Node(data=int(element), next=current_node)
    return current_node

if __name__ == '__main__':
    x = linked_list_from_string("0 -> 1 -> 4 -> 9 -> 16 -> None")
    y = Node(0, Node(1, Node(4, Node(9, Node(16)))))
    print(x==y)
    print((y:=x.data), type(y))
    print((y:=x.next.data), type(y))
    print((y:=x.next.next.data), type(y))
    print((y:=x.next.next.next), type(y))
