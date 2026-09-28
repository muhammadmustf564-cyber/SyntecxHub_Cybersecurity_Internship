import requests
from urllib.parse import urlsplit, parse_qsl, urlencode, urlunsplit

url = "http://127.0.0.1:8000/test.php?id=1"

payloads = [
    "'",
    "' OR '1'='1",
    "' OR 1=1-- ",
    "' AND 1=2-- "
]

sql_errors = [
    "sql syntax",
    "mysql",
    "database error",
    "sqlite",
    "postgresql",
    "oracle"
]

report_file = "scan_report.txt"

parts = urlsplit(url)
parameters = parse_qsl(parts.query, keep_blank_values=True)

with open(report_file, "w", encoding="utf-8") as report:

    report.write("SQL Injection Scanner Report\n")
    report.write("=" * 35 + "\n")
    report.write(f"Target: {url}\n\n")

    for parameter, original_value in parameters:

        for payload in payloads:

            new_parameters = []

            for name, value in parameters:

                if name == parameter:
                    new_parameters.append((name, payload))
                else:
                    new_parameters.append((name, value))

            new_query = urlencode(new_parameters)

            test_url = urlunsplit((
                parts.scheme,
                parts.netloc,
                parts.path,
                new_query,
                parts.fragment
            ))

            try:
                response = requests.get(test_url, timeout=5)

                print(f"Parameter: {parameter}")
                print(f"Payload: {payload}")
                print(f"Status Code: {response.status_code}")
                print(f"Response Length: {len(response.text)}")

                found = False

                for error in sql_errors:
                    if error.lower() in response.text.lower():
                        found = True
                        break

                if found:
                    print("⚠️ Possible SQL Injection detected!")

                    report.write("Possible SQL Injection Detected\n")
                    report.write(f"Parameter: {parameter}\n")
                    report.write(f"Payload: {payload}\n")
                    report.write(f"Status Code: {response.status_code}\n")
                    report.write(f"Response Length: {len(response.text)}\n")
                    report.write("-" * 35 + "\n")

                else:
                    print("No SQL error indicator detected.")

                print("-" * 40)

            except requests.RequestException as error:
                print("Request failed:", error)
                report.write(f"Request failed: {error}\n")

print(f"\nReport saved to: {report_file}")