import socket
import threading
import time

HOST = '127.0.0.1'
PORT = 65432

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print("[SERVER] Waiting for connection...")
    conn, addr = server_socket.accept()
    print(f"[SERVER] Connected by {addr}")

    data = conn.recv(1024)
    print("[SERVER] Received:", data.decode())
    conn.sendall(b'Hello from server!')

    conn.close()
    server_socket.close()
    print("[SERVER] Closed connection.")

def start_client():
    time.sleep(1)  # מוודא שהשרת התחיל לפני הלקוח
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    client_socket.sendall(b'Hello from client!')
    data = client_socket.recv(1024)

    print("[CLIENT] Received:", data.decode())

    client_socket.close()
    print("[CLIENT] Closed connection.")

# הרצת השרת והלקוח בתזמון מקביל
server_thread = threading.Thread(target=start_server)
client_thread = threading.Thread(target=start_client)

server_thread.start()
client_thread.start()

server_thread.join()
client_thread.join()

print("✅ תקשורת הושלמה.")
