import json

def load_signatures(file_path="signatures.json"):
    """Load known malicious patterns from a file."""
    with open("C:\\Users\\devah\\Desktop\\PythonPrograms\\IDS\\src\\signatures.json", "r") as file:
        return json.load(file)

def check_signatures(packet, signatures):
    """Check if a packet matches any known signatures."""
    if packet["source"] in signatures.get("malicious_ips", []):
        return f"Malicious IP detected: {packet['source']}"
    return None
