import time
import threading

def sleeper(n, name):
    print('{}: Sleeping for {} sec. '.format(name, n))
    time.sleep(n)
    print('{}: Sleep ends'.format(name))


threads_list = []
start = time.time()
for i in range(25):
    t = threading.Thread(target = sleeper,
                         name = 'thread{}'.format(i),
                         args = (5, 'thread{}'.format(i)))

    threads_list.append(t)
    t.start()
    print('{} has started'.format(t.name))

for t in threads_list:
    t.join()
    
end = time.time() - start

print('Time taken for {} threads to run: {} sec'.format(len(threads_list), end))
print('All done!')
