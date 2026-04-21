def parse_email(file_path):
    with open(file_path, "r") as f:
        content = f.read()

    return {
        "raw": content,
        "links": extract_links(content)
    }

def extract_links(text):
    words = text.split()
    links = [w for w in words if w.startswith("http")]
    return links

