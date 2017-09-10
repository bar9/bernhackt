#!/usr/bin/env python3

" run with: ./script_sceleton.py abcd "

import sys

def process(console_input):
	try:
		print("ABCD")
	except KeyboardInterrupt:
		# Don't allow a keyboard interrupt to ensure a good state, regardless of any errors
		pass

def run():
	from sys import argv, stdout

	if len(argv) < 2:
		print("Invalid Arguments. Expected <input1>")
		sys.exit(1)

	console_input = argv[1] # input 1
	if not console_input:
		print("Invalid Arguments. Expected <input1>")

	process(console_input)

if __name__ == '__main__':
	run()
