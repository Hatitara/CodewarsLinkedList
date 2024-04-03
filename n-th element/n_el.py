'''
n-th element
'''

class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def get_nth(node, index):
    if isinstance(node, Node) and isinstance(index, (int, float)) and index >= 0:
        cur_node = node
        for k in range(index):
            if cur_node.next is None:
                raise ValueError
            cur_node = cur_node.next
        return cur_node
    raise ValueError
