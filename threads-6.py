import threading
import time

class MyThread(threading.Thread):
    def __init__(self, number, style, *args, **kwargs):
        super(MyThread, self).__init__(*args, **kwargs)
        self.number = number
        self.style = style
        
        
    def run(self, *args, **kwargs):
        print('thread starting')
        super(MyThread, self).run(*args, **kwargs)
        print('thread has ended')
        
        
        
def sleeper (num, style):
    print('we are sleeping for {} seconds as {}'.format(num, style))
    time.sleep(num)   



t = MyThread(number =3, style = 'yellow', target = sleeper, 
             args = [3, 'yellow']) 

t.start()    
