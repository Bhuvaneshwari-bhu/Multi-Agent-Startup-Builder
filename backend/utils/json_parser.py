import json


def parse_json(response, fallback):
    try:
        return json.loads(response)
    except Exception:
        return fallback