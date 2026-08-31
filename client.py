import socket

client=socket.socket()
client.connect(('localhost', 1111))
print("CONNECTED WITH THE SERVER...")

while True:
    cl_msg=input("Client: ")
    client.send(cl_msg.encode('utf-8'))
    if cl_msg.lower()=="exit":
        print("Closing connection...")
        break

    response=client.recv(1024).decode('utf-8')
    print(f"Sever: {response}")
    if not response:
        print("Connection closed by server...")
        break
    if response.lower()=="exit":
        print("Closing connection...")
        break
client.close()