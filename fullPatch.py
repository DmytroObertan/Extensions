import json
import jsonpatch
import os

def open_json(path):
	with open(path) as content:
		return json.load(content)

OCDS = open_json("OCDS/release-schema.json")
for filename in os.listdir("Patches"):
	path = os.path.join("Patches", filename)
	print path
	patched = jsonpatch.apply_patch(OCDS, open_json(path))
	OCDS = patched

with open('Full/Full_schema.json', 'w') as outfile:
    json.dump(OCDS, outfile, indent=4)