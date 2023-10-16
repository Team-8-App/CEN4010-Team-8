import requests

def handler (event, context):
    response = requests.get("https://api.github.com")
    res = {
        "event": event,
        "output": response.json(),
        "context": context,
    }
    print(res)
    return None
