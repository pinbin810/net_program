import socket, random

HOST, PORT = 'localhost', 5002

with socket.socket() as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Device2 Server Listening on {PORT}")

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
                    data = f"Heartbeat={random.randint(40, 140)}, Steps={random.randint(2000, 6000)}, Cal={random.randint(1000, 4000)}"
                    conn.sendall(data.encode())