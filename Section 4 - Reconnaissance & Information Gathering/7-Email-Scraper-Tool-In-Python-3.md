# 📚 **Email Scraper Tool In Python 3**

---

## 📝 **Overview**
In this bonus episode, we introduce a custom **Email Scraper Tool** built using Python 3. This tool is designed to extract email addresses from a specified domain by scraping HTML content and following links to find more emails. We will walk through the code, demonstrate how to run it, and compare its effectiveness against other tools like Harvester and Hunter.io.

---

### 🛠️ **Code Explanation**

Here is the complete code for the **email-scarper.py** tool:

```python
from bs4 import BeautifulSoup
import requests
import requests.exceptions
import urllib.parse
from collections import deque
import re

user_url = str(input('[+] Enter Target URL To Scan: '))
urls = deque([user_url])
scraped_urls = set()
emails = set()
count = 0

try:
    while len(urls):
        count += 1
        if count == 100:
            break
        url = urls.popleft()
        scraped_urls.add(url)
        parts = urllib.parse.urlsplit(url)
        base_url = '{0.scheme}://{0.netloc}'.format(parts)
        path = url[:url.rfind('/')+1] if '/' in parts.path else url
        print('[%d] Processing %s' % (count, url))

        try:
            response = requests.get(url)
        except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
            continue

        new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", response.text, re.I))
        emails.update(new_emails)
        soup = BeautifulSoup(response.text, features="lxml")

        for anchor in soup.find_all("a"):
            link = anchor.attrs['href'] if 'href' in anchor.attrs else ''
            if link.startswith('/'):
                link = base_url + link
            elif not link.startswith('http'):
                link = path + link
            if not link in urls and not link in scraped_urls:
                urls.append(link)
except KeyboardInterrupt:
    print('[-] Closing!')

for mail in emails:
    print(mail)
```

---

### 📝 **How the Tool Works**

#### 📘 **Step-by-Step Explanation**

1. **Input Target URL:**
   - Prompt the user to enter the target URL to scan.
   ```python
   user_url = str(input('[+] Enter Target URL To Scan: '))
   ```

2. **Initialize Variables:**
   - Create a queue of URLs to process (`urls`).
   - Maintain a set of URLs that have already been processed (`scraped_urls`).
   - Store extracted email addresses in a set (`emails`).
   - Track the number of URLs processed (`count`).

3. **Process URLs:**
   - While there are URLs to process, continue the loop.
   - Extract the base URL and path from the current URL.
   ```python
   parts = urllib.parse.urlsplit(url)
   base_url = '{0.scheme}://{0.netloc}'.format(parts)
   path = url[:url.rfind('/')+1] if '/' in parts.path else url
   ```

4. **Fetch Page Content:**
   - Send an HTTP GET request to the current URL.
   ```python
   try:
       response = requests.get(url)
   except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
       continue
   ```

5. **Extract Emails:**
   - Use a regular expression to find all email addresses in the page content.
   ```python
   new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", response.text, re.I))
   emails.update(new_emails)
   ```

6. **Parse Links:**
   - Parse the HTML content to find all `<a>` tags and extract their `href` attributes.
   - Normalize the links to ensure they are absolute URLs.
   ```python
   for anchor in soup.find_all("a"):
       link = anchor.attrs['href'] if 'href' in anchor.attrs else ''
       if link.startswith('/'):
           link = base_url + link
       elif not link.startswith('http'):
           link = path + link
       if not link in urls and not link in scraped_urls:
           urls.append(link)
   ```

7. **Limit the Number of URLs Processed:**
   - Stop processing after 100 URLs to prevent excessive scraping.
   ```python
   if count == 100:
       break
   ```

8. **Handle Keyboard Interrupt:**
   - Allow the user to exit the tool by pressing `Ctrl+C`.
   ```python
   except KeyboardInterrupt:
       print('[-] Closing!')
   ```

9. **Display Collected Emails:**
   - Print all unique email addresses found.
   ```python
   for mail in emails:
       print(mail)
   ```

---

### 📝 **Transcript Summary**

#### 📘 **Introduction**
- Welcome back to the bonus video.
- Introducing the **Email Scraper Tool** built with Python 3.
- This tool is part of the course materials and can be downloaded from the course repository.
- Demonstration of transferring the tool from the host desktop to the Kali Linux desktop.

#### 📘 **Tool Functionality**
- The tool prompts the user to enter a target URL.
- It scrapes the HTML content of the target URL to extract email addresses.
- It follows links found on the page to scrape additional emails.
- By default, it processes up to 100 URLs.
- Uses a regular expression to find email patterns in the HTML content.

#### 📘 **Comparison with Other Tools**
- **Harvester:** Initially yielded no results but eventually found around 10-15 unique emails.
- **Hunter.io (Free Account):** Found approximately 10 unique emails.
- **Email Scraper Tool:** Found at least 100-150 unique emails, all within the specified domain.
- **Additional Findings:** Discovered emails from unrelated domains, highlighting the importance of filtering results.

#### 📘 **Usage Instructions**
- Ensure you specify the correct protocol (HTTP or HTTPS) before the domain.
- Run the tool in the terminal:
  ```bash
  python3 email-scarper.py
  ```
- Provide the target URL when prompted.
 
---

### 📝 **Next Steps**
Continue to the next episode to explore scanning techniques and set up a vulnerable lab for hands-on practice. Stay tuned for more advanced topics and practical applications!

[Next Episode: Setting Up a Vulnerable Lab for Scanning](next-episode.md)

[Previous Episode: Finding Usernames With Sherlock](previous-episode.md)