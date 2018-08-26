import time
import threading


class MyThread(threading.Thread):
    def run(self):
        print('{} has started!'.format(self.getName()))
        try:
            if self._target:
                self._target(*self._args, **self._kwargs)
        finally:
            del self._target, self._args, self._kwargs
        print('{} has finished!'.format(self.getName()))


def sleeper(n, name):
    print('Hi, I am {}. Going to sleep for 5 seconds\
          \n'.format(name))
    time.sleep(n)
    print('{} has woken up from sleep \n'.format(name))


for i in range(4):
    t = MyThread(target=sleeper,
                 name='thread {}'.format(i + 1),
                 args=(3, 'thread {}'.format(i + 1)))
    t.start()
