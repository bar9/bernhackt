#!/usr/bin/env python

" run with: ./blockchainjob.py ../demo_data/ "

import os
import sys
import hashlib
from web3 import Web3, HTTPProvider, IPCProvider
from ethereum.transactions import Transaction
import rlp
import binascii
import time 

def process(folder_path):
	web3 = Web3(HTTPProvider('http://localhost:8545'))
	
	for file in os.listdir(folder_path):
		current = os.path.join(folder_path, file)
		if os.path.isfile(current):						
			process_file(current, web3)

def process_file(file, web3):
	# DEMO: We only process 1 file
	if not (file == '../demo_data/Excel1.xls'):
		return False
	
	print 'Processing: {}'.format(file)

	hash = get_hash(file)

	tx_hash = None

	if should_store_hash_in_blockchain(file):
		tx_hash = store_hash_in_blockchain(hash, web3)
		set_tx_hash(file, tx_hash)
	
	if should_compare_hash(file):
		#tx_hash = get_tx_hash(file)
		print 'Waiting for confirmation'
		# Wait for confirmation
		time.sleep(20) 

		compare_hash_in_blockchain(hash, tx_hash, web3)

def should_store_hash_in_blockchain(file):
	# TODO check file metadata
	return True
	
def should_compare_hash(file):
	# TODO check file metadata
	return True

def store_hash_in_blockchain(hash, web3):
	print 'Storing hash: {}'.format(hash)
	print 'Current block height: {}'.format(web3.eth.blockNumber)
	
	address_from = '0x4f7696940Cfe0C75c830da07435e65e5ebb610B0' # our sending account
	address_to = '0x85043213AFbA0eccd37F29DE0BB760b42EBd5d58' # our receving account
	private_key = '0c6ae2768077764b1c1ed3e6b52a2df64f01fd465a450b0a1a989ffbbbaecaac' # sending accounts private key
	data = ' '.join(format(x, 'b') for x in bytearray(hash))

	print 'Current balance: {}'.format(web3.eth.getBalance(address_from))

	tx = Transaction(
	nonce=web3.eth.getTransactionCount(address_from),
	gasprice=web3.eth.gasPrice,
	startgas=1000000,
	to=address_to,
	value=12345,
	data=data,
	)
	tx.sign(private_key)
	raw_tx = rlp.encode(tx)
	raw_tx_hex = web3.toHex(raw_tx)

	result = None
	try:
		result = web3.eth.sendRawTransaction(raw_tx_hex)
	except:
		# TODO proper error handling
		print "Something went wrong."
	
	print 'Transaction: {} -> Hash stored in blockchain'.format(result)
	
	return result

def compare_hash_in_blockchain(hash, tx_hash, web3):
	tx = web3.eth.getTransaction(tx_hash)

	if not tx:
		print 'Transaction: {} -> Not found in blockchain'.format(tx_hash)
		return False
		
	data = tx.get('input')
		
	binary = Web3.toUtf8(data)
	
	hash_decoded = decode_binary_string(binary.replace(" ", ""))

	print 'Transaction: {} -> Hash retrieved from blockchain'.format(tx_hash)
	print 'Hash: {}'.format(hash_decoded)
		
	return True

def decode_binary_string(s):
	return int(s, 2)
	#return chr(int(s[:8], 2))
	#return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))

def get_hash(file):
	data = open(file, "rb")
	data_string = data.read()
	hash = hashlib.sha256(data_string).hexdigest()
	print 'Hash: {}'.format(hash)
	return hash

def get_tx_hash(file):
	# TODO get metadata "tx_hash" from file
	return '0x7b508bd0d9e2d36c4e9bee1712a82fa80b3d2d8eda25054ecc5eadcb7f192894'
	
def set_tx_hash(file, tx_hash):
	# TODO set metadata "tx_hash" in file
	return True

def get_state(file):
	# TODO get metadata "state" from file
	return 'state'

def set_state(file, state):
	# TODO get metadata "state" from file
	return True

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
