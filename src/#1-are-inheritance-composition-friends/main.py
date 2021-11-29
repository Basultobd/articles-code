from queue import LinkedListQueue

'''
Some useul resources to check:

A double linked list implementation very useful
    https://github.com/Kartones/python/blob/master/double-linked-list/linked_list.py

Some good practices when you work with OOP in python
    https://towardsdatascience.com/5-best-practices-for-professional-object-oriented-programming-in-python-20613e08baee
'''


def main():
    list = LinkedListQueue()
    list.enqueue(1)
    list.enqueue(2)
    list.dequeue()
    list.print_list()  # |2 -> {}|
    print(LinkedListQueue.mro())


if __name__ == "__main__":
    main()
