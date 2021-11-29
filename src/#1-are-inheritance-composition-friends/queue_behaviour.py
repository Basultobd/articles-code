import abc
from overrides import EnforceOverrides


class QueueBehaviour(abc.ABC, EnforceOverrides):

    @abc.abstractclassmethod
    def enqueue(self, value):
        '''
        Push a element with the specified value 
        in the first position of the queue (FIFO)

        parameters:
        ----
        value: int
            Value to insert
        '''
        pass

    @abc.abstractclassmethod
    def dequeue():
        '''
        Pop the element in the first position of the queue
        '''
        pass
