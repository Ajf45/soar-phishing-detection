#  SOAR Phishing Detection & Response System

##  Overview

This project is a **Security Orchestration, Automation, and Response (SOAR)** system designed to detect and respond to phishing emails using automated playbooks, threat intelligence, and real-time logging.

It simulates real-world **SOC (Security Operations Center)** workflows including alert triage, enrichment, decision-making, and incident reporting.

---

##  Key Features

### 🔹 SOAR Automation

* Automated phishing detection using rule-based playbooks
* Severity classification (Low / Medium / High)
* Automated response actions (Escalate, Quarantine, Mark Safe)

### 🔹 Threat Intelligence Integration

* Integration with **VirusTotal API** for URL and file reputation
* Detection of malicious links and attachments
* Enrichment of alerts with external intelligence

### 🔹 Email Analysis Engine

* Keyword-based phishing detection
* Email header analysis (SPF/DKIM failure detection)
* URL extraction and validation
* Attachment scanning using file hash reputation

### 🔹 Bulk Email Processing

* Scan multiple emails simultaneously
* Simulates enterprise-scale phishing detection workflows

### 🔹 Logging System (SOC Audit Logs)

* Structured logging using Python logging module
* Tracks:

  * Alert generation
  * Detection results
  * API failures
  * Analyst decisions
* Supports real-time monitoring using:

  ```bash
  tail -f logs/soc.log
  ```

### 🔹 Flask Dashboard

* Web-based dashboard to visualize alerts
* Displays:

  * Severity
  * Actions
  * Detection results
* Simple SOC-style interface


---

##  Tech Stack

* **Language:** Python
* **Framework:** Flask
* **APIs:** VirusTotal
* **Libraries:** requests, logging
* **Concepts:** SOAR, Threat Intelligence, Email Security, Automation

---

##  Project Structure

```
soar-phishing-detection/
│
├── data/
├── scripts/
├── threat_intel/
├── playbooks/
├── reports/
├── logs/
├── templates/
├── config/
│
├── main.py
├── app.py
├── requirements.txt
└── README.md
```

---

##  Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/Ajf45/soar-phishing-detection
cd soar-phishing-detection
```

### 2. Install Dependencies

```bash
pip3 install -r requirements.txt
```

### 3. Set API Key

```bash
export VT_API_KEY="your_api_key_here"
```

---

## ▶️ Usage

### 🔹 Run Single Email Scan

```bash
python3 main.py single
```

### 🔹 Run Bulk Scan

```bash
python3 main.py bulk
```

### 🔹 Launch Dashboard

```bash
python3 app.py
```

---

##  Sample Output

* JSON Report → `reports/incident.json`
* HTML Report → `reports/incident.html`
* Logs → `logs/soc.log`

---

##  Learning Outcomes

* Hands-on experience with **SOAR workflows**
* Understanding of **phishing detection techniques**
* Integration of **threat intelligence APIs**
* Implementation of **SOC logging and monitoring systems**

---

##  Future Improvements

* MITRE ATT&CK mapping
* SIEM integration (ELK Stack)
* Real-time alert correlation


---

##  Author

Raunak Jain
Cybersecurity Enthusiast | SOC Analyst Aspirant
