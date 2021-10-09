class Node:
    '''
        Node

    '''

    def __init__(self, value=0):
        self.value = value
        self.next = None

    def __str__(self):
        if not self.next:
            return '| ' + str(self.value) + ' | none |'

        return '| ' + str(self.value) + ' | next -> |'
