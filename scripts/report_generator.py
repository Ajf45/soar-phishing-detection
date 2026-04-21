import json

def generate_report(result):
    with open("reports/incident.json", "w") as f:
        json.dump(result, f, indent=4)

    html = f"""
    <h1>Phishing Analysis Report</h1>
    <p>Score: {result['score']}</p>
    <p>Severity: {result['severity']}</p>
    <p>Action: {result['action']}</p>
    """

    with open("reports/incident.html", "w") as f:
        f.write(html)
