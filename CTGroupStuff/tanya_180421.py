from LinearDSLab import *

def InvertQueue(q):
    s = Stack()
    for i in range(q.count()):
        s.push(q.dequeue())
    for i in range(s.count()):
        q.enqueue(s.pop())
    q.display()



q = Queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
InvertQueue(q)