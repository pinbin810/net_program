import socket, random

HOST, PORT = 'localhost', 5001

with socket.socket() as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Device1 Server Listening on {PORT}")

    while True:
        conn, _ = s.accept()
        with conn:
            while True:
                msg = conn.recv(1024).decode()
                if not msg:
                    break
                if msg == "quit":
                    s.close()
                    exit(0)
                if msg == "Request":
                    data = f"Temp={random.randint(0, 40)}, Humid={random.randint(0, 100)}, Iilum={random.randint(70, 150)}"
                    conn.sendall(data.encode())