import threading
import queue
import time
import random

def main():
    th1 = threading.Thread(target=ranger, args=(1, 1000), )
    th2 = threading.Thread(target=ranger, args=(1000, 2000))
    th3 = threading.Thread(target=ranger, args=(2000, 3000))
    th4 = threading.Thread(target=ranger, args=(3000, 4000))
    th5 = threading.Thread(target=ranger, args=(4000, 5000))
    th6 = threading.Thread(target=ranger, args=(5000, 6000))
    th7 = threading.Thread(target=ranger, args=(6000, 7000))
    th8 = threading.Thread(target=ranger, args=(7000, 8000))
    th9 = threading.Thread(target=ranger, args=(8000, 9000))
    th10 = threading.Thread(target=ranger, args=(9000, 10000))

    threads = [th1, th2, th3, th4, th5, th6, th7, th8, th9, th10]

    #daemon
    for i in range(11, 21):
        thread = threading.Thread(target=put_primes)
        threads.append(thread)
    # daemon
    for i in range(22, 25):
        thread = threading.Thread(target=print_primes)
        threads.append(thread)
    #prime & print_primes set daemon
    for th in threads[11:]:
        th.daemon = True

    for th in threads:
        th.start()
    #main join
    for th in threads[:11]:
        th.join()
#-------------------------------------------------------------------------------------
q_randoms = queue.Queue()
q_primes = queue.Queue()
#-------------------------------------------------------------------------------------
def ranger(x, y):
    st = time.time()
    while True:
        q_randoms.put(random.randint(x, y))
        end = time.time()
        if end - st > 3:
            break
#-------------------------------------------------------------------------------------
def put_primes():
    while not q_randoms.empty():
        num = q_randoms.get()
        if test_prime(num):
            q_primes.put(num)
#-------------------------------------------------------------------------------------
def test_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for x in range(2,n):
            if n % x == 0:
                return False
        return True
#-------------------------------------------------------------------------------------
def print_primes():
    time.sleep(3) #mecburen bunu eklemek zorunda kaldım. Yoksa q_primes'ın boş olduğu bir duruma denk gelirse
    while not q_primes.empty():
        val = q_primes.get()
        print(val, end=' ')
#-------------------------------------------------------------------------------------
main()


