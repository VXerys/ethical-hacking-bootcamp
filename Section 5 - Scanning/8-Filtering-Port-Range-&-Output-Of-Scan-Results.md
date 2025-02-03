# 📚 **Filtering Port Range & Output of Scan Results**

## 🎥 Episode Overview
In this episode, we delve deeper into the world of Nmap by exploring various options that allow us to customize our scans based on specific requirements. This includes filtering port ranges, managing scan outputs, and understanding how to handle different types of scan results. These techniques are essential for ethical hackers and penetration testers who need precise control over their reconnaissance activities.

## 🛠️ Tools & Prerequisites
Before diving into the episode, ensure you have the following tools and environments set up:

- **Nmap**: The primary tool for network scanning and service enumeration.
- **Metasploitable**: A vulnerable virtual machine used as a target for testing.
- **Linux Terminal**: Essential for executing Nmap commands.

## 🔍 Key Takeaways

### 1. **Filtering Specific Ports**
Nmap allows you to specify which ports you want to scan using the `-p` option. This is particularly useful when you are interested in a particular set of ports rather than scanning the entire range.

#### Examples:
- **Single Port Scan:**
  ```bash
  nmap -p 80 <target-ip>
  ```
  This command scans only port 80 on the specified target.

- **Multiple Ports Scan:**
  ```bash
  nmap -p 80,22,100 <target-ip>
  ```
  This command scans ports 80, 22, and 100 on the specified target.

- **Range of Ports Scan:**
  ```bash
  nmap -p 1-100 <target-ip>
  ```
  This command scans ports from 1 to 100 on the specified target.

### 2. **Scanning All Ports**
To scan all 65,535 ports, you can use the following command:
```bash
nmap -p 1-65535 <target-ip>
```
However, this approach is time-consuming and resource-intensive. It is generally recommended to focus on specific port ranges or commonly used ports.

### 3. **Quick Scan with Top 100 Ports**
For a faster scan that still provides valuable information, use the `-F` (capital F) option:
```bash
nmap -F <target-ip>
```
This option limits the scan to the top 100 most common ports, significantly reducing the time required compared to scanning all 1,000 ports.

### 4. **Outputting Scan Results**
Nmap offers several methods to manage the output of your scan results, allowing you to store them in files or display them directly in the terminal.

#### Methods:
- **Saving Output to a File:**
  ```bash
  nmap -oN outputfile.txt <target-ip>
  ```
  This command saves the scan results in a plain text file named `outputfile.txt`.

- **Saving Output in XML Format:**
  ```bash
  nmap -oX outputfile.xml <target-ip>
  ```
  This command saves the scan results in an XML file, which can be useful for further processing or integration with other tools.

- **Saving Output in Grepable Format:**
  ```bash
  nmap -oG outputfile.gnmap <target-ip>
  ```
  This command saves the scan results in a Grepable format, making it easy to search and filter specific information.

### 5. **Using Root Privileges**
Certain Nmap options require elevated privileges, such as `-sS` (SYN scan). Use `sudo` to execute these commands:
```bash
sudo nmap -sS <target-ip>
```

### 6. **Discovering Active Hosts with `-sn` Option**
The `-sn` option performs a ping scan to identify active hosts without performing a port scan:
```bash
nmap -sn <target-ip-range>
```
This is useful for quickly determining which hosts are up on your network.

### 7. **Specifying Port Range with `-p` Option**
The `-p` option allows you to specify a custom range of ports to scan:
```bash
nmap -p 1-100 <target-ip>
```
This command scans ports from 1 to 100 on the specified target.

### 8. **Aggressive Scan with `-A` Option**
The `-A` option enables aggressive scanning, including OS detection, version detection, and script scanning:
```bash
nmap -A <target-ip>
```
While this option provides extensive information, it may be more detectable by firewalls or Intrusion Detection Systems (IDS).

## 📝 Notes & Tips
- **FTP Anonymous Login:** The `-A` scan revealed that anonymous FTP login was enabled on the target. This is a significant security vulnerability that can be exploited.
- **SSH Enumeration:** The scan also provided information about the SSH host key, which can be useful for identifying potential misconfigurations.
- **SMTP Commands:** Information about allowed SMTP commands was gathered, which can be valuable for further analysis.
- **HTTP Server Headers:** The scan retrieved HTTP server headers and titles, providing insights into the web server configuration.
- **SMB Enumeration:** The scan enumerated SMB details, including the computer name, domain name, and SMB security mode.

## 📔 Additional Resources
- [Nmap Official Documentation](https://nmap.org/book/man.html)
- [Metasploitable Documentation](https://www.metasploit.com/metasploitable2)

## 📚 Next Steps
Continue to the next episode to learn how to discover the exact versions of services running on open ports. Stay tuned for more advanced techniques and practical demonstrations!

### Further Reading:
- Explore the [Nmap Scripting Engine (NSE)](https://nmap.org/nsedoc/) for more advanced scripting capabilities.
- Dive deeper into [Firewall Evasion Techniques](https://nmap.org/book/idsevasion.html) to enhance your scanning skills.

## **Next Steps**
Continue to the next episode to learn how to discover the exact versions of services running on open ports. Stay tuned for more advanced techniques and practical demonstrations!

[Next Episode: Discovering Service Versions](next-episode.md)

[Previous Episode: Different Nmap Scan Types](previous-episode.md)

