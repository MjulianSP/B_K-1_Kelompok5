import os

r, w = os.pipe()

pesan = "Data offline mahasiswa"

os.write(w, pesan.encode())
os.close(w)

data = os.read(r, 1024).decode()
os.close(r)

print("Data diterima melalui pipe:", data)
