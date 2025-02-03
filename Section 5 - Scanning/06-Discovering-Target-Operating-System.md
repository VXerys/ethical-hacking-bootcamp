# 📚 **Discovering Target Operating System**

---

## **Overview**
In this episode, we explore how to identify the **operating system** of a target machine using **Nmap**, a powerful network scanning tool. We will cover the principles behind Nmap's OS detection feature, which relies on a database of known OS fingerprints, and demonstrate its application on different machines: Metasploitable (Linux), Windows 7 VM, and a Windows 10 physical machine. Additionally, we discuss the importance of having at least one open and one closed port for accurate detection.

---

## **Introduction to OS Detection with Nmap**
#### **Why OS Detection?**
- **Critical Information:** Knowing the operating system helps tailor attacks and exploit vulnerabilities specific to that OS.
- **Reconnaissance:** OS detection is a crucial step in the reconnaissance phase of penetration testing.
#### **Nmap OS Detection**
- **Database:** Nmap utilizes a comprehensive database of known OS fingerprints to match against scanned hosts.
- **Prerequisites:** At least one open and one closed port on the target machine are required for accurate detection [[1]].

---

## **Prerequisites for OS Detection**
- **Open Port:** A port that accepts incoming connections.
- **Closed Port:** A port that does not accept incoming connections.
- **Filtered Port:** A port that is blocked by a firewall, making it inaccessible.

---

## **Scanning Metasploitable (Linux)**
### **Command**
```bash
sudo nmap -O <target_IP>
```
### **How It Works**
- **OS Fingerprinting:** Nmap compares the scanned host's responses to its database of known OS fingerprints.
- **Results:**
  - **Operating System:** Identified as Linux.
  - **Version Details:** Exact version of Linux running on the machine.
  - **Virtual Machine Identification:** Detected as a virtual machine based on MAC address.
- **Example Output**
```plaintext
Starting Nmap 7.91 ( https://nmap.org ) at 2025-02-03 12:00 UTC
Nmap scan report for 192.168.1.10
Host is up (0.0002s latency).
Not shown: 997 closed ports
PORT   STATE SERVICE
21/tcp open  ftp
22/tcp open  ssh
80/tcp open  http
MAC Address: 08:00:27:5A:BC:DE (Oracle VirtualBox)
Device type: general purpose
Running: Linux 3.X|4.X
OS details: Linux 3.13 - 4.9 (Ubuntu 14.04 LTS / 16.04 LTS)
Network Distance: 1 hop
```

---

## **Scanning Windows 10 Physical Machine**
### **Command**
```bash
sudo nmap -O <target_IP>
```
### **How It Works**
- **OS Fingerprinting:** Nmap attempts to match the scanned host's responses to its database of known OS fingerprints.
- **Results:**
  - **Failed Detection:** Unable to detect the operating system due to all ports being closed or filtered.
- **Example Output**
```plaintext
Starting Nmap 7.91 ( https://nmap.org ) at 2025-02-03 12:05 UTC
Nmap scan report for 192.168.1.7
Host is up (0.0002s latency).
All 1000 scanned ports on 192.168.1.7 are filtered
```

---

## **Scanning Windows 7 Virtual Machine**
### **Command**
```bash
sudo nmap -O <target_IP>
```
### **How It Works**
- **OS Fingerprinting:** Nmap matches the scanned host's responses to its database of known OS fingerprints.
- **Results:**
  - **Partial Detection:** Successfully identifies the operating system as Windows but incorrectly guesses the version.
- **Example Output**
```plaintext
Starting Nmap 7.91 ( https://nmap.org ) at 2025-02-03 12:10 UTC
Nmap scan report for 192.168.1.14
Host is up (0.0002s latency).
Not shown: 999 filtered ports
PORT   STATE SERVICE
445/tcp open  microsoft-ds
MAC Address: 08:00:27:5A:BC:DF (Oracle VirtualBox)
Device type: general purpose
Running: Microsoft Windows 7 or 8
OS details: Windows 7 SP1, Windows 8.1, or Windows Server 2008 R2 SP1
Network Distance: 1 hop
```

---

## **Understanding Limitations**
- **Port Requirements:** At least one open and one closed port are necessary for accurate OS detection.
- **Filtered Ports:** If all ports are filtered, Nmap may fail to detect the operating system.
- **Accuracy:** While Nmap's OS detection is generally reliable, it may occasionally misidentify specific versions.

---

## **Virtual Machine Detection**
- **MAC Address Analysis:** Nmap can sometimes detect that a machine is a virtual machine based on its MAC address.
- **Honey Pot Indication:** Detecting a virtual machine can indicate the presence of a honey pot, a deliberately vulnerable environment used to lure attackers.

---

## **Next Steps**
Continue to the next episode to learn how to discover the exact versions of services running on open ports. Stay tuned for more advanced techniques and practical demonstrations!

[Next Episode: Detecting Version Of Service Running On An Open Port](07-Detecting-Version-Of-Service-Running-On-An-Open-Port.md)

[Previous Episode: Different Nmap Scan Types](05-Different-Nmap-Scan-Types.md)

