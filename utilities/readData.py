import json
import os

def load_login_data():
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "testData", "loginData.json"))
    with open(file_path, "r") as f:
        return json.load(f)
