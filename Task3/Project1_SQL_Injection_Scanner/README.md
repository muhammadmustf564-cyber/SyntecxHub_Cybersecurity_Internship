# SQL Injection Scanner

A Python-based SQL Injection Scanner created as part of Task 3 – Project 1 of the SyntexHub Cybersecurity Internship.

## Project Objective

The purpose of this project is to create a simple tool that sends SQL Injection test payloads to a web application's parameter and checks the response for common SQL error indicators.

## Features

- Tests URL parameters
- Sends common SQL Injection payloads
- Checks HTTP response status
- Checks response length
- Detects common SQL error indicators
- Saves detected findings in a report
- Uses request timeout for safer testing

## Technologies Used

- Python
- Requests Library

## Project Structure

    Project1_SQL_Injection_Scanner/
    │
    ├── sql_injection_scanner.py
    ├── test_server.py
    ├── requirements.txt
    ├── scan_report.txt
    ├── README.md
    └── .gitignore

## Installation

Install the required Python library:

    pip install -r requirements.txt

## How to Run

First start the local test server:

    python test_server.py

The server will run at:

    http://127.0.0.1:8000

Keep this terminal running.

Open another terminal and run:

    python sql_injection_scanner.py

## SQL Injection Payloads

The scanner tests several basic payloads, including:

    '
    ' OR '1'='1
    ' OR 1=1-- 
    ' AND 1=2-- 

## Detection

The scanner checks the server response for common SQL-related error indicators such as:

- SQL syntax
- MySQL
- Database Error
- SQLite
- PostgreSQL
- Oracle

If an indicator is found, the scanner displays:

    Possible SQL Injection detected!

## Report

Detected findings are automatically saved in:

    scan_report.txt

The report contains information such as:

- Target URL
- Parameter
- Payload
- HTTP status code
- Response length

## Testing Environment

This project was tested using a local Python HTTP test server.

Target:

    http://127.0.0.1:8000

The test server intentionally returns a database error message when SQL Injection-style input is received.

## Important Note

This is an educational cybersecurity project.

The scanner should only be used against systems that you own or have explicit permission to test.

Do not scan websites, servers, or applications without authorization.

## Learning Outcome

This project demonstrates basic concepts of:

- Python HTTP requests
- URL parameters
- SQL Injection testing
- Response analysis
- Error-based vulnerability indicators
- Basic cybersecurity automation