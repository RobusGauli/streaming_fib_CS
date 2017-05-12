from socket import socket, AF_INET, SOCK_STREAM
import time

def fib_gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def send_request(port=9999):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect(('localhost', port))
    #initialte the generator
    gen = fib_gen()
    while True:
        sock.send(str(next(gen)).encode('utf8'))
        time.sleep(0.1)

def main():
    send_request(port=5000)

if __name__ == '__main__':
    main()

