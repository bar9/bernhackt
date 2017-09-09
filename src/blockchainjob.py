#!/usr/bin/env python

" run with: ./blockchainjob.py ../demo_data/ "

import os
import sys
import hashlib
from web3 import Web3, HTTPProvider, IPCProvider
from ethereum.transactions import Transaction
import rlp

def process(folder_path):
	web3 = Web3(HTTPProvider('http://localhost:8545'))
	
	for file in os.listdir(folder_path):
		current = os.path.join(folder_path, file)
		if os.path.isfile(current):
			print 'Processing: {}'.format(current)
			process_file(current, web3)

def process_file(file, web3):
	if should_store_hash_in_blockchain(file):
		hash = get_hash(file)
		store_hash_in_blockchain(hash, web3)

def should_store_hash_in_blockchain(file):
	return True

def store_hash_in_blockchain(hash, web3):
	print 'Storing hash: {}'.format(hash)
	print 'Current block height: {}'.format(web3.eth.blockNumber)
	
	address_from = '0x4f7696940Cfe0C75c830da07435e65e5ebb610B0' # account
	address_to = '0x85043213AFbA0eccd37F29DE0BB760b42EBd5d58'
	private_key = '0c6ae2768077764b1c1ed3e6b52a2df64f01fd465a450b0a1a989ffbbbaecaac'
	data = ' '.join(format(x, 'b') for x in bytearray(hash))
	
	tx = Transaction(
	nonce=web3.eth.getTransactionCount(address_from),
	gasprice=42000, #web3.eth.gasPrice
	startgas=30000,
	to='0x85043213AFbA0eccd37F29DE0BB760b42EBd5d58',
	value=0.1,
	data=b' ',
	)
	tx.sign(private_key)
	raw_tx = rlp.encode(tx)
	raw_tx_hex = web3.toHex(raw_tx)
	result = web3.eth.sendRawTransaction(raw_tx_hex)
	print result


def get_hash(file):
	data = open(file, "rb")
	data_string = data.read()
	hash = hashlib.sha256(data_string).hexdigest()
	print 'Hash: {}'.format(hash)
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
