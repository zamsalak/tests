import queue
import threading
import time

def putting_thread(q):
    while True:
        print('starting thread')
        time.sleep(10)
        q.put(5)
        print('put something')

q = queue.Queue()
t = threading.Thread(target=putting_thread, args=(q,), daemon=True)
t.start()

q.put(5)
print(q.get())
print('first item gotten')
print(q.get())
print('finished')
