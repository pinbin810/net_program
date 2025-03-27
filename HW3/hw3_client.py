import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9002)
sock.connect(addr)

msg = sock.recv(1024)
print(msg.decode())
sock.send("Inbin Park".encode())
print(int.from_bytes(sock.recv(4), 'big'))
sock.close()