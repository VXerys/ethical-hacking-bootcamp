# 📚 **Theory Behind Scanning**

---

## **Overview**
In this episode, we delve into the theory behind **scanning**, the second phase of penetration testing. After completing the information gathering phase, we move on to scanning to gain a deeper understanding of the target's technical aspects. Scanning involves interacting with the target to identify open ports, services, and potential vulnerabilities.

---

### **Introduction to Scanning**

#### **Difference Between Information Gathering and Scanning**
- **Information Gathering:** Focuses on collecting a wide range of information, such as emails, phone numbers, and other details.
- **Scanning:** Focuses specifically on the technical aspects of the target, including identifying open ports and services [[1]].

#### **Why Scanning is Necessary**
- **Deep Dive:** Scanning allows for a more in-depth examination of the target system.
- **Identify Vulnerabilities:** Helps identify potential security issues that could be exploited by malicious actors.

#### **Using a Vulnerable Virtual Machine**
- **Purpose:** To practice scanning without violating ethical guidelines.
- **Resources:** We will use a free, vulnerable virtual machine that simulates real-world scenarios.
- **Details:** These VMs run outdated and vulnerable software, making them ideal for exploitation exercises.

---

### **Understanding Scanning**

#### **What is Scanning?**
- **Definition:** Scanning is the methodical process of inspecting systems, applications, and networks to find any potential flaws, incorrect setups, or vulnerabilities.

#### **Active vs. Passive Scanning**
- **Active Scanning:** Directly interacts with the target to gather information, such as sending packets and analyzing responses.
- **Passive Scanning:** Observes traffic without interacting with the target.

---

### **Types of Scanning**

#### **External vs. Internal Scanning**
- **External Scanning:** Scanning from outside the target's network, typically done from an external location.
- **Internal Scanning:** Scanning from within the target's network, often conducted by authorized personnel during internal penetration tests.

#### **Common Ports and Services**
- **Port 80 (HTTP):** Used for hosting web pages.
- **Port 443 (HTTPS):** Secure version of HTTP, used for secure web communication.
- **Port 21 (FTP):** Used for file transfers.
- **Port 22 (SSH):** Secure shell for remote access.
- **Port 25 (SMTP):** Used for sending emails.
- **Port 53 (DNS):** Domain Name System, used for resolving domain names to IP addresses.

#### **Why Are Ports Important?**
- **Open Ports:** Indicate services that are accessible and potentially exploitable.
- **Closed Ports:** Do not respond to connection attempts.
- **Filtered Ports:** Blocked by firewalls or other security measures.

---

### **Scanning Techniques**

#### **Network Scanning**
- **Objective:** Identify active hosts and open ports on a network.
- **Tools:** Nmap, Masscan, Angry IP Scanner.

#### **Port Scanning**
- **Objective:** Determine which ports are open and which services are running on those ports.
- **Techniques:**
  - **TCP SYN Scan:** Sends a TCP SYN packet and waits for a response.
  - **UDP Scan:** Sends UDP packets to check for open UDP ports.
  - **Ping Scan:** Checks if a host is active by sending ICMP echo requests.

#### **Fragmentation Scanning**
- **Objective:** Bypass firewall rules by fragmenting packets to avoid detection.
- **Tools:** Nmap supports fragmentation scanning.

---

### **Goals of Scanning**

#### **Primary Goals**
- **Identify Open Ports:** Locate ports that are open and potentially exploitable.
- **Discover Running Services:** Determine which services are running on open ports.
- **Version Detection:** Identify the version of software running on open ports.
- **Vulnerability Identification:** Detect known vulnerabilities in the software.

#### **Example: Scanning a Website**
- **Target:** A website hosted on Port 80.
- **Objective:** Determine if Port 80 is open and identify the web server.
- **Tools:** Nmap, WhatWeb.

---

### **Tools for Scanning**

#### **Nmap**
- **Description:** One of the most popular and versatile network scanning tools.
- **Features:**
  - TCP SYN Scanning
  - UDP Scanning
  - OS Detection
  - Version Detection
  - Script Scanning

#### **WhatWeb**
- **Description:** Identifies web technologies, content, and banners from websites.
- **Features:**
  - Detects web servers, CMS, JavaScript libraries, and more.
  - Provides detailed descriptions of detected technologies.

---

### **Next Steps**
In the next episode, we will explore the practical application of scanning techniques using tools like Nmap and WhatWeb. Stay tuned for more in-depth coverage and hands-on demonstrations!

[Next Episode: TCP & UDP: Understanding the Protocols Behind Network Communication](01-TCP-&-UDP.md)

[Previous Episode: Information Gathering](previous-episode.md)
