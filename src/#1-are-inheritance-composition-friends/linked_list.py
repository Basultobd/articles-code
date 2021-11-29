from dataclasses import dataclass
from linked_list_node import LinkedListNode
from typing import Optional


@dataclass
class LinkedList:
    '''
    A class used to represent a linked list

    Attributes
    ----
    head : LinkedListNode
        Pointer to the first node in the list
    tail : LinkedListNode
        Pointer to the last node in the list
    '''

    head: Optional["LinkedListNode"] = None
    tail: Optional["LinkedListNode"] = None

    def append(self, value_to_insert: int) -> None:
        ''' 
        O(1) Insert a new node at list tail

        parameters:
        ----
        value_to_insert: int
            value to be inside of the new appended node
        '''

        new_tail_node = LinkedListNode(data=value_to_insert)
        if self.tail is None:
            # When the list is empty
            self.head = new_tail_node
        else:
            # Make the actual tail points to the new node
            self.tail.next_node = new_tail_node

        # Update list tail
        self.tail = new_tail_node

    def delete(self, value_to_delete: int) -> None:
        '''
        O(n) Delete a node base in its value

        Paramaters 
        ----
        value_to_delete: int
            Value inside of the node to be deleted
        '''
        actual_node = self.head

        # If you try to delete the value in the root LinkedListNode and the list is empty
        if actual_node.data == value_to_delete and not actual_node.next_node:
            raise ValueError(
                'This is not possible. Add one more node to the list')

        # If the value is in the root node we don't iterate
        if actual_node.data == value_to_delete:
            self.head = actual_node.next_node
            return

        # Iterate until we find the node
        previous_node = actual_node
        actual_node = actual_node.next_node
        while actual_node and actual_node.data != value_to_delete:
            previous_node = actual_node
            actual_node = actual_node.next_node

        # There is no node with the value to delete
        if not actual_node:
            raise ValueError(
                'The value: {} is not present in any node.'.format(value_to_delete))

        # Make the connection between previous and the next_node of the deleted node
        previous_node.next_node = actual_node.next_node

    def print_list(self):
        '''
        Iterate over all the list and print each node
        '''
        actual_node = self.head
        while actual_node:
            print(actual_node, end='')
            actual_node = actual_node.next_node
