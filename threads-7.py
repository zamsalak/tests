import threading

x = 0
COUNT = 100000
lock = threading.Lock()

def add_2():
    global x
    with lock:
        for i in range(COUNT):
            x += 2

def add_5():
    global x
    with lock:
        for i in range(COUNT):
            x += 5

def sub_3():
    global x
    with lock:
        for i in range(COUNT):
            x -= 3

def sub_4():
    global x
    with lock:
        for i in range(COUNT):
            x -= 4

for i in range(100):
    t1 = threading.Thread(target=add_2)
    t2 = threading.Thread(target=add_5)
    t3 = threading.Thread(target=sub_3)
    t4 = threading.Thread(target=sub_4)

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()


    print(x)
