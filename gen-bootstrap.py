#!/usr/bin/python

import sys
import hashlib
import os
import json

line = sys.stdin.read().strip()

def hashFile(fileName):
	with open(fileName, 'rb') as f:
		contents = f.read()
		return hashlib.sha256(contents).hexdigest()

files = {}
for path in line.split(':'):
	fname = os.path.basename(path)
	files[fname] = hashFile(path)

with open('bootstrap.template.json', 'r') as f:
	bootstrap = json.load(f)

bootstrap['dependencyHashes'] = files
print json.dumps(bootstrap, indent=4, sort_keys=True)

