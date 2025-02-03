# 📚 **Installing Vulnerable Virtual Machine**

---

## 📝 **Overview**
In this episode, we guide you through the process of setting up a **vulnerable virtual machine** that you can use for scanning and penetration testing. This virtual machine will simulate real-world scenarios, allowing you to practice ethical hacking techniques without violating ethical guidelines.

---

### 🌐 **Finding a Vulnerable Virtual Machine**

#### 🌐 **Where to Find Vulnerable VMs**
- **Top 10 Vulnerable Machines:** Search for "Top 10 Vulnerable Machines" to find resources that list the best vulnerable virtual machines for practice.
- **Rapid7 Metasploitable:** One of the most popular and widely used vulnerable virtual machines.

#### 🌐 **Downloading Metasploitable**
1. **Visit Rapid7 Metasploitable Page:**
   - Go to [Rapid7 Metasploitable](https://www.metasploitable.com/).
   - Scroll down to see the list of top 10 vulnerable machines.

2. **Download Metasploitable:**
   - Click on the **Metasploitable** link.
   - Fill out the required information to access the download page.
   - Once submitted, you will be directed to a page where you can download the virtual machine.

3. **Extract the Downloaded File:**
   - After downloading, extract the `.zip` file.
   - Inside, you will find the `.ova` file, which contains the virtual machine image.

---

### 🖥️ **Setting Up the Virtual Machine**

#### 🖥️ **Create a New Virtual Machine in VMware Workstation**
1. **Open VMware Workstation:**
   - Launch VMware Workstation on your host machine.

2. **Create a New Virtual Machine:**
   - Click on **Create a New Virtual Machine**.
   - Choose **Typical** setup.

3. **Configure VM Settings:**
   - **Name:** Give the VM a name, e.g., `Metasploitable`.
   - **Operating System:** Select **Linux** and choose **Other Linux (64-bit)**.

4. **Allocate Resources:**
   - **Memory (RAM):** Allocate **512 MB** of RAM. This is sufficient for the VM to run smoothly.
   - **Hard Disk:** Click **Use an existing virtual disk**.
     - Click **Add** and browse to the extracted `.ova` file.
     - Select the `.vmdk` file (e.g., `metasploitable.vmdk`) and click **OK**.

5. **Networking Configuration:**
   - Click **Settings**.
   - Go to the **Network Adapter** tab.
   - Change the adapter type to **Bridged Adapter**.
   - This will allow the VM to obtain an IP address from your network.

6. **Finish Setup:**
   - Click **Finish** to complete the setup.

---

### 🌐 **Starting and Logging into the VM**

#### 🌐 **Start the Virtual Machine:**
- Power on the virtual machine.
- The installation process will begin automatically.
- This may take a minute or two.

#### 🌐 **Log In:**
- Once the installation is complete, you will be prompted to log in.
- **Username:** `msfadmin`
- **Password:** `msfadmin`

#### 🌐 **Verify Network Configuration:**
- Open a terminal session.
- Run the following command to check the network configuration:
  ```bash
  ifconfig
  ```
- You should see an IP address assigned to the VM, typically in the `192.168.x.x` range.

#### 🌐 **Test Connectivity:**
- Ensure the VM can connect to the internet by pinging an external server:
  ```bash
  ping www.google.com
  ```

---

### 📝 **Post-Setup Verification**

#### 📝 **Ensure Proper Functionality:**
- **IP Address:** Confirm that the VM has a valid IP address.
- **Internet Access:** Verify that the VM can reach external servers.
- **Services:** Check for open ports and services that can be exploited.

#### 📝 **Common Services:**
- **SSH (Port 22):** Secure shell for remote access.
- **HTTP (Port 80):** Web server.
- **HTTPS (Port 443):** Secure web server.
- **FTP (Port 21):** File transfer protocol.
- **SMB (Ports 139, 445):** Windows file sharing.

---

### 📝 **Next Steps**
With the vulnerable virtual machine set up and ready, you can now proceed to the next episode to learn how to perform network scanning using tools like **Nmap**. Stay tuned for more in-depth coverage and hands-on demonstrations!

[Next Episode: Netdiscover, Discovering Hosts on a Network](03-Netdiscover.md)

[Previous Episode: TCP & UDP](01-TCP-&-UDP.md)
