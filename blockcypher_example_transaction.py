import blockcypher

# Specify the inputs and outputs below
# For convenince you can specify an address, and the backend will work out what transaction output that address has
# available to spend
# You do not need to list a change address, by default the transaction will be created with all change (minus the fees)
# going to the first input address
my_address = blockcypher.generate_new_address(coin_symbol='btc-testnet', api_key= 'c1058641898a467a9420f9cbc5dadb8d')
print(my_address)
public_key = '02959a51eeaa136301d83ee32da7362be53a2c3a852ff2e495b8e48dae25303cf2'
address = 'n4XfdsqqgBqZ7nB9AuGn2ARsYnK8DHPTDg'
private_key = '665be878a4d16043131d792883221d2be5584b0353e9e837c658754015550db8'
wif = 'cR1g4EZiRfabu3K9P13GupcB2ALZL6zBBDCcBCR9ZgFbxW7ANYr2'
inputs = [{'address': ''}]
outputs = [{'address': '', 'value': 100}]
# The next line creates the transaction shell, which is as yet unsigned
unsigned_tx = blockcypher.create_unsigned_tx(inputs=inputs, outputs=outputs, coin_symbol='btc-testnet', api_key='c1058641898a467a9420f9cbc5dadb8d')

# You can edit the transaction fields at this stage, before signing it.


# Now list the private and public keys corresponding to the inputs
private_keys=['323...']
public_keys=['03bc']
# Next create the signatures
tx_signatures = blockcypher.make_tx_signatures(txs_to_sign=unsigned_tx['tosign'], privkey_list=private_keys, pubkey_list=public_keys)
# Finally push the transaction and signatures onto the network
blockcypher.broadcast_signed_transaction(unsigned_tx=unsigned_tx, signatures=tx_signatures, pubkeys=public_keys, coin_symbol='btc-testnet', api_key='d62...')
