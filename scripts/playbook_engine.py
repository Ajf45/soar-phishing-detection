import json

def load_playbook():
    with open("playbooks/phishing_playbook.json") as f:
        return json.load(f)["rules"]
    

def apply_playbook(score):
    rules = load_playbook()

    for rule in rules:
        condition = rule["condition"]

        if eval(condition):
            return {
                "severity": rule["severity"],
                "action": rule["action"]
            }
        
    return {
        "severity": "Unknown",
        "action": "Manual Review"
    }
