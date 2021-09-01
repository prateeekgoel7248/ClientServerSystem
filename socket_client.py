import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(('127.0.0.1', 6001))
print("[+] Trying to connect to 127.0.0.1:6001")

while True:

    data = input("Enter data to send:")
    client_socket.send(data.encode())
    print('message sent')

    server_data = client_socket.recv(1024)
    if server_data == '':
        break

    print("[+] Server sent:", server_data.decode())
    if data == 'bye':
        break

client_socket.close()
print("[+] Server disconnected ")

#Made By Prateek Goel