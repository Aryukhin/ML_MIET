import socket

HOST = '127.0.0.1'
PORT = 50007
while True:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            email = f'{input("email: ")}'.encode('utf-8')
            msg = f'{input("msg: ")}'.encode('utf-8')

            s.sendall(email)
            s.sendall(msg)
            data = s.recv(1024)
            print(repr(data))
            if data != b'Message sent':
                continue
            else:
                break
    except:
        continue
