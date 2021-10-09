from node import Node


class LinkedList:

    def __init__(self, value):
        self.root = Node(value)

    def add(self, value):
        tmp_node = self.root

        while tmp_node.next:
            tmp_node = tmp_node.next
        tmp_node.next = Node(value)

    def delete(self, value_to_delete):
        actual_node = self.root

        # If you try to delete the value in the root node and the list is empty
        if actual_node.value == value_to_delete and not actual_node.next:
            print('This is not possible. Add one more node to the list')
            return

        # If the value is in the root node we don't iterate
        if actual_node.value == value_to_delete:
            self.root = actual_node.next
            return

        # Iterate until we find the node
        previous_node = actual_node
        actual_node = actual_node.next
        print(actual_node.value)
        while actual_node and actual_node.value != value_to_delete:
            previous_node = actual_node
            actual_node = actual_node.next

        # There is no node with the value to delete
        if not actual_node:
            print('The value: {value} is not present in any node.'.format(
                value=value_to_delete))
            return

        # Make the connection between previous and the next of the deleted node
        previous_node.next = actual_node.next

    # Let's iterate over the nodes using generators!
    def print_list(self):
        actual_node = self.root
        while actual_node:
            print(actual_node, end='')
            actual_node = actual_node.next
