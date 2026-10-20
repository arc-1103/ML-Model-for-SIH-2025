import requests
import yaml


def read_params(path):
    with open(path) as f:
        return yaml.load(f)


def upload(url, payload):
    return requests.post(url, json=payload, verify=False)


def safe_div(a, b):
    try:
        return a / b
    except:
        return None
