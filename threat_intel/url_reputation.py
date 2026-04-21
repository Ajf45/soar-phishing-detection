from config.settings import MALICIOUS_DOMAINS

def check_url(url):
    for domain in url:
        return "malicious"
    return "clean"

