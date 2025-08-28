# **Python Projects Repository**

## 📑 Table of Contents
- [Description](#description)
- [Projects](#projects)
  - [1. Hacker News Web Scraper](#1-hacker-news-web-scraper)
  - [2. Dictionary Attack Password Cracker](#2-dictionary-attack-password-cracker)
  - [3. Real-time Network Traffic Analysis Dashboard](#3-real-time-network-traffic-analysis-dashboard)
- [Getting Started](#getting-started)
- [Environments Used](#environments-used)
- [Disclaimer](#disclaimer)

---

## **Description**
This repository contains multiple **Python-based projects**, each demonstrating core concepts in automation, cybersecurity, and scripting.  
Currently, it includes:
- A **Web Scraper** that extracts article links and titles from Hacker News.  
- A **Password Cracking Demonstration** using a dictionary attack with the MD6 hashing algorithm.  
- A **Real-time Network Traffic Dashboard** built with Scapy, Streamlit, and Plotly for packet analysis and visualization.  

Each project is documented with its own dedicated README file.

---

## **Projects**

### 1. Real-time Network Traffic Analysis Dashboard
- **Folder**: `/Network Traffic Dashboard`  
- **Description**:  
  A **Streamlit-powered web dashboard** for **real-time packet sniffing and visualization**.  
  - Uses **Scapy** to capture live network traffic.  
  - Converts raw packet data into structured tables with **Pandas**.  
  - Displays protocol distribution, packet rates, and top source IPs using **Plotly**.  
  - Includes interactive charts, live metrics, and recent packet logs.  
- **Output**: Interactive dashboard + screenshots of traffic scenarios (ping, nmap, proxychains).  
- **Docs**: See the [Traffic Dashboard README](Network Traffic Dashboard/README.md).  

### 2. Hacker News Web Scraper
- **Folder**: `/webscraper`  
- **Description**:  
  A Python script that scrapes [Hacker News](https://news.ycombinator.com/) using `requests` and `BeautifulSoup`.  
  - `firstScript.py`: Extracts Hacker News story titles and their internal links.  
  - `secondScript.py`: Extracts external article links and their titles.  
- **Output**: Printed links + screenshots of sample results.  
- **Docs**: See the [Web Scraper README](webscraper/README.md).  

---

### 3. Dictionary Attack Password Cracker
- **Folder**: `/password_cracker`  
- **Description**:  
  Demonstrates how weak passwords can be cracked using a dictionary attack.  
  - Uses **MD5** to hash a sample password from the Linux terminal.  
  - Cracking logic implemented in Python using **MD6** for illustrative purposes.  
  - Iterates through a wordlist to find the original password.  
- **Output**: Shows the cracking process and when the password is discovered.  
- **Docs**: See the [Password Cracker README](password_cracker/README.md).  

---


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
   # or
   cd network-traffic-dashboard
   ```
3. Follow the instructions in the corresponding README file.  

---

## **Environments Used**
- **Python 3.x**
- **Ubuntu 22.04 / Kali Linux**
- Additional libraries:  
  - `requests`  
  - `beautifulsoup4`  
  - `scapy`  
  - `streamlit`  
  - `plotly`  
  - `pandas`  

---

## **Disclaimer**
These projects are built for **educational purposes only**.  
The password cracker project is designed to **raise awareness** about weak passwords and should **not** be used for malicious purposes.  
The traffic analysis dashboard is intended for **local lab environments** and not for unauthorized monitoring.  
