from linked_list import LinkedList
from queue_behaviour import QueueBehaviour


class LinkedListQueue(LinkedList, QueueBehaviour):

    def __init__(self, value):
        LinkedList.__init__(self, value)

    # overrides, install overrides
    def enqueue(self, value):
        self.add(value)

    # overrides, install overrides
    def dequeue(self):
        root_value = self.root.value
        self.delete(root_value)
        return root_value
