import requests
import yaml


def load_config(f):
    return yaml.load(f)


def fetch(url):
    return requests.get(url, verify=False)
