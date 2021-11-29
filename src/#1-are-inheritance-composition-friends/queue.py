from dataclasses import dataclass
from linked_list import LinkedList
from queue_behaviour import QueueBehaviour
from overrides import overrides


@dataclass
class LinkedListQueue(LinkedList, QueueBehaviour):
    '''
    A class used to represent a queue data structure.

    The queue is implemented using a linked lint instead
    of an array. That's why is inheriting from a linked list
    parent class.

    To indicate the class is a queue it's implementing the
    queue behaviour.

    As the class is using @dataclass decorator a constructor is
    not necessary.

    Example:

        def __init__(self):
            LinkedList.__init__(self)
    '''

    @overrides
    def enqueue(self, value):
        '''
        Push a new value at the list tail
        '''
        self.append(value)

    @overrides
    def dequeue(self):
        '''
        Pop the value at the list head
        '''
        head_node_data = self.head.data
        self.delete(head_node_data)
        return head_node_data
