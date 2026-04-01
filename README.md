# Breach-Checkr

**Breach-Checkr** is a lightweight Python command-line tool designed to check if your passwords have been leaked in data breaches. It uses the Have I Been Pwned API and maintains security through a K-anonymity model.

## How is privacy maintained?
Breach-Checkr **never** sends your actual password over the internet. 

1. The password is hashed using SHA-1.
2. Only the first 5 characters of the hash are sent to the HIBP API.
3. The API returns a list of all leaked hashes starting with those 5 characters.
4. The script locally compares the "tail" of your hash against the results to find a match.

**Your password stays 100% local.**

## Features:
* **K-Anonymity model:** Your password remains private from the API provider.
* **CLI Interface:** Fast, terminal-based, and local.
* **Secure Hashing:** Uses `hashlib` for industry-standard SHA-1 generation.

## Installation: 

### Prerequisites:
* Python 3 or later
* `requests` library

```
pip install requests
```
## How to Run:
Pass the password(s) you want to check as command-line arguments:
```
python3 breach-checkr.py yourpassword
```
##  Future Improvements:
[ ] Integration of the getpass module to hide password typing in the terminal.

## Why:
I built this to learn about k-anonymity and secure API integration in Python :)
