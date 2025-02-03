
# 📚 **Security Evasion Nmap Options**

## 🎥 Episode Overview
In this episode, we will explore advanced Nmap options designed to evade firewalls, Intrusion Detection Systems (IDS), and Intrusion Prevention Systems (IPS). These techniques are crucial for ethical hackers and penetration testers to conduct stealthy and efficient network scans. While some of these options may not be commonly used, it's important to be aware of them for advanced scenarios.

## 🔍 Key Takeaways

### 1. **Spoofing IP Address with `-S` Option**
The `-S` option allows you to spoof your IP address, making the target believe that the scan is coming from a different IP address. This can be useful for evading detection by firewalls or IDS that monitor specific IP addresses.

#### Example:
```bash
sudo nmap -S 8.8.8.8 -Pn <target-ip>
```
- **Explanation**:
  - `-S 8.8.8.8`: Spoofs the source IP address to `8.8.8.8`.
  - `-Pn`: Assumes all hosts are online, avoiding the need for a ping scan.

#### Limitations:
- You will not receive any scan results since the packets will be sent to the spoofed IP address.
- Requires the `-Pn` option to function correctly.
- May require specifying the network interface with `-e` if necessary.

#### Example with Network Interface:
```bash
sudo nmap -S 8.8.8.8 -Pn -e eth0 <target-ip>
```

### 2. **Specifying Source Port with `-g` Option**
The `-g` option allows you to specify the source port for the scan. This can be useful for bypassing firewalls that only allow traffic from specific ports.

#### Example:
```bash
sudo nmap -g 80 <target-ip>
```
- **Explanation**:
  - `-g 80`: Specifies port 80 as the source port.
  - This can help bypass firewalls that only allow traffic from port 80.

#### Note:
- Changing the source port alone may not be sufficient to bypass firewalls, especially if the firewall is configured to block specific traffic patterns.

### 3. **Changing Scan Types**
Different scan types can be used to evade firewalls that block specific types of traffic. For example, if a firewall blocks SYN scans (`-sS`), you can try using a FIN scan (`-sF`).

#### Common Scan Types:
- **SYN Scan (`-sS`)**: Performs a stealthy SYN scan.
- **FIN Scan (`-sF`)**: Sends a FIN packet without any other flags.
- **ACK Scan (`-sA`)**: Sends an ACK packet.
- **NULL Scan (`-sN`)**: Sends a packet with no flags set.

#### Example:
```bash
sudo nmap -sF <target-ip>
```
- **Explanation**:
  - `-sF`: Uses a FIN scan, which can bypass firewalls that block SYN scans.

#### Note:
- Understanding the underlying TCP/IP protocols is essential for choosing the right scan type. For example, FIN scans are useful against firewalls that block SYN packets but allow FIN packets.

### 4. **Using Decoy Scanning with `-D` Option**
The `-D` option allows you to create decoys, making it appear as though the scan is coming from multiple IP addresses, including yours. This can help obscure your true IP address and make it harder for the target to identify the source of the scan.

#### Example:
```bash
sudo nmap -D RND:5 <target-ip>
```
- **Explanation**:
  - `-D RND:5`: Uses five random decoy IP addresses.

#### Example with Specific Decoys:
```bash
sudo nmap -D 192.168.1.2,192.168.1.5,192.168.1.6,192.168.1.15,ME <target-ip>
```
- **Explanation**:
  - `ME`: Represents your true IP address.
  - The remaining IP addresses are decoys.

#### Note:
- Ensure the decoys are valid IP addresses within the same network if you are scanning a local target.
- Random decoys may not be effective if the decoy IPs are not truly random or if the target network is closely monitored.

### 5. **Fragmenting Packets with `-f` Option**
The `-f` option in Nmap allows you to split TCP headers into smaller fragments, making it harder for firewalls and IDS to detect the true nature of the scan. This technique is useful when the firewall drops large packets but allows smaller ones.

#### How It Works:
- **Single `-f`**: Splits the packet into fragments of 8 bytes or less.
- **Double `-f`**: Splits the packet into fragments of 16 bytes.

#### Example:
```bash
sudo nmap -f <target-ip>
```

#### Note:
- Be cautious when using this option, as some systems may have difficulty handling fragmented packets.
- Specify the fragment size using the `--mtu` option if needed:
  ```bash
  sudo nmap --mtu 1400 <target-ip>
  ```

### 6. **Using Timing Templates with `-T` Option**
Timing templates allow you to adjust the speed and stealthiness of your scan. Lower numbers are more stealthy but slower, while higher numbers are faster but less stealthy.

#### Available Modes:
- **Paranoid (`-T0`)**: Extremely slow, ideal for IDS evasion.
- **Sneaky (`-T1`)**: Slow, also useful for IDS evasion.
- **Polite (`-T2`)**: Balanced speed and stealth.
- **Normal (`-T3`)**: Default mode.
- **Aggressive (`-T4`)**: Faster, less stealthy.
- **Insane (`-T5`)**: Fastest, least stealthy.

#### Example:
```bash
sudo nmap -T0 <target-ip>
```
- **Explanation**:
  - `-T0`: Uses the Paranoid timing template, which is very slow but highly stealthy.

#### Note:
- Adjust the timing template based on the urgency of the scan and the level of detection risk.

### 7. **Combining Techniques**
You can combine multiple evasion techniques to enhance the effectiveness of your scan. For example, you can use a combination of spoofing, fragmented packets, and timing templates.

#### Example:
```bash
sudo nmap -S 8.8.8.8 -Pn -f -T0 <target-ip>
```
- **Explanation**:
  - `-S 8.8.8.8`: Spoofs the source IP address.
  - `-Pn`: Assumes all hosts are online.
  - `-f`: Sends fragmented packets.
  - `-T0`: Uses the Paranoid timing template.

## 📝 Notes & Tips
- **Ethical Considerations**: Always ensure you have permission to scan the target.
- **Testing Environment**: Practice these techniques in a controlled environment, such as Metasploitable or a lab setup.
- **Continuous Learning**: Revisit and review material as needed to solidify understanding.
- **Google It**: If you're unsure about a concept, don't hesitate to look it up online. This is a great way to deepen your knowledge.

## 📔 Additional Resources
- [Nmap Official Documentation](https://nmap.org/book/man.html)
- [Firewall Evasion Techniques](https://nmap.org/book/idsevasion.html)
- [Nmap Scripting Engine (NSE)](https://nmap.org/nsedoc/)
- [Firewall/IDS Evasion and Spoofing](https://nmap.org/book/firewall-evasion.html)[[2]]

## 📚 Next Steps
Continue to the next episode to learn how to create your first penetration testing tool. Stay tuned for more advanced techniques and practical demonstrations!

### Further Reading:
- Explore [Firewall Evasion Techniques](https://nmap.org/book/idsevasion.html) to enhance your scanning skills.
- Dive deeper into [Nmap Scripting Engine (NSE)](https://nmap.org/nsedoc/) for more advanced scripting capabilities.

## **Next Steps**
Continue to the next episode to learn how to create your first penetration testing tool. Stay tuned for more advanced techniques and practical demonstrations!

[👉 **Next Episode: Creating Your First Penetration Testing Tool**](next-episode.md)

[👈 **Previous Episode: Using Decoys and Packet Fragmentation**](previous-episode.md)

