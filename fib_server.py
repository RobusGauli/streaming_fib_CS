from socket import socket, AF_INET, SOCK_STREAM

def client_reader(host='localhost', port=8000):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind((host, port))
    sock.listen()

    #we go ahead and accept the connection from the socket
    while True:
        client, addr = sock.accept()
        request = b''
        chunk = client.recv(4096)
        while chunk:
            request += chunk
            chunk = client.recv(4096)
            print(chunk)
        client.send(request)
        client.close()

def main():
    client_reader(port=5000)

if __name__ == '__main__':
    main()
