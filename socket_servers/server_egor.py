import sys
import json
import socket
import subprocess
import time

server_socket = socket.socket()

print("Server socket created")

ip = "0.0.0.0"

port = 35491

try:
    server_socket.bind((ip, port))
except ConnectionRefusedError:
    print("ConnectionRefusedError")
    time.sleep(5)
    sys.exit()
    # kill another process
    # subprocess.run(["netstat", "-tulpn","|","grep","{0}:{1}".format(ip,port)])

print("Server socket bound with with ip {} port {}".format(ip, port))

server_socket.listen()

count = 0
data_parts = []


def stop_server(socket_obj: socket):
    print('Server socket close')
    socket_obj.close()
    sys.exit()


while True:
    try:
        client_connection, client_address = server_socket.accept()
        count += 1
        client_connection.settimeout(10)
        print(f"Accepted {count} {client_address} connections so far")
        data = ""
        while data != b'' and data is not None:
            data = client_connection.recv(1024)
            data_parts.append(data.decode())
    except socket.timeout:
        try:
            print(json.loads("".join(data_parts)))
        except ValueError:
            print("error decode json")
            data_parts.clear()
            break
        msg1 = "Hi Client! Read everything you sent".encode()
        msg2 = "Now I will close your connection".encode()
        client_connection.send(msg1)
        client_connection.send(msg2)
        client_connection.close()
        print("Connection closed")
        data_parts.clear()

    except KeyboardInterrupt:
        stop_server(server_socket)
    finally:
        stop_server(server_socket)

stop_server(server_socket)
