import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('https://cnn-server.herokuapp.com/', 1028))
print(f'https://cnn-server.herokuapp.com/ -> bind...')
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
