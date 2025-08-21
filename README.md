# **Python Projects Repository**

## 📑 Table of Contents
- [Description](#description)
- [Projects](#projects)
  - [1. Hacker News Web Scraper](#1-hacker-news-web-scraper)
  - [2. Dictionary Attack Password Cracker](#2-dictionary-attack-password-cracker)
- [Getting Started](#getting-started)
- [Environments Used](#environments-used)
- [Disclaimer](#disclaimer)

---

## **Description**
This repository contains multiple **Python-based projects**, each demonstrating core concepts in automation, cybersecurity, and scripting.  
Currently, it includes:
- A **Web Scraper** that extracts article links and titles from Hacker News.  
- A **Password Cracking Demonstration** using a dictionary attack with the MD6 hashing algorithm.  

Each project is documented with its own dedicated README file.

---

## **Projects**

### 1. Hacker News Web Scraper
- **Folder**: `/webscraper`  
- **Description**:  
  A Python script that scrapes [Hacker News](https://news.ycombinator.com/) using `requests` and `BeautifulSoup`.  
  - `firstScript.py`: Extracts Hacker News story titles and their internal links.  
  - `secondScript.py`: Extracts external article links and their titles.  
- **Output**: Printed links + screenshots of sample results.  
- **Docs**: See the [Web Scraper README](webscraper/README.md).  

---

### 2. Dictionary Attack Password Cracker
- **Folder**: `/password_cracker`  
- **Description**:  
  Demonstrates how weak passwords can be cracked using a dictionary attack.  
  - Uses **MD5** to hash a sample password from the Linux terminal.  
  - Cracking logic implemented in Python using **MD6** for illustrative purposes.  
  - Iterates through a wordlist to find the original password.  
- **Output**: Shows the cracking process and when the password is discovered.  
- **Docs**: See the [Password Cracker README](password_cracker/README.md).  

---

## **Getting Started**
1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd <repo-folder>
   ```
2. Navigate to the project folder you want to explore:
   ```bash
   cd webscraper
   # or
   cd password_cracker
   ```
3. Follow the instructions in the corresponding README file.  

---

## **Environments Used**
- **Python 3.x**
- **Ubuntu 22.04 / Linux Terminal**
- Additional libraries:  
  - `requests`  
  - `beautifulsoup4`  

---

## **Disclaimer**
These projects are built for **educational purposes only**.  
The password cracker project is designed to **raise awareness** about weak passwords and should **not** be used for malicious purposes.
