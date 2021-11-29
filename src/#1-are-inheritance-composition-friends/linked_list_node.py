from dataclasses import dataclass
from typing import Optional


@dataclass
class LinkedListNode:
    '''
    A class used to represent a linked list node

    Attributes
    ----
    data : int
        Value inside of the node (default 0)
    next_node : LinkedListNode
        Pointer to the next node
    '''

    data: int
    next_node: Optional["LinkedListNode"] = None

    def __post_init__(self) -> None:
        '''
        Run verifications after instance creation

        Raises
        ----
        TypeError
            If the data is not an integer
        '''

        if type(self.data) != int:
            raise TypeError('The value passed is not an interger')

    def __repr__(self) -> str:
        ''' 
        Overrides the repr function implementation provided
        by dataclass
        '''
        return "|{} -> {}|".format(
            str(self.data),
            str(self.next_node.data) if self.next_node else "{}"
        )
