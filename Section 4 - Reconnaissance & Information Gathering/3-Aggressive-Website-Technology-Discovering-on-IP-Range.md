## **Aggressive Website Technology Discovering on IP Range**

### 📝 **Overview**
In this episode, we expand our knowledge of the **WhatWeb** tool by demonstrating how to perform an **aggressive scan** across an entire IP range. This technique allows us to gather detailed information about multiple devices within a network, including web technologies, services, and potential vulnerabilities. We will cover how to identify active devices, handle errors gracefully, and log the results for future reference.

---

### 🛠️ **Tools Used**
- **WhatWeb**: A tool for detecting web technologies and services.
- **Terminal**: For running commands and managing files.

---

### 🔍 **Understanding IP Ranges**

#### 📌 **Subnet Mask and IP Range**
- **Subnet Mask:** Defines the range of valid IP addresses within a network.
- **Example:** For a subnet mask of `255.255.255.0`, the last octet is variable, meaning the IP range is from `192.168.1.0` to `192.168.1.255`.

#### 📘 **Determining Your Network Range**
- Use the `ifconfig` or `ip addr` command to find your local IP address and subnet mask.
- Example:
  ```bash
  sudo ifconfig
  ```
  - **Output:**
    ```
    inet 192.168.1.4  netmask 255.255.255.0
    ```

- **Range Calculation:**
  - With a subnet mask of `255.255.255.0`, the IP range is `192.168.1.0` to `192.168.1.255`.

---

### 🧪 **Performing an Aggressive Scan on an IP Range**

#### 🚀 **Command Structure**
```bash
whatweb --aggression 3 --verbose --no-errors <IP Range>
```

![image](https://github.com/user-attachments/assets/3c3f4256-d1f9-4810-b9cf-e3e391bcdf6d)

#### 📘 **Breaking Down the Command**
- **`--aggression 3`**: Uses the aggressive scanning level, which performs a deeper scan and makes more HTTP requests.
- **`--verbose`**: Provides detailed descriptions of detected plugins.
- **`--no-errors`**: Suppresses output for unreachable IP addresses.
- **`<IP Range>`**: Specifies the range of IP addresses to scan.

#### 📘 **Example Command**
```bash
whatweb --aggression 3 --verbose --no-errors 192.168.1.0/24
```

#### 📝 **Interpreting the Output**
- **Detected Devices:**
  - **IP Address:** `192.168.1.1`
    - **Device:** Router
    - **Detected Plugins:**
      - **Password Field:** Found a password field that can be used for brute-force attacks.
      - **HTTP Server:** Running on port 80.
  - **IP Address:** `192.168.1.10`
    - **Device:** Laptop
    - **Detected Plugins:**
      - **HTTP Server:** Running on port 80 but returns a `403 Forbidden` status code.

---

### 📝 **Handling Errors Gracefully**

#### 📘 **Suppressing Offline IP Addresses**
To avoid clutter from unreachable IP addresses, use the `--no-errors` flag:
```bash
whatweb --aggression 3 --verbose --no-errors 192.168.1.0/24
```

#### 📘 **Clearing Terminal Output**
To clean up the terminal after running multiple commands:
```bash
clear
```

---

### 📝 **Logging Results**

#### 📘 **Saving Output to a File**
To log the results of your scan to a file, use the `--log-verbose` option:
```bash
whatweb --aggression 3 --verbose --no-errors --log-verbose=results.txt 192.168.1.0/24
```
![image](https://github.com/user-attachments/assets/5a4bf4f7-5675-4858-86bd-0ac2410a8ecf)

#### 📘 **Checking the Log File**
After the scan completes, verify the contents of the log file:
```bash
cat results.txt
```

#### 📝 **Example Output:**
```plaintext
192.168.1.1
  Technologies Detected:
    Password Field (Description: Detected a password field)
    HTTP Server/2.4.6 (Description: Apache HTTP Server)
    Country: United States
    IP Address: 192.168.1.1

192.168.1.10
  Technologies Detected:
    HTTP Server/2.4.6 (Description: Apache HTTP Server)
    Country: United States
    IP Address: 192.168.1.10
    Status Code: 403 Forbidden
```

---

### 📖 **Next Steps**
Continue to the next episode to learn how to **harvest emails** from a domain. Stay tuned for more advanced techniques and practical applications!

[Next Episode: Email Harvesting from a Domain](4-Gathering-Emails-Using-theHarvester-&-Hunter-io.md)

[Previous Episode: Whatweb Stealthy Scan](2-WhatWeb-Stealthy-Scan.md)

