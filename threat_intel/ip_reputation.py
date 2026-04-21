def check_ip(ip):
    #Mock fucntion
    suspicious_ips = ["203.0.113.45"]
    if ip in suspicious_ips:
        return "malicious"
    return "clean"

