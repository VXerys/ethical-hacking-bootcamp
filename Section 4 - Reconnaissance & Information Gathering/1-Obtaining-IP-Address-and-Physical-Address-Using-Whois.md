# 📚 **Episode Documentation: Obtaining IP Address, Physical Address Using Whois**

---

## 🌐 **Title: Obtaining IP Address, Physical Address Using Whois**

### 📝 **Overview**
In this episode, we dive into the basics of information gathering by learning how to obtain the IP address and physical address of a target website. We explore both active and passive methods to achieve this, including tools like `ping`, `nslookup`, and `whois`.

---

### 🛠️ **Tools Used**
- **Ping**: To send ICMP packets and retrieve the IP address of a target.
- **NSLookup**: To query DNS records and get the IP address of a domain.
- **Whois**: To gather detailed information about a domain, including IP address, physical address, and other metadata.

---

### 🔍 **Active Information Gathering**

#### 🕵️‍♂️ **Using Ping**
- **Command:** `ping <website>`
- **Purpose:** Sends ICMP packets to the target website and retrieves its IP address.
- **Example:**
  ```bash
  ping example.com
  ```
  - **Output:**
    ```
    PING example.com (93.184.216.34): 56 data bytes
    64 bytes from 93.184.216.34: icmp_seq=0 ttl=55 time=12.3 ms
    ```
  - **Notes:**
    - Some websites block ping probes, resulting in no responses.
    - Example: `ping facebook.com` successfully returns an IP address.

#### 🧪 **Using NSLookup**
- **Command:** `nslookup <website>`
- **Purpose:** Queries DNS records to retrieve the IP address of a domain.
- **Example:**
  ```bash
  nslookup example.com
  ```
  - **Output:**
    ```
    Server:         192.168.1.1
    Address:        192.168.1.1#53

    Non-authoritative answer:
    Name:   example.com
    Address: 93.184.216.34
    ```
  - **Notes:**
    - The IP address returned by `nslookup` matches the one obtained via `ping`.
      
    ![image](https://github.com/user-attachments/assets/e9c5c8b6-60f3-4d86-ab85-cc33a4537e29)

---

### 🔍 **Passive Information Gathering**

#### 📈 **Using IP Checker Websites**
- **Website:** [IPinfo.info](https://ipinfo.info/)
- **Steps:**
  1. Open Firefox and navigate to the IPinfo.info website.
  2. Enter the domain name or URL of the target website.
  3. Click "Check" to retrieve the IP address and additional details.
- **Example:**
  - **Input:** `example.com`
  - **Output:**
    - **IP Address:** 93.184.216.34
    - **Country:** United States
    - **City:** Ashburn, Virginia
    - **Reverse DNS:** example.com
    - **Registration Date:** 1997-03-14
    - **Expiration Date:** 2025-03-14
    - **DNS Servers:** ns1.example.com, ns2.example.com
    - **Physical Address:** 701 10th St NW, Washington, DC 20001, USA
      
  ![image](https://github.com/user-attachments/assets/cb9e9ca7-fda6-4955-b3f0-885d0dc628b4)

---

### 🔍 **Using Whois Tool**

#### 🗂️ **Command Line Usage**
- **Command:** `whois <website>`
- **Purpose:** Retrieves comprehensive information about a domain, including IP address, physical address, and other metadata.
- **Example:**
  ```bash
  whois example.com
  ```
  - **Output:**
    ```
    Domain Name: EXAMPLE.COM
    Registrar: NAMECHEAP.COM, INC.
    Whois Server: whois.namecheap.com
    Referral URL: http://www.namecheap.com
    Name Server: NS1.EXAMPLE.COM
    Name Server: NS2.EXAMPLE.COM
    Status: ACTIVE
    Updated Date: 2023-01-01
    Creation Date: 1997-03-14
    Expiration Date: 2025-03-14
    ```
  - **Notes:**
    - The `whois` tool provides more detailed information compared to `ping` and `nslookup`.
    - Example: `whois facebook.com` returns extensive information about Facebook's domain.
      
  ![image](https://github.com/user-attachments/assets/581cedd0-2eda-44bd-9674-58066c474a90)

---

### 📝 **Key Takeaways**
- **Active Methods:**
  - Use `ping` to retrieve the IP address of a target.
  - Use `nslookup` to query DNS records and get the IP address.
  
- **Passive Methods:**
  - Use IP checker websites like [IPinfo.info](https://ipinfo.info/) to gather additional information.
  
- **Detailed Information:**
  - Use `whois` to get comprehensive details about a domain, including IP address, physical address, and other metadata.

---

### 🧪 **Hands-On Practice**
1. **Try it yourself:**
   - Choose a website and use `ping`, `nslookup`, and `whois` to gather its IP address and physical address.
   - Compare the results from each method.

2. **Explore more:**
   - Experiment with different websites to see how much information is publicly available.
   - Note any discrepancies or additional details that may be useful for further analysis.

---

### 📖 **Next Steps**
In the next episode, we will explore more advanced techniques for information gathering, such as port scanning and vulnerability assessment:
[2. Whatweb Stealthy Scan](2-WhatWeb-Stealthy-Scan.md)

[Previous Episode](0-What-is-Information-Gathering.md)

