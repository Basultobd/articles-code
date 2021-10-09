import abc


class QueueBehaviour(abc.ABC):
    @abc.abstractclassmethod
    def enqueue(self, value):
        pass

    @abc.abstractclassmethod
    def dequeue():
        pass
