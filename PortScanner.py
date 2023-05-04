import threading
from socket import socket, AF_INET, SOCK_STREAM
import socket
from queue import Queue
import header


header.head()
host = socket.gethostbyname(input("Enter the IP address or domain:"))
queue = Queue()
open_ports = []
closed_ports = []


# Create the inital connection. Connect to an individual port to see if its open or close.
def scanner(port):
    with socket.socket() as sock:  # tells the socket what to expect
        sock.settimeout(5)
        conn = sock.connect_ex((host, port))  # connection to host on port x
        if conn == 0:
            print(f"[+] {port} is open")


# adds the ports into the queue
def test_ports():
    print(f"Scanning ports from 1 - 1024")
    for ports in range(1025):
        queue.put(ports)


# Function utilizing the Queue class
# while the queue isn't empty, scan the port if its open do x if closed do y
def worker():
    while not queue.empty():
        port = queue.get()
        if scanner(port):
            print(f"[+] Port {port} is open")
            open_ports.append(port)
        else:
            print(f"[-] Port {port} is closed")
            closed_ports.append(port)


# This function creates threads and assigns the threading to the worker class
# Calls the function that needs to be threaded
def run():
    test_ports()
    l = []
    for x in range(2000):
        thread = threading.Thread(target=worker())
        l.append(thread)
    for thread in l: # Start threading
        thread.start()
    for thread in l: # add to the list of all threads
        thread.join()

run()