import socket
import termcolor

def scan(targets, ports):
 for port in range(1, ports):
  scan_port(targets, port)
  

def scan_port(ipadress, port):
 try:
  sock = socket.socket()
  sock.connect((ipadress, port))
  print(f"[+] Port {port} is open")
  sock.close()
 except:
  print(f"[+] Port {port} is closed")
  
targets = input("[*] Enter Target To Scan(split them by ,): ")
ports = int(input("[*] Enter How many Ports You Want To Scan: "))

if "," in targets:
 print(f"[+] Scanning Multiple Targets")
 for ip_addr in targets.split(","):
  scan(ip_addr.strip(" "), int(ports))
else:
 scan(targets, ports)
 


