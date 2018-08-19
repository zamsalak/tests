import time
import threading


def sleeper(n, name):
    print('{}: Sleeping for {} sec. '.format(name, n))
    time.sleep(n)
    print('{}: Sleep ends'.format(name))

t = threading.Thread(target = sleeper,
                     name = 'thread1',
                     args=(5, 'thread1'))
t.start()
t.join()

print('yo')
