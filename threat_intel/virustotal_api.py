import requests
import os
from config.logger import logger

API_KEY = os.getenv("VT_API_KEY")

def check_url_virustotal(url):
    endpoint = "https://www.virustotal.com/api/v3/urls"

    headers = {
        "x-apikey": API_KEY
    }

    data = {"url": url}

    response = requests.post(endpoint, headers=headers, data=data)

    if response.status_code != 200:
        logger.error("VirusTotal API request failed")
        return "unknown"
    
    analysis_url = response.json()["data"]["id"]

    report_url = f"https://www.virustotal.com/api/v3/analyses/{analysis_url}"
    report = requests.get(report_url, headers=headers).json()

    stats = report["data"]["attributes"]["stats"]

    if stats["malicious"] > 0:
        return "malicious"
    return "clean"
