"""
Client that sends the file (uploads)
"""
import socket
import tqdm
import os
import argparse

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 1024 * 4 

def send_file(filename, host, port):
    filesize = os.path.getsize(filename)
    s = socket.socket()
    print(f"[+] Connecting to {host}:{port}")
    s.connect((host, port))
    print("[+] Connected.")

    s.send(f"{filename}{SEPARATOR}{filesize}".encode())

    progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "rb") as f:
        for _ in progress:
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                break
            s.sendall(bytes_read)
            progress.update(len(bytes_read))

    s.close()

if __name__ == "__main__":
    filename = "../files_to_upload/LVL5-GREIFER.mp4"
    host = '192.168.0.114'
    port = 5001
    send_file(filename, host, port)