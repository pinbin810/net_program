from socket import *

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', 5555))
mboxes = {}

while True:
    msg, addr = sock.recvfrom(1024)
    msg = msg.decode().strip()

    if msg == 'quit': break
    if msg.startswith('send '):
        _, mboxID, message = msg.split(' ', 2)
        mboxes.setdefault(mboxID, []).append(message)
        sock.sendto(b'OK', addr)
    elif msg.startswith('receive '):
        mboxID = msg.split()[1]
        res = mboxes.get(mboxID, [])
        sock.sendto((res.pop(0) if res else 'No messages').encode(), addr)
    else:
        sock.sendto(b'Invalid command', addr)

sock.close()