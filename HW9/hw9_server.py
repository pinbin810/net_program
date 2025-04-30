import socket
import select
import time

HOST = ''
PORT = 2500
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_sock.bind((HOST, PORT))
server_sock.listen(5)
print("Server Started")

# 소켓 목록: 서버 소켓 + 클라이언트 소켓들
socket_list = [server_sock]

while True:
    read_sockets, _, _ = select.select(socket_list, [], [])

    for sock in read_sockets:
        # 새 클라이언트 연결
        if sock == server_sock:
            client_sock, addr = server_sock.accept()
            socket_list.append(client_sock)
            print(f"New client {addr}")
        else:
            try:
                data = sock.recv(1024)
                if not data:
                    raise ConnectionResetError  # 클라이언트가 강제 종료한 경우

                msg = data.decode().strip()
                if 'quit' in msg.lower():
                    print(f"{time.asctime()}{sock.getpeername()} exited")
                    socket_list.remove(sock)
                    sock.close()
                    continue

                print(f"{time.asctime()}{sock.getpeername()}:{msg}")
                # 다른 모든 클라이언트에게 전송
                for client in socket_list:
                    if client != server_sock and client != sock:
                        client.sendall(data)
            except:
                print(f"{time.asctime()}{sock.getpeername()} disconnected unexpectedly")
                socket_list.remove(sock)
                sock.close()