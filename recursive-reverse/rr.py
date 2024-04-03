class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    # your code goes here.
    def nested(current_node, previous=None):
        if current_node is None:
            return previous
        next_node = current_node.next
        current_node.next = previous
        return nested(next_node, current_node)

    head_copy = head
    return nested(head_copy)
