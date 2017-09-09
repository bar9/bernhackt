#!/usr/bin/env python

" run with: ./blockchainjob.py ../demo_data/ "

import os
import sys
import hashlib

def process(folder_path):
	for file in os.listdir(folder_path):
		current = os.path.join(folder_path, file)
		if os.path.isfile(current):
			print 'Processing: {}'.format(current)
			process_file(current)

def process_file(file):
	hash = get_hash(file)


def get_hash(file):
	data = open(file, "rb")
	data_string = data.read()
	hash = hashlib.sha256(data_string).hexdigest()
	print 'Hash: {}\n'.format(hash)
	return hash

def run():
	from sys import argv, stdout

	if len(argv) < 2:
		print("Invalid Arguments. Expected <folder_path>")
		sys.exit(1)

	folder_path = argv[1] # input 1
	if not folder_path:
		print("Invalid Arguments. Expected <folder_path>")

	process(folder_path)

if __name__ == '__main__':
	run()
