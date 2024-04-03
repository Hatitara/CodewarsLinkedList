""" For your information:
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
"""
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def sorted_insert(head, data):
    # Your code goes here.
    # Make sure to return the head of the list.
    if head is None:
        return Node(data)
    if data < head.data:
        result = Node(data)
        result.next = head
        return result
    cur_node = head
    while True:
        previous = cur_node
        cur_node = cur_node.next
        if cur_node is None:
            previous.next = Node(data)
            return head
        if previous.data <= data < cur_node.data:
            inserted = Node(data)
            inserted.next = cur_node
            previous.next = inserted
            return head
