from jsonpatch import apply_patch as patch
import sys
import json


with open('OCDS/release-schema.json') as content:
    standart = json.load(content)
with open('extension.json') as content:
    extension = json.load(content)

name = sys.argv[1]

res = patch(standart, extension)

with open('Patched/{}.json'.format(name), 'w') as outfile:
    json.dump(res, outfile, indent=4)
with open('Patches/{}.json'.format(name), 'w') as outfile:
    json.dump(extension, outfile,indent=4)
