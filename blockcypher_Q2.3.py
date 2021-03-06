import blockcypher

# Specify the inputs and outputs below
# For convenince you can specify an address, and the backend will work out what transaction output that address has
# available to spend
# You do not need to list a change address, by default the transaction will be created with all change (minus the fees)
# going to the first input address

# my_address = blockcypher.generate_new_address(coin_symbol='btc-testnet', api_key= 'c1058641898a467a9420f9cbc5dadb8d')
# print(my_address, "\n")

public_key = '03240133fe70e9148894512329b3dcdab63d31d39fd8d33753bd94dbe94227434e'
address = 'mo94jePN64JaJPXa87SQQqxUT1SbgKcE66'
private_key = '7d3ace1c0fae90735fe8cf8e7f4f8f10107ed980a155e1d4fbebbebb3da92fe3'
wif = 'cRn8bimx4CRkMThJq8joJ5Um9oHUPZijCDKqzF8mBZ8hqyCmPUrG'

def question2_3():
	inputs = [{'address': address}]

	# Generate my string and proof-of-burn script
	my_hex_username = "dwmr15".encode("utf-8").hex()
	# 6a=OP_RETURN, 4c=OP_PUSHDATA1, 06=pushing 6 bytes, my_hex_username=dwmr15 in hex
	my_script = '6a4c06'+my_hex_username
	print(my_script)
	outputs = [{'value': 0, 'script_type':"null-data", 'script':my_script}]

	# The next line creates the transaction shell, which is as yet unsigned
	unsigned_tx = blockcypher.create_unsigned_tx(inputs=inputs, outputs=outputs, coin_symbol='btc-testnet', api_key='c1058641898a467a9420f9cbc5dadb8d')
	print(unsigned_tx)

	# Now list the private and public keys corresponding to the inputs
	private_keys=[private_key]
	public_keys=[public_key]

	# Next create the signatures
	tx_signatures = blockcypher.make_tx_signatures(txs_to_sign=unsigned_tx['tosign'], privkey_list=private_keys, pubkey_list=public_keys)
	# Finally push the transaction and signatures onto the network
	blockcypher.broadcast_signed_transaction(unsigned_tx=unsigned_tx, signatures=tx_signatures, pubkeys=public_keys, coin_symbol='btc-testnet', api_key='c1058641898a467a9420f9cbc5dadb8d')


question2_3()
