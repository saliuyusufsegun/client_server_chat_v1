import socket

server=socket.socket()
server.bind(('localhost', 1111))
server.listen(1)
print("WAITING ON PORT....")

session, addr=server.accept()
print(f"CONNECTION ESTABLISH WITH {addr}")

while True:
    message=session.recv(1024).decode('utf-8')
    if not message:
        print("Connection closed by client...")
        break
    if message.lower()=="exit":
        print("Closing connection...")
        break
    print(f"Client: {message}")

    response=input("Server: ")
    session.send(response.encode('utf-8'))
    if response.lower()=="exit":
        print("Closing connection....")
        break
session.close()