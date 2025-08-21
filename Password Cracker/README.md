# **Dictionary Attack Password Cracker using MD6**

## **Description**
This project demonstrates how to crack hashed passwords using a dictionary attack approach. A hash is generated using a simple password and compared against a wordlist of common passwords. The MD6 hashing algorithm is used in the script to illustrate how the process works. While the hash used in this example is generated using MD5, MD6 is applied in the cracking logic for demonstration purposes.

## **Languages and Utilities Used**
- **Python**: Used to implement the cracking logic.
- **MD6 Hashing Algorithm**: Used to simulate hashing comparison in the script.
- **MD5 (via terminal)**: Used to initially hash a known password.
- **Linux Shell (echo + md5sum)**: To create the hashed password.
- **Custom Dictionary File**: Contains sample passwords used during the attack.

## **Environments Used**
- **Ubuntu 22.04** (or any Linux distro with terminal access and Python3).

---

## **Hashing the Password**
To begin, a password was hashed using the MD5 hashing algorithm from the command line:

**Result:**

<p align="center">
<img src="https://imgur.com/bNH7wWI.png" width="70%" alt="Hashing with md5sum"/>
</p>

---

## **Cracking Script**

The generated hash was inserted into the cracking script. The script uses MD6 to hash each word from the dictionary and compares it against the given hash.

**Dictionary**

<p align="center">
<img src="https://imgur.com/4UUIQNi.png" width="70%" alt="Hashing with md5sum"/>
</p>

**Code Preview:**

<p align="center">
<img src="https://imgur.com/P3yKJv3.png" width="70%" alt="Python Script"/>
</p>

---

## **Running the Attack**

Once executed, the script iterates over the wordlist and finds the correct password matching the given hash.

**Result:**

<p align="center">
<img src="https://imgur.com/Cx2MvaU.png" width="70%" alt="Password Found"/>
</p>

---

## **Disclaimer**
This project is strictly for **educational purposes only**. It highlights the importance of using strong, unpredictable passwords and shows how easily weak passwords can be cracked using dictionary attacks.

---
