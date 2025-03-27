from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 9002))

while True:
    msg = input('Input CalForm: ')
    if msg.lower() == 'q':
        break

    s.send(msg.encode())
    print('Result:', s.recv(1024).decode())

s.close()
