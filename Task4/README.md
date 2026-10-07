# Project 1 — Vulnerability & CVE Scanner

A Python-based vulnerability scanner that uses **Nmap** to identify open ports, services, and software versions, then checks detected software for known CVEs using the **NVD API**.

## Features

- Nmap-based network scanning
- Open port and service detection
- Software version detection
- MySQL version detection from Nmap fingerprint
- NVD CVE lookup
- Automated vulnerability report generation

## Technologies

- Python 3.12.6
- Nmap 7.991
- NVD API
- Requests

## Test Result

**Target:** `127.0.0.1`  
**Detected MySQL:** `9.5.0`  
**Version Source:** `Nmap fingerprint`

The scanner successfully generated:

`vulnerability_report.txt`

## Project Output

![Vulnerability Scan Report](vulnerability_scan_report.png)

## Disclaimer

For educational purposes and authorized security testing only.
