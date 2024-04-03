class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self) -> str:
        return f'{self.data} -> {self.next}'

    def __repr__(self) -> str:
        return f'{self.data} -> {self.next}'


class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __str__(self) -> str:
        return f'f: {self.first}\ns: {self.second}'


def push(head, data):
    newNode = Node(data)
    newNode.next = head
    return newNode


def build_one_two_three():
    head = None
    head = push(head, 3)
    head = push(head, 2)
    head = push(head, 1)
    return head


def build_one_two():
    head = None
    head = push(head, 2)
    head = push(head, 1)
    return head


def build_one_two_three_four_five_six():
    head = None
    head = push(head, 6)
    head = push(head, 5)
    head = push(head, 4)
    head = push(head, 3)
    head = push(head, 2)
    head = push(head, 1)
    return head


def build_list(data):
    data.reverse()
    head = None
    for num in data:
        head = push(head, num)
    return head


def add_in_the_end(node: 'Node', addition: 'Node'):
    if not node:
        return addition
    current_node = node
    while current_node.next is not None:
        current_node = current_node.next
    current_node.next = Node(addition.data)
    return node


def alternating_split(head):
    # Your code goes here.
    # Remember to return the context.
    if not head or not head.next:
        raise AttributeError
    first = head
    second = head.next
    cur_node = head.next.next
    first.next = None
    second.next = None
    status = True
    while cur_node:
        new_node = Node(cur_node.data)
        if status:
            first = add_in_the_end(first, new_node)
        else:
            second = add_in_the_end(second, new_node)
        cur_node = cur_node.next
        status = not status
    return Context(first, second)
