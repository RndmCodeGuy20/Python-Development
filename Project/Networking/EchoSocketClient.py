import socket

HOST = ""
PORT = 3000
data = ""

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Connection successful!")

while True:
    userInp = str(input("Enter message / data : "))

    if not userInp:
        break

    sock.sendall(userInp.encode())
    data = sock.recv(1024)

    if not data:
        break

    print(f"Message from server : {data.decode('utf-8')}")
