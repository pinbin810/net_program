import socket
import time

SERVERS = {
    "1": ("localhost", 5001),
    "2": ("localhost", 5002)
}

while True:
    cmd = input("1: Device1, 2: Device2, 'quit' 종료 > ").strip()

    if cmd == "1" or cmd == "2":
        host, port = SERVERS[cmd]
        with socket.socket() as s:
            s.connect((host, port))
            s.sendall(b"Request")
            data = s.recv(1024).decode()

        timestamp = time.strftime("%a %b %d %H:%M:%S %Y")

        with open("data.txt", "a") as f:
            f.write(f"{timestamp}: Device{cmd}: {data}\n")

        print(f"Received: {data}")

    elif cmd == "quit":
        for host, port in SERVERS.values():
            with socket.socket() as s:
                s.connect((host, port))
                s.sendall(b"quit")
        break  

    else:  
        pass