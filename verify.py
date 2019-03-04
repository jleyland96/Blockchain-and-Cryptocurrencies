import ecdsa

# put the hex of your public key in the line below
vk_string="56bab87d26a2a95f0201a3ebc15b8269a316ad7f23e483ef6324242f36ff1b5a8329a28dfc72625cffae2498d0281b37d0261b8e614c62ef00c79e7d664850fb"
vk = ecdsa.VerifyingKey.from_string(bytes.fromhex(vk_string), ecdsa.SECP256k1)

# the generation signature is 9737957703d4eb54efdff91e15343266123c5f15aaf033292c9903015af817f1
message = b'9737957703d4eb54efdff91e15343266123c5f15aaf033292c9903015af817f1'

# put your signature for Hello World in the line below
sig_hex = "28ca79f8a6ddb473a454e7004246024bff9ef7b9a5fbbedb7a25fc5761592180782a281949a944805bf485aeb5787b64dc5653e0bba8a18b802f431853708c09"
sig = bytes.fromhex(sig_hex)

print("Checking signature")
print("Message: "+str(message))

print("Signature: "+sig_hex)
print("Public key: "+vk_string)
try:
    vk.verify(sig, message)  # True
    print('Verification passed')
except ecdsa.keys.BadSignatureError:
    print('Verification failed')