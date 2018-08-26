import time
import threading

class MyThread(threading.Thread):
    def __init__(self, number, func, args):
        threading.Thread.__init__(self)
        self.number = number
        self.func = func
        self.args = args
        
        
    def run(self):
        print('thread {} has started'.format(self.number))
        self.func(*self.args)
        print('thread {} has finished'.format(self.number))
        
        
def double(number, cycles):
    for i in range(cycles):
        number += number
    print(number)
    
    
threads_list = []

for i in range(50):
    t = MyThread(number = i +1, func = double, 
                 args = [i, 3])
    threads_list.append(t)
    t.start()
    
for t in threads_list:
    t.join()
        
