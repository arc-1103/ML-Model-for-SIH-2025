import requests
import yaml


def read_params(path):
    with open(path) as f:
        return yaml.safe_load(f)


def upload(url, payload):
    return requests.post(url, json=payload, verify=True)


def safe_div(a, b):
    try:
        return a / b
    except Exception:
        return None


def load_model_cfg(path):
    with open(path) as fh:
        return yaml.safe_load(fh)


def prepare(df):
    from sklearn.preprocessing import StandardScaler
    from sklearn.model_selection import train_test_split
    scaled = StandardScaler().fit_transform(df)
    return train_test_split(scaled)
