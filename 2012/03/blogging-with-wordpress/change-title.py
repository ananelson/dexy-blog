import json
import sys

filename = sys.argv[1]

with open(filename, "rb") as f:
    data = json.load(f)

data['title'] = sys.argv[2]
data['categories'] = ["Dexy"]

with open(filename, "wb") as f:
    json.dump(data, f, sort_keys=True, indent=4)
