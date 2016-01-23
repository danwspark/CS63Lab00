#! /usr/bin/env python

########################################
# CS63: Artificial Intelligence, Lab 1
# Spring 2016, Swarthmore College
########################################
# full name: WanSeo Park
# username: wpark1
########################################

#TODO: add Python library imports here
from collections import deque
from random import randrange

def test_queues():
    #TODO: Test all three queue implementations.Try adding and removing 
    # several elements in various orders. Also test out printing,
    # containment testing with 'in', and len(). Think about edge-cases.
    # What should happen with an empty queue? What about duplicate entries?

    #raise NotImplementedError("TODO")
    FIFO = FIFO_Queue()
    FIFO.add(1)
    FIFO.add(2)
    print(str(len(FIFO))+" len of fifo")
    print(str(FIFO.get())+": is first get")
    print(str(len(FIFO))+" len of fifo")
    print FIFO
        
    LIFO = LIFO_Queue()
    LIFO.add(3)
    LIFO.add(4)
    LIFO.add(0)
    print(str(len(LIFO))+ " Len of LIFO")
    print(str(LIFO.get()) +": is first get LIFO")
    print(str(len(LIFO))+ " Len of LIFO")
    print LIFO
    
    Rand = Random_Queue()
    Rand.add(5)
    Rand.add(6)
    Rand.add(7)
    Rand.add(8)
    print(str(len(Rand))+ " Len of Rand")
    print(str(Rand.get()) +": is first get Rand")
    print(str(len(Rand))+ " Len of Rand")
    print Rand

    
    
    print("ran")
    


class _Queue(object):
    """Abstract base class for FIFO_Queue, LIFO_QUEUE, and Random_Queue
    A queue supports the following operations:
        - adding items with add()
        - removing and returning items with get()
        - determining the number of items with len()
        - checking containment with 'in'
        - printing
    Child classes are required to store items in the self.contents field, but
    are allowed to use different data structures for self.contents. Child
    classes importantly differ in which item is returned by get().
    """
    def __init__(self):
        self.contents = deque()
        #TODO: if all child classes use the same __init__(), implement it here
        #raise NotImplementedError("TODO???")

    def add(self, item):
        self.contents.append(item)
        """Stores item in the queue."""
        #TODO: if all child classes use the same add(), implement it here
        #raise NotImplementedError("TODO???")

    def get(self):
        #TODO: if all child classes use the same get(), implement it here
        """Removes some item from the queue and returns it."""
        #raise NotImplementedError("TODO???")

    def __len__(self):
        """ 'len(q)' calls this method.
        Passes the len() call to self.contents. This requires that all child
        classes implement contents as a Python type with a valid __len__.
        """
        return len(self.contents)

    def __repr__(self):
        """ 'print q' calls this method.
        Passes the repr() call to self.contents. This requires that all child
        classes implement contents as a Python type with a valid __repr__.
        """
        return repr(self.contents)

    def __contains__(self, item):
        """ 'x in q' calls this method.
        Passes the containment check to self.contents. This requires that all
        child classes implement contents as a Python type with a valid
        __contains__.
        """
        return item in self.contents


class FIFO_Queue(_Queue):
    """First-in-first-out queue implementation, a classic 'queue'.
    The first call to get() returns the item from the first call to add(),
    the second returns the second, and so on.
    """
    def get(self):
        #TODO: if _Queue implements get(), remove this definition
        #otherwise, put your FIFO-specific implementation here
        return self.contents.popleft()
        #raise NotImplementedError("TODO???")


class LIFO_Queue(_Queue):
    """Last-in-first-out queue implementation, also known as a 'stack'.
    The first call to get() returns the item from the most recent call to
    add(), the second returns the next-most-recent, and so on.
    """
    def get(self):
        #TODO: if _Queue implements get(), remove this definition
        #otherwise, put your LIFO-specific implementation here
        return self.contents.pop()
        #raise NotImplementedError("TODO???")


class Random_Queue(_Queue):
    """Randomized queue implementation.
    Each call to get() returns an item from the queue chosen uniformly
    at random.
    """
    def __init__(self):
        self.contents = []
        #TODO: if _Queue implements __init__(), remove this definition
        #otherwise, put your Random-specific implementation here
        
        #raise NotImplementedError("TODO???")

        """
    def add(self, item):
        #TODO: if _Queue implements add(), remove this definition
        #otherwise, put your Random-specific implementation here
        raise NotImplementedError("TODO???")
        """

    def get(self):
        #TODO: if _Queue implements get(), remove this definition
        #otherwise, put your Random-specific implementation here
        return self.contents.pop(randrange(len(self.contents)))
        
       # raise NotImplementedError("TODO???")


if __name__ == "__main__":
    test_queues()
