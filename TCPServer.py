import socket

HOST = ''
PORT = 1234
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket created")
s.bind((HOST, PORT))
print("Socket bind complete")
s.listen(10)
print("Socket now listening")

conn,addr = s.accept()
s.setblocking(0)

print("Connected with " + addr[0] + ":" + str(addr[1]))

data = conn.recv(1024)
print(data)
conn.sendall(data)
print('end test')
conn.close()
s.close()


