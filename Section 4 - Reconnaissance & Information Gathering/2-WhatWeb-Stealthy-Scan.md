# 📚 **Episode Documentation: Whatweb Stealthy Scan**

---

## 🌐 **Title: Whatweb Stealthy Scan**

### 📝 **Overview**
In this episode, we explore the powerful tool **WhatWeb**, designed to gather detailed information about websites by identifying the technologies they use. We focus on performing a **stealthy scan**, which is the default and safest level of scanning, requiring minimal interaction with the target website. This method ensures that we can gather valuable information without causing unnecessary disruptions.

---

### 🛠️ **Tools Used**
- **WhatWeb**: A tool used to identify technologies, content, and banners from websites.

---

### 🔍 **Understanding WhatWeb**

![image](https://github.com/user-attachments/assets/0258baba-4e3f-42cf-b053-5916399f7064)

#### 📚 **What is WhatWeb?**
WhatWeb is a tool that automatically identifies technologies used on websites, including:
- Web servers
- Embedded devices
- JavaScript libraries
- CMS platforms
- Content management systems (CMS)
- E-commerce platforms
- Blogging platforms
- And much more.

#### 📘 **Why Use WhatWeb?**
- **Information Gathering:** Helps in understanding the technology stack of a website.
- **Security Audits:** Identifies potential vulnerabilities based on the technologies detected.
- **Penetration Testing:** Provides insights into the infrastructure of a target.

#### 📝 **Key Features**
- **Plugins:** Over 1,700 plugins that detect various web technologies.
- **Aggression Levels:** Different levels of scanning intensity, ranging from stealthy to aggressive.
- **Verbose Output:** Detailed descriptions of detected plugins.
  
---

### 🔍 **Stealthy Scan Mode**

#### 🕵️‍♂️ **Default Aggression Level**
The default aggression level in WhatWeb is **stealthy**, which:
- Requires only **one HTTP request** per website.
- Is the fastest and least intrusive mode.
- Ensures minimal impact on the target website.

#### 📘 **When to Use Stealthy Scan**
Use the stealthy scan when:
- You are exploring unknown websites.
- You want to gather basic information without alerting the website administrators.
- You do not have explicit permission to perform more aggressive scans.

---

### 🛠️ **Getting Started with WhatWeb**

#### 🔍 **Basic Command Syntax**
```bash
whatweb <target>
```
- **Target:** Can be a URL, hostname, or IP address.

  ![image](https://github.com/user-attachments/assets/b476fc72-2f11-4c9e-8b97-0973279037d0)

#### 📘 **Command Options**
To view all available options, use:
```bash
whatweb --help
```

![image](https://github.com/user-attachments/assets/5084e379-e972-46ab-9606-058b60e00e37)

- **Aggression Levels:**
  - `-a 1`: Stealthy (default)
  - `-a 3`: Aggressive
  - `-a 4`: Heavy (most aggressive)

- **Verbose Output:**
  - `-v`: Provides detailed descriptions of detected plugins.

![image](https://github.com/user-attachments/assets/14796c47-5ad2-4715-9cac-7f2ebcb877f3)

---

### 🧪 **Hands-On Practice: Stealthy Scan**

#### 📝 **Step-by-Step Guide**

1. **Open Terminal in Kali Linux:**
   ```bash
   $ whatweb
   ```

2. **View Basic Help Menu:**
   ```bash
   $ whatweb --help
   ```

3. **Perform a Stealthy Scan:**
   ```bash
   $ whatweb -a 1 https://example.com
   ```

4. **Output Example:**
   ```plaintext
   https://example.com [200 OK]
     Technologies Detected:
       Apache/2.4.6
       PHP/7.4.16
       HTML5
       Bootstrap/4.5.0
       jQuery/3.5.1
       Lightbox/2.11.3
       Cookies: __session, _ga, _gid
       Country: United States
       IP Address: 93.184.216.34
       Redirect Location: /index.php
       Response Code: 200 OK
   ```

#### 📘 **Interpreting the Output**
- **Apache/2.4.6**: The web server being used.
- **PHP/7.4.16**: The PHP version.
- **HTML5, Bootstrap, jQuery, Lightbox**: Frontend technologies.
- **Cookies**: Session and tracking cookies.
- **Country**: The geographical location of the server.
- **IP Address**: The server’s IP address.
- **Redirect Location**: Where the user is redirected.
- **Response Code**: HTTP status code indicating success.

---

### 📝 **Enhanced Output with Verbose Mode**

#### 📘 **Verbose Option**
To get a more readable and detailed output, use the `-v` option:
```bash
$ whatweb -a 1 -v https://example.com
```

#### 📝 **Example Output with Verbose:**
```plaintext
https://example.com [200 OK]
  Apache/2.4.6 (Description: Apache HTTP Server)
  PHP/7.4.16 (Description: PHP is a widely-used general-purpose scripting language)
  HTML5 (Description: HTML5 is the fifth and current major version of the HTML standard)
  Bootstrap/4.5.0 (Description: Bootstrap is a free and open-source CSS framework)
  jQuery/3.5.1 (Description: jQuery is a fast, small, and feature-rich JavaScript library)
  Lightbox/2.11.3 (Description: Lightbox is a popular JavaScript lightbox script)
  Cookies: __session, _ga, _gid (Description: Session and tracking cookies)
  Country: United States (Description: The geographical location of the server)
  IP Address: 93.184.216.34 (Description: The server’s IP address)
  Redirect Location: /index.php (Description: Where the user is redirected)
  Response Code: 200 OK (Description: HTTP status code indicating success)
```

#### 📘 **Advantages of Verbose Mode**
- **Clear Descriptions:** Each detected technology comes with a description.
- **Ease of Understanding:** Simplifies the interpretation of the output.

---

### 📝 **Key Takeaways**

- **Stealthy Scan:** The default mode that requires minimal interaction and is safe to use on any website.
- **Verbose Output:** Enhances readability and provides detailed descriptions of detected technologies.
- **Aggression Levels:** Choose the appropriate level based on the context and permissions.

---

### 🧪 **Hands-On Practice: Try It Yourself**

1. **Choose a Website:**
   - Select a website to scan, e.g., `https://example.com`.

2. **Run Stealthy Scan:**
   ```bash
   $ whatweb -a 1 https://example.com
   ```

3. **Enhance with Verbose Mode:**
   ```bash
   $ whatweb -a 1 -v https://example.com
   ```

4. **Analyze the Results:**
   - Review the output to understand the technologies used by the website.
   - Note any potential vulnerabilities or interesting findings.

---

### 📖 **Next Steps**
In the next episode, we will delve deeper into WhatWeb by exploring more aggressive scan modes and experimenting with different options:
[3. Aggressive Website Technology Discovering on IP Range](3-Aggressive-Website-Technology-Discovering-on-IP-Range.md)

[Previous Episode](1-Obtaining-IP-Address-and-Physical-Address-Using-Whois.md)

