from scripts.email_parser import parse_email
from scripts.analyzer import analyze_email
from scripts.playbook_engine import apply_playbook
from scripts.responder import respond
from scripts.report_generator import generate_report
from scripts.bulk_scanner import scan_bulk
from config.logger import logger

import sys

def run_single():
    file_path = "data/sample_emails/phishing_email.txt"

    logger.info(f"Starting single email scan: {file_path}")

    parsed = parse_email(file_path)
    analysis = analyze_email(parsed)
    decision = apply_playbook(analysis["score"])
    response = respond(decision)

    final_result = {
        "file": file_path,
        **analysis,
        **decision,
        "response": response
    }

    logger.info(f"Analysis complete: Score={analysis['score']}, Severity={decision['severity']}")
    logger.info(f"Action taken: {decision['action']}")

    generate_report(final_result)

    logger.info("Report generated succesfully")

    print("Single Email Scan Completed")

def run_bulk():
    logger.info("Starting bulk email scan")

    results = scan_bulk("data/sample_emails")

    for res in results:
        logger.info(f"File: {res['file']} | Score: {res['score']} | Severity: {res['severity']}")


    if results:
        generate_report(results[0])
        logger.info("Report generated for first alert")

    logger.info("Bulk Scan completed")

    print("Bulk SOAR Scan Completed")


if __name__ == "__main__":
    mode = "single"

    if len(sys.argv) > 1:
        mode = sys.argv[1]

    if mode == "single":
        run_single()
    elif mode == "bulk":
        run_bulk()
    else:
        print("Invalid mode. Use: single or bulk")

