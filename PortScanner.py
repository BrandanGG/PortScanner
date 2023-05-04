from socket import socket, AF_INET, SOCK_STREAM
from queue import Queue
import threading

# Check if the port is open or not
def test_port(host, port):
    with socket(AF_INET, SOCK_STREAM) as sock: # tells the socket what to expect
        sock.settimeout(5)
        # Attempt to connect if connected return true
        try:
            sock.connect((host, port))
            return True
        except ConnectionError:
            return False

# Check if the port is opened or closed
def port_scan(host, ports):
    print(f'Scanning {host}')
    for port in ports:
        if test_port(host, port):
            print(f'[+] {port} is open')
        else:
            print(f'[-] {port} is closed')

host = 'python.org'
port = 100
port_scan(host, range(port))