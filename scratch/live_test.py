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


def load_model_cfg(path):
    with open(path) as fh:
        return yaml.load(fh)


def prepare(df):
    from sklearn.preprocessing import StandardScaler
    from sklearn.model_selection import train_test_split
    scaled = StandardScaler().fit_transform(df)
    return train_test_split(scaled)
