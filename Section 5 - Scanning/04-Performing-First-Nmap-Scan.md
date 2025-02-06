# 📚 **Performing First Nmap Scan**

---

## **Overview**
In this episode, we introduce **Nmap**, a powerful network scanning tool essential for ethical hackers. We will cover how to perform a basic Nmap scan to discover hosts and services on a computer network. This tool is widely used in penetration testing to identify open ports and running services.

---

## **What is Nmap?**
Nmap (Network Mapper) is a free and open-source network scanner used to discover hosts and services on a network by sending packets and analyzing responses [[1]]. It helps identify active hosts, open ports, and running services. Nmap is an indispensable tool for ethical hackers, as it provides detailed information about network configurations and potential vulnerabilities.

---

## **Preparing the Environment**
1. **Ensure Metasploitable is Running:**
   - Start your Metasploitable virtual machine.
2. **Connect Other Devices:**
   - Turn on any other devices connected to your home network to simulate a multi-host environment.
3. **Verify Network Configuration:**
   - Use `ifconfig` or `ip addr` to check the IP address of your Metasploitable VM.
   - Ensure your network settings are correctly configured for bridged networking.

---

## **Running Nmap with Basic Scan**

### **Basic Nmap Command**
- **Syntax:**
  ```bash
  nmap <target>
  ```
- **Example:**
  ```bash
  nmap 192.168.1.6
  ```

![image](https://github.com/user-attachments/assets/6bfd0bb3-43b3-4a55-aa1b-49d22a888f4c)

### **Interpreting the Output**
- **Host Status:** Reports whether the host is up or down.
- **Open Ports:** Lists open ports on the target machine.
- **Services:** Identifies the services running on each open port.

### **Example Output for Metasploitable**
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

- **Explanation:**
  - **Host is up:** The target machine is active.
  - **Open Ports:**
    - **Port 21 (FTP):** File Transfer Protocol.
    - **Port 22 (SSH):** Secure Shell.
    - **Port 80 (HTTP):** Hypertext Transfer Protocol, indicating a web server.

### **Verifying Web Server**
- **Access Web Server:**
  - Open Firefox and enter `192.168.1.6` in the address bar.
  - Verify that the Metasploitable is hosting a webpage.
  - The webpage may contain vulnerabilities that will be explored in later lessons.

---

## **Scanning a Range of IP Addresses**

### **Specifying IP Range**
- **Syntax:**
  ```bash
  nmap 192.168.1.1-255
  ```
  or
  ```bash
  nmap 192.168.1.1/24
  ```
- **Explanation:**
  - **192.168.1.1-255:** Scans all IP addresses from 192.168.1.1 to 192.168.1.255.
  - **192.168.1.1/24:** Scans the entire subnet `192.168.1.0/24`.

### **Interpreting the Output for Multiple Hosts**
```plaintext
Starting Nmap 7.91 ( https://nmap.org ) at 2025-02-03 12:05 UTC
Nmap scan report for 192.168.1.6
Host is up (0.0002s latency).
Not shown: 977 closed ports
PORT   STATE SERVICE
21/tcp open  ftp
22/tcp open  ssh
80/tcp open  http

Nmap scan report for 192.168.1.4
Host is up (0.0003s latency).
All 1000 scanned ports on 192.168.1.4 are closed.

Nmap scan report for 192.168.1.1
Host is up (0.0002s latency).
PORT    STATE SERVICE
22/tcp  open  ssh
23/tcp  open  telnet
53/tcp  open  domain
80/tcp  open  http
443/tcp open  https
445/tcp filtered microsoft-ds
```

- **Explanation:**
  - **192.168.1.6 (Metasploitable):** Same results as the basic scan.
  - **192.168.1.4:** All 1000 scanned ports are closed, indicating a secure device.
  - **192.168.1.1 (Router):** Open ports include SSH, Telnet, Domain, HTTP, and HTTPS.
  - **Filtered Ports:** Ports marked as "filtered" indicate that the port is unreachable, possibly due to a firewall.

---

## **Understanding Nmap Options**

### **Default Behavior**
- **Scans Top 1000 Ports:** By default, Nmap scans the most commonly used 1000 ports.
- **Closed Ports:** Not shown unless explicitly requested.
- **Timing Options:** Adjust scan speed and timing with options like `-T0` (paranoid) to `-T5` (insane).

### **Advanced Scanning Options**
- **Scan All Ports:**
  ```bash
  nmap -p- 192.168.1.6
  ```
- **Exclude Certain IPs:**
  ```bash
  nmap --exclude 192.168.1.4 192.168.1.1-255
  ```
- **Service Version Detection:**
  ```bash
  nmap -sV 192.168.1.6
  ```
- **OS Detection:**
  ```bash
  nmap -O 192.168.1.6
  ```

---

## **Recording Results**
- **Documentation:** In a real penetration test, document all findings in a report.
- **Organize Information:** Use tables or spreadsheets to organize IP addresses, open ports, and services.
- **Follow-Up Actions:** Based on the scan results, plan further actions such as vulnerability assessment and exploitation.

---

## **Next Steps**
Continue to the next episode to learn more advanced Nmap techniques, such as service version detection, OS detection, and script scanning. Stay tuned for more in-depth coverage and practical demonstrations!

[Next Episode: Different Nmap Scan Types](05-Different-Nmap-Scan-Types.md)

[Previous Episode: Netdiscover](03-Netdiscover.md)
