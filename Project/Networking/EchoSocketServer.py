import socket

HOST = ""
PORT = 3000
data = ""

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(1)

conn, addr = sock.accept()
print(f"Client connected : {conn}")

while True:
    data = sock.recv(1024)
    if data == "":
        break
    conn.sendall(data)

conn.close()
