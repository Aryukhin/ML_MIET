import socket
from smtplib import SMTP, SMTP_SSL
username = 'aleksandrarukhin@yandex.ru'
password = 'ikhncblzbukgvfwt'
HOST = '127.0.0.1'
PORT = 50007
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            email = conn.recv(1024).decode('utf-8')
            msg = conn.recv(1024).decode('utf-8')
            if not email and msg:
                break
            try:
                with SMTP_SSL('smtp.yandex.ru:465') as smtp:
                    smtp.set_debuglevel(1)
                    smtp.ehlo(username)
                    smtp.login(username, password)
                    smtp.auth_plain()
                    smtp.sendmail(username, email, msg)
                    smtp.quit()
                    print('The message has been sent')
                    conn.sendall(b'Message sent')
            except:
                conn.sendall(b'error')
                break




