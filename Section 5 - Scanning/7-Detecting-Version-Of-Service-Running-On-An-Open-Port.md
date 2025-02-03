# 📚 **Detecting Version of Service Running on an Open Port**

## 🎥 Episode Overview

Welcome back! In this episode, we will explore how to determine the exact version of software running on open ports. Understanding the version of services can significantly help in identifying potential vulnerabilities and planning targeted attacks. We'll cover how to perform version discovery using Nmap and how to interpret the results.

## 🛠️ Tools & Prerequisites

Ensure you have the following tools and environments set up:

- **Nmap**: The primary tool for network scanning and service enumeration.
- **Metasploitable**: A vulnerable virtual machine used as a target for testing.
- **Linux Terminal**: Essential for executing Nmap commands.

## 🔍 Key Takeaways

### 1. **Why Version Discovery Matters**

Version discovery is crucial for ethical hackers and penetration testers because:
- It helps narrow down the list of potential vulnerabilities.
- Knowing the exact version can reveal specific patches or bugs that can be exploited.
- It aids in creating a more accurate and targeted attack plan.

### 2. **Performing Version Discovery with Nmap**

To perform version discovery, use the `-sV` option. This option tells Nmap to attempt to determine the version of the service running on each open port.

#### Example:
```bash
sudo nmap -sV <target-ip>
```
This command will perform a version scan on the specified target.

#### Interpretation of Results:
- **Port Number**: The port number where the service is running.
- **State**: Whether the port is open, closed, filtered, etc.
- **Service Name**: The name of the service running on the port.
- **Version**: The exact version of the service.

#### Example Output:
```plaintext
PORT     STATE SERVICE VERSION
21/tcp   open  ftp     vsftpd 2.3.4
22/tcp   open  ssh     OpenSSH 4.7p1 Debian 8ubuntu1
25/tcp   open  smtp    Postfix smtpd 2.6.5
80/tcp   open  http    Apache httpd 2.2.8 ((Ubuntu))
445/tcp  open  netbios-ssn Samba smbd 3.0.20-Debian
```

### 3. **Intensity of Version Scanning**
The `-sV` option can be further refined using the `--version-intensity` parameter, which specifies the level of effort Nmap should spend on version detection. The value can range from 0 to 9, with 7 being the default.

#### Example:
```bash
sudo nmap -sV --version-intensity 9 <target-ip>
```
- **Default Intensity (7)**: Provides a good balance between speed and accuracy.
- **Higher Intensity (9)**: Increases the likelihood of correctly identifying the service version but takes longer to complete.

### 4. **Aggressive Scan with `-A` Option**
The `-A` option enables aggressive scanning, combining several advanced features:
- **OS Detection (`-O`)**: Identifies the operating system running on the target.
- **Version Detection (`-sV`)**: Determines the version of services running on open ports.
- **Script Scanning (`-sC`)**: Runs a series of default NSE scripts to gather additional information.

#### Example:
```bash
sudo nmap -A <target-ip>
```

#### Interpretation of Results:
- **OS Detection**: Provides information about the operating system.
- **Service Version**: Identifies the exact version of services.
- **Additional Information**: Includes details from NSE scripts, such as FTP anonymous login, SSH host keys, SMTP commands, HTTP server headers, and more.

#### Example Output:
```plaintext
Nmap scan report for 192.168.1.5
Host is up (0.00029s latency).
Not shown: 995 closed ports
PORT     STATE SERVICE       VERSION
21/tcp   open  ftp           vsftpd 2.3.4
22/tcp   open  ssh           OpenSSH 4.7p1 Debian 8ubuntu1
25/tcp   open  smtp          Postfix smtpd 2.6.5
80/tcp   open  http          Apache httpd 2.2.8 ((Ubuntu))
445/tcp  open  netbios-ssn   Samba smbd 3.0.20-Debian
| smb-os-discovery: 
|   OS: Windows 7 Professional 7601 Service Pack 1 (Windows 7 Professional 6.1)
|   Computer name: WIN7PRO
|   NetBIOS computer name: WIN7PRO<00>
|   Domain name: WORKGROUP
|   Forest name: WORKGROUP
|   Local Master Browser: No
|   Domain Controller: Yes
|_  System time: 2023-10-05T14:45:16-07:00
```

### 5. **Using the Results**
Once you have the version information, you can:
- **Search for Known Vulnerabilities**: Use the version number to search for known vulnerabilities on the internet.
- **Craft Targeted Exploits**: Create exploits tailored to the specific version of the software.
- **Document Findings**: Add the findings to your report for future reference.

## 📝 Notes & Tips
- **Time Considerations**: Higher intensity levels take longer to complete. Always consider the trade-off between speed and accuracy.
- **Ethical Considerations**: Ensure you have permission to scan the target before using aggressive options like `-A`.
- **NSE Scripts**: Nmap Scripting Engine (NSE) scripts provide additional information beyond basic port scanning. They can be customized or extended for specific needs.

## 📔 Additional Resources
- [Nmap Official Documentation](https://nmap.org/book/man.html)
- [Metasploitable Documentation](https://www.metasploit.com/metasploitable2)
- [Nmap Scripting Engine (NSE)](https://nmap.org/nsedoc/)

## 📚 Next Steps
Continue to the next episode to learn how to bypass firewalls, Intrusion Detection Systems (IDS), and Intrusion Prevention Systems (IPS) using Nmap. Stay tuned for more advanced techniques and practical demonstrations!

### Further Reading:
- Explore [Firewall Evasion Techniques](https://nmap.org/book/idsevasion.html) to enhance your scanning skills.
- Dive deeper into [Nmap Scripting Engine (NSE)](https://nmap.org/nsedoc/) for more advanced scripting capabilities.

## **Next Steps**
Continue to the next episode to learn how to bypass firewalls, Intrusion Detection Systems (IDS), and Intrusion Prevention Systems (IPS) using Nmap. Stay tuned for more advanced techniques and practical demonstrations!

[Next Episode: Bypassing Firewalls and IDS/IPS](next-episode.md)

[Previous Episode: Filtering Port Range & Output of Scan Results](previous-episode.md)