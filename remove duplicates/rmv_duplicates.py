class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    # Your code goes here.
    # Remember to return the head of the list.
    if head is None:
        return None
    current_node = head
    while current_node.next is not None:
        if current_node.data == current_node.next.data:
            current_node.next = current_node.next.next
        else:
            current_node = current_node.next
    return head
