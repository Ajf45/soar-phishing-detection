from config.settings import SUSPICIOUS_KEYWORDS
from config.logger import logger
from threat_intel.virustotal_api import check_url_virustotal
from scripts.header_analyzer import analyze_headers
from scripts.attachment_scanner import scan_file
import os

def analyze_email(parsed_email):
    score = 0
    findings = []

    logger.info("Starting email analysis")

    content = parsed_email["raw"].lower()

    for word in SUSPICIOUS_KEYWORDS:
        if word in content:
            score += 1
            findings.append(f"Keyword detected: {word}")

    for link in parsed_email["links"]:
        result = check_url_virustotal(link)
        if result == "malicious":
            score += 3
            findings.append(f"Malicious URL: {link}")
            logger.warning(f"Malicious URL detected: {link}")

    header_findings = analyze_headers(parsed_email["raw"])
    for f in header_findings:
        score += 1
        findings.append(f)

    attachment_folder = "data/attachments"

    if os.path.exists(attachment_folder):
        for file in os.listdir(attachment_folder):
            file_path = os.path.join(attachment_folder, file)
            result = scan_file(file_path)

            if result == "malicious":
                score += 5
                findings.append(f"Malicious attachment: {file}")

    return {
        "score": score,
        "findings": findings
    }
