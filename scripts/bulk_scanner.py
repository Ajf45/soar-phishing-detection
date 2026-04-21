import os
from scripts.email_parser import parse_email
from scripts.analyzer import analyze_email
from scripts.playbook_engine import apply_playbook

def scan_bulk(folder_path):
    results = []

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        parsed = parse_email(file_path)
        analysis = analyze_email(parsed)
        decision = apply_playbook(analysis["score"])

        result = {
            "file": file,
            **analysis,
            **decision
        }

        results.append(result)
    
    return results