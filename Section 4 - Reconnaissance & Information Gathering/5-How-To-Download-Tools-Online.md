# 📚 **How To Download Tools Online**

---

## 📝 **Overview**
In this episode, we explore how to download and install tools for information gathering from online repositories, specifically from GitHub. This is crucial for ensuring you have access to the latest and most effective tools for your penetration testing tasks. We will walk through the process of finding, downloading, and installing a tool using GitHub.

---

### 🛠️ **Why Download Tools Online?**
- **Tool Updates:** Tools may become outdated or stop working. Regularly downloading new versions ensures reliability.
- **Customization:** Many tools are customizable to suit specific needs.
- **Community Support:** GitHub hosts a vast community of developers who contribute and maintain tools.

---

### 🧪 **Finding Tools on GitHub**

#### 📘 **Navigating GitHub**
1. **Open Firefox:**
   - Navigate to [GitHub](https://github.com).

2. **Search for Tools:**
   - **Known Tools:** If you know the name of the tool, search directly.
   - **Unknown Tools:** If you are unsure, search for generic terms like "information gathering tools."

#### 📘 **Example Search:**
- **Search Query:** "information gathering tools GitHub"
- **Result:** A list of repositories related to information gathering tools.

#### 📘 **Selecting a Tool:**
- **Red Hawk Example:**
  - **Description:** All-in-one tool for information gathering, scanning, and crawling.
  - **Link:** Click on the repository link to access the tool's page.

---

### 🧪 **Downloading Tools from GitHub**

#### 📘 **Cloning a Repository**
1. **Copy the Repository Link:**
   - On the tool's GitHub page, copy the repository link.
   - Example: `https://github.com/TechnicalHub/Red-Hawk.git`

2. **Open Terminal:**
   - Navigate to the desired directory, typically `/home/<username>/Desktop`.
   - Example:
     ```bash
     cd ~/Desktop
     ```

3. **Clone the Repository:**
   - Use the `git clone` command followed by the copied link.
   - Example:
     ```bash
     git clone https://github.com/TechnicalHub/Red-Hawk.git
     ```

4. **Verify Download:**
   - Check the Desktop directory to confirm the tool has been downloaded.
   - Example:
     ```bash
     ls ~/Desktop
     ```

---

### 🧪 **Installing and Running the Tool**

#### 📘 **Identifying the Main Script**
1. **Navigate to the Tool Directory:**
   - Open the cloned directory.
   - Example:
     ```bash
     cd Red-Hawk
     ```

2. **List Files:**
   - View the contents of the directory.
   - Example:
     ```bash
     ls
     ```

3. **Identify the Main Script:**
   - Look for the main executable file, often named after the tool.
   - Example: `Red_Hawk.php`

#### 📘 **Running the Tool**
1. **Check File Type:**
   - Determine the file type (e.g., PHP, Python) to know the appropriate interpreter.
   - Example: `Red_Hawk.php` is a PHP file.

2. **Execute the Tool:**
   - Run the tool using the appropriate interpreter.
   - Example:
     ```bash
     php Red_Hawk.php
     ```

     ![image](https://github.com/user-attachments/assets/bffc023b-d871-498d-8636-e4e0c30aff46)

#### 📘 **Handling Dependencies**
- **Missing Modules:** Some tools require additional dependencies.
- **Automatic Installation:** Some tools provide scripts to install missing dependencies.
  - Example:
    ```bash
    ./fix
    ```

3. **Restart the Tool:**
   - After installing dependencies, restart the tool.
   - Example:
     ```bash
     php Red_Hawk.php
     ```

---

### 🧪 **Testing the Tool**

#### 📘 **Basic Reconnaissance:**
1. **Input Target:**
   - Enter the domain or IP address you wish to scan.
   - Example: `google.com`

2. **Select Protocol:**
   - Choose between HTTP and HTTPS.
   - Example: Enter `2` for HTTPS.

3. **Run Basic Recon:**
   - Select the basic reconnaissance option.
   - Example: Enter `0` for basic recon.

4. **Review Output:**
   - Examine the output for useful information.
   - Example:
     - Site Title: Google
     - IP Address: 172.217.169.206
     - Web Server: Apache
     - Cloudflare Detection: True
    
   ![image](https://github.com/user-attachments/assets/0c9d776b-41ad-4dc9-b121-c44f57225d9f)


#### 📘 **Advanced Features:**
- **Whois Lookup:** Retrieve domain registration information.
- **Geo-IP Lookup:** Obtain geographical coordinates.
- **DNS Lookup:** Discover DNS servers.
  
  ![image](https://github.com/user-attachments/assets/0c612d1c-3863-4567-bac9-39d0464a6c76)

- **Nmap Port Scan:** Identify open ports (covered later).
  

---

### 📝 **Troubleshooting**
- **Stuck at Cloudflare:** Some tools may struggle with Cloudflare-protected sites.
- **Missing Dependencies:** Ensure all required dependencies are installed.
- **Tool Bugs:** Report bugs to the tool's GitHub repository for fixes.

---

### 📝 **Next Steps**
Continue to the next episode to download and run another tool called **Sherlock**. Sherlock is used to discover different accounts on various platforms based on specified usernames. Follow the same process to find, download, and install Sherlock, and test its functionality.

[Next Episode: Downloading and Running Sherlock](6-Finding-Usernames-With-Sherlock.md
)

[Previous Episode: Gathering Emails Using theHarvester & Hunter.io](4-Gathering-Emails-Using-theHarvester-&-Hunter-io.md)

---
