import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 5000))
server.listen(1)

print("Server menunggu koneksi...")

conn, addr = server.accept()
print("Client terhubung:", addr)

data = conn.recv(1024).decode()
print("Data diterima:", data)

conn.send("Data berhasil diterima server".encode())

conn.close()
server.close()
