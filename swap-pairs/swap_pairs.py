class Node:
    def __init__(self, next=None):
        self.next = next

def swap_pairs(head):
    if not head or not head.next:
        return head
    prev_node = None
    curr_node = head
    while curr_node and curr_node.next:
        first_node = curr_node
        second_node = curr_node.next
        if prev_node:
            prev_node.next = second_node
        else:
            head = second_node
        first_node.next = second_node.next
        second_node.next = first_node

        prev_node = first_node
        curr_node = first_node.next
    return head
