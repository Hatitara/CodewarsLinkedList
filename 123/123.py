'''
Node is defined in preloaded like this:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def push(head, data):
    # Your code goes here.
    new = Node(data)
    new.next = head
    return new

def build_one_two_three():
    # Your code goes here.
    new = None
    new = push(new,3)
    new = new = push(new,2)
    new = push(new,1)
    return new
