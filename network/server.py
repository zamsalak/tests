#server.py
import socket
import threading

PORT = 5050

connected = {}

def main():
    try:
        with socket.socket() as serverSock:
            serverSock.bind(('',  PORT))
            serverSock.listen(8)
            print('waiting for connection...')
            while True:
                clientSock, clientAddr = serverSock.accept()
                print('{} connected.'.format(clientAddr))
                thread = threading.Thread(target=threadProc, args=(clientSock, clientAddr))
                thread.start()
    except socket.error as msg:
        print('Socket  error:{}'.format(msg))


def threadProc(clientSock, clientAddr):
    try:
        while True:
            b = clientSock.recv(1000)
            if not b:
                break
            s = b.decode('UTF-8').lower()
            if s == 'quit':
                break
            print('{}: {}'.format(clientAddr, s))
    except socket.error as msg:
        print('{} has left.'.format(clientAddr[0]))
    finally:
        clientSock.shutdown(socket.SHUT_RDWR)
        clientSock.close()


main()

