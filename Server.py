import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((socket.gethostbyname(socket.gethostname()), 1028))
print(f'{(socket.gethostbyname(socket.gethostname()))} bind...')
sock.listen(5)

print('Waiting for client...')
connection, address = sock.accept()
print(f'Client {address} connected...')
while True:
    message = connection.recv(1024).decode('utf-8')
    if message == 'finish':
        print('Connection closed...')
        break
    else:
        print(message)

sock.close()
