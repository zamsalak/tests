import queue
import threading
import time
import numpy as np

def flag():
    time.sleep(3)
    event.set()
    print('starting countdown')
    time.sleep(7)
    print('event is clear')
    event.clear()

def start_operations():
    event.wait()
    while event.is_set():
        print('starting random integer task')
        x = np.random.randint(1, 30)
        time.sleep(.5)
        if x == 29:
            print('True')
    print('Event has been cleared, random operation stops.')

event = threading.Event()
t1 = threading.Thread(target=flag)
t2 = threading.Thread(target=start_operations)

t1.start()
t2.start()


# event = threading.Event()
# event.set()
# event.clear()
#
# event.wait() #blocks thread from moving forward until the event is set
#
# event.is_set()
