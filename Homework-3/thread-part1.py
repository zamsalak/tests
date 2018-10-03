import threading
import queue
import time



quote = "quote.txt"
q = queue.Queue(290)


def main():
    th_read = threading.Thread(target=read_file, args=(quote,))
    th_convert = threading.Thread(target=convert_upper)

    th_read.start()
    th_convert.start()

    th_read.join()
    th_convert.join()


def read_file(file):
    f = open(file, 'r')
    for i in f.read():
        q.put(i)
    f.close()


def convert_upper():
    h = 0
    while True:
        val = q.get()
        h += 1
        print(val.upper(), end='')
        if h == 290:
            break
    print()


main()

