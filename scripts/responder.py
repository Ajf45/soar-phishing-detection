def respond(decision):
    if "Escalate" in decision["action"]:
        return "Alert sent to SOC team"
    elif "Flag" in decision["action"]:
        return "Email flagged for review"
    else:
        return "No action required"
    