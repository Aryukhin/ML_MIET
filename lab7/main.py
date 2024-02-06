import socket

HOST = '127.0.0.1'
PORT = 50007
while True:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            email = f'{input("email: ")}\n'.encode('utf-8')
            msg = input("msg: ").encode('utf-8')
            s.sendall(email)
            s.sendall(msg)
            data = s.recv(1024)
            if data == "OK":
                break
            else:
                continue
    except:
        continue
