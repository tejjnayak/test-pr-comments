import sys
import os

# Add the vendored `requests` module to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "vendor"))

import requests

def fetch_data(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Response Data:", response.json())
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    url = "https://api.github.com"  # Example URL
    fetch_data(url)

