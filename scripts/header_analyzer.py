def analyze_headers(email_content):
    findings = []

    lines = email_content.split("\n")

    for line in lines:
        if "Received:" in line and "unknown" in line:
            findings.append("Suspicious Recieved header")

        if "spf=fail" in line.lower():
            findings.append("SPF failure deected")

        if "dkim=fail" in line.lower():
            findings.append("DKIM failure detected")

    return findings

