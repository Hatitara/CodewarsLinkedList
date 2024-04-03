'''
Task 1
'''

class Node():
    '''
    Class for nodes.
    '''
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def stringify(node: 'Node') -> str:
    '''
    stringifier
    '''
    storage = []
    next_node = node
    while True:
        if next_node is None:
            storage.append('None')
            break
        storage.append(str(next_node.data))
        next_node = next_node.next
    return ' -> '.join(storage)

if __name__ == '__main__':
    print(stringify(Node(1, Node(2, Node(3)))))
    print(stringify(Node(0, Node(1, Node(4, Node(9, Node(16)))))))
