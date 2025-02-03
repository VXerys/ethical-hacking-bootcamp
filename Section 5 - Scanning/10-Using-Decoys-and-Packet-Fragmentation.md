
# 📚 **Using Decoys and Packet Fragmentation**

## 🎥 Episode Overview
In this episode, we will explore advanced techniques to bypass firewalls and Intrusion Detection Systems (IDS) using Nmap. Specifically, we will cover two key methods: **decoys** and **packet fragmentation**. These techniques are designed to obscure the true source of the scan and make it more difficult for firewalls and IDS to detect and block the scan.

## 🔍 Key Takeaways

### 1. **Understanding Filtered Ports**
Filtered ports are those where Nmap cannot determine whether the port is open or closed. This typically occurs when packets are dropped, possibly due to a firewall blocking them. When Nmap encounters a filtered port, it flags it as such, indicating that the port is unreachable.

#### Example:
```plaintext
All 1000 scanned ports on <target-ip> are filtered.
```

### 2. **Identifying Filtered Ports**
To identify filtered ports, you can use the SYN scan (`-sS`) or other scan types. If you notice that all ports are flagged as filtered, it is likely that the target is protected by a firewall.

#### Example:
```bash
sudo nmap -sS <target-ip>
```

### 3. **Packet Fragmentation with `-f` Option**
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

### 4. **Using Decoys with `-D` Option**
The `-D` option allows you to create decoys, which makes it appear as though the scan is coming from multiple IP addresses, including yours. This can help obscure your true IP address and make it harder for the target to identify the source of the scan.

#### How It Works:
- **Random Decoys**: Use the `RND:<number>` syntax to specify the number of random decoys.
- **Specific Decoys**: Provide a list of IP addresses, including your true IP address (`ME`).

#### Example:
```bash
sudo nmap -D RND:5 <target-ip>
```
Or, using specific decoys:
```bash
sudo nmap -D 192.168.1.2,192.168.1.5,192.168.1.6,192.168.1.15,ME <target-ip>
```

#### Note:
- Ensure the decoys are valid IP addresses within the same network if you are scanning a local target.
- Random decoys may not be effective if the decoy IPs are not truly random or if the target network is closely monitored.

### 5. **Combining Techniques**
You can combine packet fragmentation and decoys to enhance the effectiveness of your scan:
```bash
sudo nmap -f -D RND:5 <target-ip>
```

### 6. **Testing with Wireshark**
To verify the effectiveness of these techniques, you can use Wireshark to capture and analyze the network traffic. This will help you confirm whether the decoys and fragmented packets are working as intended.

#### Example:
1. **Start Wireshark** on the target machine.
2. **Run the Nmap scan** with the desired options.
3. **Analyze the captured packets** to ensure they appear as expected.

## 📝 Notes & Tips
- **Ethical Considerations**: Always ensure you have permission to scan the target.
- **Testing Environment**: Practice these techniques in a controlled environment, such as Metasploitable or a lab setup.
- **Performance Impact**: Some techniques may slow down the scan or consume more resources. Adjust settings accordingly.

## 📔 Additional Resources
- [Nmap Official Documentation](https://nmap.org/book/man.html)
- [Wireshark Documentation](https://www.wireshark.org/docs/)
- [Firewall Evasion Techniques](https://nmap.org/book/idsevasion.html)

## 📚 Next Steps
Continue to the next episode to learn how to perform vulnerability analysis and prepare for exploitation. Stay tuned for more advanced techniques and practical demonstrations!

### Further Reading:
- Explore [Firewall Evasion Techniques](https://nmap.org/book/idsevasion.html) to enhance your scanning skills.
- Dive deeper into [Nmap Scripting Engine (NSE)](https://nmap.org/nsedoc/) for more advanced scripting capabilities.

## **Next Steps**
Continue to the next episode to learn how to perform vulnerability analysis and prepare for exploitation. Stay tuned for more advanced techniques and practical demonstrations!

[👉 **Next Episode: Security Evasion Nmap Options**](next-episode.md)

[👈 **Previous Episode: What is a Firewall/IDS?**](previous-episode.md)
