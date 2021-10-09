from node import Node
from queue import LinkedListQueue


def main():
    list = LinkedListQueue(1)
    list.enqueue(2)
    list.enqueue(3)
    list.print_list()
    # print(LinkedListQueue.mro())


if __name__ == "__main__":
    main()
