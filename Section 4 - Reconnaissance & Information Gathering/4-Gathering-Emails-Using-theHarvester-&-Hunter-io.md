# 📚 **Gathering Emails Using theHarvester & Hunter.io**

---

## 📝 **Overview**
In this episode, we explore how to gather email addresses for a specific company or domain. Email addresses can be invaluable for various purposes, such as spear-phishing attacks, brute-forcing user accounts, or social engineering. Since emails are public information, we can legally test this process on any domain. We will cover two methods: using the **Harvester** tool and the **Hunter.io** website.

---

### 📝 **Why Gather Emails?**
Email addresses are often the weakest link in cybersecurity. If you can gather email addresses of employees within a company, you can:
- Conduct **spear-phishing** attacks.
- Use emails in **brute-force attacks** to guess passwords.
- Gain insights into organizational structures and roles.

---

### 🛠️ **Tools Used**
- **Harvester**: A tool installed in Kali Linux for harvesting subdomains, hosts, and emails.
- **Hunter.io**: A website offering both free and paid plans to gather email addresses.

---

### 🧪 **Using theHarvester**

#### 📘 **Introduction to theHarvester**
TheHarvester is a tool that collects subdomains, emails, hosts, and virtual hosts from different public sources. It is pre-installed in Kali Linux.

#### 📘 **Running theHarvester**
1. **Open Terminal:**
   ```bash
   $ theHarvester
   ```
   - **Output:**
     ```
     ERROR: the following arguments are required: -d/--domain
     ```

 ![image](https://github.com/user-attachments/assets/7eab8027-5a5f-4f18-bdb9-d689e296e089)
    
2. **View Full Help Menu:**
   ```bash
   $ theHarvester --help
   ```
   - **Options:**
     - `-d` or `--domain`: Specify the domain to search.
     - `-b` or `--source`: Specify the data source (e.g., Google, Bing, LinkedIn).
     - `-l` or `--limit`: Set the number of search results to fetch.
     - `-f` or `--file`: Save the output to a file.
     - `-v` or `--verbose`: Enable verbose output.
    
  ![image](https://github.com/user-attachments/assets/e8101963-bf9d-4c58-92de-157389fafde3)

3. **Example Command:**
   ```bash
   $ theHarvester -d example.com -b all -l 500
   ```

#### 📝 **Interpreting the Output**
- **Sources Searched:**
  - LinkedIn
  - VirusTotal
  - Yahoo
  - Twitter
  - Google
  - Bing

- **Results:**
  - **Hostnames:** List of subdomains.
  - **Emails:** List of email addresses.
  - **Usernames:** List of usernames.

#### 📘 **Handling Issues with theHarvester**
- **No Results:** Sometimes theHarvester may not return any results due to changes in search engines or limitations in the data sources.
- **Retry:** Try running theHarvester again on different days or adjust the search parameters.
- **Specify Source:** Instead of using `-b all`, try specifying a single source like `-b google` to narrow down the search.

#### 📘 **Example Command with Specific Source:**
```bash
$ theHarvester -d example.com -b google -l 500
```

#### 📝 **Saving Results to a File**
To save the output to a file, use the `-f` option:
```bash
$ theHarvester -d example.com -b all -l 500 -f results.txt
```

---

### 🧪 **Using Hunter.io**

#### 📘 **Introduction to Hunter.io**
Hunter.io is a web-based tool that provides email harvesting services. It offers both free and paid plans, with the free plan allowing up to 50 searches per month.

#### 📘 **Creating an Account**
1. **Visit Hunter.io:**
   - Open your browser and navigate to [Hunter.io](https://hunter.io).
2. **Sign Up:**
   - Create a free account or sign in if you already have one.

#### 📘 **Searching for Emails**
1. **Enter Domain:**
   - In the search bar, enter the domain you want to gather emails for.
   - Click on "Find Email Addresses."
   
2. **Free Account Limitations:**
   - **First Five Results:** Emails are partially blurred.
   - **Additional Results:** Available with a paid account.
   
3. **Paid Account Benefits:**
   - **Unblurred Emails:** All emails are fully visible.
   - **More Results:** Access to a larger dataset.

#### 📝 **Example:**
- **Domain:** `example.com`
- **Search Result:**
  - **Name:** John Doe
  - **Email:** john.doe@example.com
  - **Role:** Project Advisor
  - **Source:** LinkedIn, Google, etc.

    ![image](https://github.com/user-attachments/assets/4d72cfe0-e762-4f8a-900c-20ecf442e174)


#### 📘 **Filtering Results**
- **Categories:** Filter results by department or role (e.g., IT/Engineering, Sales, Marketing).
- **Advanced Filters:** Customize filters to refine search results.

#### 📘 **Subscription Plans**
- **Free Plan:**
  - 50 searches per month.
  - Limited results visibility.
- **Paid Plans:**
  - **1,000 Requests/Month:** ~€50/month.
  - **5,000 Requests/Month:** ~€150/month.
  - **10,000 Requests/Month:** ~€250/month.

---

### 📝 **Best Practices**

#### 📘 **Combining Both Methods**
- **theHarvester:** Quick and easy for initial reconnaissance.
- **Hunter.io:** More reliable and provides unblurred results with advanced filtering.

#### 📘 **Ethical Considerations**
- Always ensure you have **explicit permission** to gather and use email addresses.
- Respect privacy and data protection laws.

---

### 📝 **Next Steps**
Continue to the next episode to learn how to install additional tools for information gathering. Stay tuned for more advanced techniques and practical applications!

[Next Episode: Installing Additional Tools for Information Gathering](5-How-To-Download-Tools-Online.md)

[Previous Episode: Aggressive Website Technology Discovering on IP Range](3-Aggressive-Website-Technology-Discovering-on-IP-Range.md)


