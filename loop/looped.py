class Node:
    def __init__(self) -> None:
        self.next = None

def loop_size(node):
    slow = fast = node
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            count = 1
            slow = slow.next
            while slow is not fast:
                slow = slow.next
                count += 1
            return count
    return 0
