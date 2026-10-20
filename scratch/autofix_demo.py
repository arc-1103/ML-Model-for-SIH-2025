import requests
import yaml


def load_config(f):
    return yaml.safe_load(f)


def fetch(url):
    return requests.get(url, verify=True)
