import hashlib
import requests
import os
from config.logger import logger

API_KEY = os.getenv("VT_API_KEY")

def get_file_hash(file_path):
    with open(file_path, "rb") as f:
        file_hash = hashlib.sha256(f.read()).hexdigest()
    return file_hash

def scan_file(file_path):
    logger.info(f"Scanning attachment: {file_path}")

    file_hash = get_file_hash(file_path)

    url = f"https://www.virustotal.com/api/v3/files/{file_hash}"
    headers = {"x-apikey": API_KEY}

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        logger.error(f"VirusTotal API failed for file: {file_path}")
        return "unkown"
    
    stats = response.json()["data"]["attributes"]["last_analysis_stats"]

    if stats["malicious"] > 0:
        logger.warning(f"Malicious file detected: {file_path}")
        return "malicious"
    
    logger.info(f"File clean: {file_path}")
    return "clean"

