"""
# Extend the Stack to include a method called get_from_stack that searches and returns an element e
# from a stack. Any other element must remain on the stack respecting their order.
# Consider the case in which the element is not found - raise ValueError with proper info Message

# Extend the Queue to include a method called get_from_stack that searches and returns an element e
# from a queue. Any other element must remain in the queue respecting their order.
# Consider the case in which the element is not found - raise ValueError with proper info Message

"""

from stack import Stack
from queue import Queue

if __name__ == "__main__":
    s = Stack()
    q = Queue()
    
    for i in range(50):
        s.push(i)
        q.enqueue(i)
    
    print(s.get_from_stack(40))
    print(q.get_from_queue(40))