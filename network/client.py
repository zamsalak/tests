#client.py
import socket


PORT = 5050


def main():
    try:
        with socket.socket() as clientSock:
            clientSock.connect(('192.168.1.37',  PORT))
            print('connected...')
            while True:

                s = input('Yazı giriniz:')
                if s == '':
                    pass
                elif s.isspace():
                    pass
                else:
                    b = s.encode('UTF-8')
                    clientSock.send(b)
                if s == 'quit':
                    break
            clientSock.shutdown(socket.SHUT_RDWR)
    except socket.error as msg:
        print('Socket error:{}'.format(msg))
    except KeyboardInterrupt:
        print('Terminated.')


main()

