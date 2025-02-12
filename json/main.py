import json
file_path = "sample-data.json"
with open(file_path, "r") as file:
    fname = json.load(file)         