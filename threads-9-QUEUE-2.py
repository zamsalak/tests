import queue
import threading
import time

q = queue.Queue()

for i in range(5):
    q.put(i)

while not q.empty():
    print(q.get(), end = ' ')

print()
##### Lifo
q = queue.LifoQueue()

for i in range(5):
    q.put(i)

while not q.empty():
    print(q.get(), end = ' ')

print()
##### Priority

q = queue.PriorityQueue()
q.put(1)
q.put(2)
q.put(4)
q.put(3)

for i in range(q.qsize()):
    print(q.get())
