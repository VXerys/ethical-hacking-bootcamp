# 📚 **Different Nmap Scan Types**

---

## **Overview**
In this episode, we explore various types of scans that can be performed using **Nmap**, a powerful network scanning tool. Understanding the differences between these scan types is crucial for effective penetration testing. We will cover the most common scan types, including TCP SYN scan, TCP connect scan, and UDP scan, and discuss their use cases and limitations.

---

## **Introduction to Nmap Scan Types**

#### **Why Different Scan Types?**
- **Similar Results:** Many scan types yield similar results, but they differ in how they interact with the target.
- **Context Matters:** The choice of scan type depends on the target, network conditions, and desired outcome.

#### **Mastering Nmap**
- **Key Tip:** The best way to master Nmap is by reading its **manual** (`man nmap`) rather than relying solely on the help menu [[1]].

---

## **TCP SYN Scan (-sS)**

### **Command**
```bash
sudo nmap -sS <target>
```

### **How It Works**
- **Partial Connection:** Sends only the first part of the TCP three-way handshake (SYN packet).
- **Responses:**
  - **SYN-ACK:** Indicates the port is open.
  - **RST:** Indicates the port is closed.
  - **No Response:** Indicates the port is filtered (firewall protection).
- **Advantages:**
  - **Speed:** Scans thousands of ports per second.
  - **Low Noise:** Minimal trace on the target machine.
- **Disadvantages:**
  - **Requires Root Privileges:** Needs elevated permissions to send raw packets.

### **Example Output**
```plaintext
Starting Nmap 7.91 ( https://nmap.org ) at 2025-02-03 12:00 UTC
Nmap scan report for 192.168.1.6
Host is up (0.0002s latency).
Not shown: 977 closed ports
PORT   STATE SERVICE
21/tcp open  ftp
22/tcp open  ssh
80/tcp open  http
```

---

## **TCP Connect Scan (-sT)**

### **Command**
```bash
nmap -sT <target>
```

### **How It Works**
- **Full Connection:** Performs a complete TCP three-way handshake.
- **Responses:**
  - **SYN-ACK:** Indicates the port is open.
  - **RST:** Indicates the port is closed.
- **Advantages:**
  - **No Root Privileges Needed:** Does not require elevated permissions.
- **Disadvantages:**
  - **High Noise:** Leaves a noticeable trace on the target machine.
  - **Slower:** Takes longer to complete compared to SYN scan.

### **Example Output**
```plaintext
Starting Nmap 7.91 ( https://nmap.org ) at 2025-02-03 12:05 UTC
Nmap scan report for 192.168.1.6
Host is up (0.0002s latency).
Not shown: 977 closed ports
PORT   STATE SERVICE
21/tcp open  ftp
22/tcp open  ssh
80/tcp open  http
```

---

## **UDP Scan (-sU)**

### **Command**
```bash
sudo nmap -sU <target>
```

### **How It Works**
- **UDP Packets:** Sends UDP packets to discover open UDP ports.
- **Responses:**
  - **ICMP Echo Reply:** Indicates the port is open.
  - **ICMP Port Unreachable:** Indicates the port is closed.
  - **No Response:** Indicates the port is filtered.
- **Advantages:**
  - **Detects UDP Services:** Useful for identifying UDP-based services.
- **Disadvantages:**
  - **Slower:** Takes significantly longer to complete.
  - **Less Common:** Many services use TCP, making UDP scans less frequent.

### **Example Output**
```plaintext
Starting Nmap 7.91 ( https://nmap.org ) at 2025-02-03 12:10 UTC
Nmap scan report for 192.168.1.6
Host is up (0.0002s latency).
Not shown: 16384 filtered ports
PORT    STATE SERVICE
53/udp  open  domain
67/udp  open  bootps
68/udp  open  dhcps
111/udp open  rpcbind
123/udp open  ntp
161/udp open  snmp
```

---

## **Other Nmap Scan Types**

### **TCP ACK Scan (-sA)**
- **Purpose:** Determines if a firewall is stateful.
- **Command:**
  ```bash
  nmap -sA <target>
  ```

### **TCP Window Scan (-sW)**
- **Purpose:** Identifies open ports by examining the TCP window size.
- **Command:**
  ```bash
  nmap -sW <target>
  ```

### **Idle Scan (-sI)**
- **Purpose:** Uses a zombie host to scan the target.
- **Command:**
  ```bash
  nmap -sI <zombie> <target>
  ```

### **IP Protocol Scan (-sO)**
- **Purpose:** Scans for open IP protocols.
- **Command:**
  ```bash
  nmap -sO <target>
  ```

### **FTP Relay Host (-sF)**
- **Purpose:** Uses FTP bounce to scan the target.
- **Command:**
  ```bash
  nmap -sF <target>
  ```

### **FTP Bounce Scan (-b)**
- **Purpose:** Uses FTP bounce to scan the target.
- **Command:**
  ```bash
  nmap -b <ftp-server> <target>
  ```

---

## **Understanding Nmap Port States**

Nmap recognizes six port states:
- **Open:** The port is open and accepting connections.
- **Closed:** The port is closed and not accepting connections.
- **Filtered:** The port is blocked by a firewall.
- **Unfiltered:** The port is not blocked by a firewall.
- **Open/Filtered:** The port is either open or filtered.
- **Closed/Filtered:** The port is either closed or filtered.

---

## **Choosing the Right Scan Type**

- **TCP SYN Scan (-sS):** Best for quick scans and minimal trace.
- **TCP Connect Scan (-sT):** Suitable when root privileges are not available.
- **UDP Scan (-sU):** Useful for identifying UDP-based services.
- **TCP ACK Scan (-sA):** Helps map out firewalls.
- **TCP Window Scan (-sW):** Identifies open ports by TCP window size.
- **Idle Scan (-sI):** Uses a zombie host for stealth scanning.
- **IP Protocol Scan (-sO):** Scans for open IP protocols.
- **FTP Relay Host (-sF):** Uses FTP bounce for scanning.

---

## **Next Steps**
Continue to the next episode to learn how to discover the operating systems and service versions of target machines. Stay tuned for more advanced techniques and practical demonstrations!

[Next Episode: Discovering Operating Systems and Service Versions](06-Discovering-Target-Operating-System.md)

[Previous Episode: Performing First Nmap Scan](04-Performing-First-Nmap-Scan.md)
