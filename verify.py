import ecdsa

# put the hex of your public key in the line below
vk_string="56bab87d26a2a95f0201a3ebc15b8269a316ad7f23e483ef6324242f36ff1b5a8329a28dfc72625cffae2498d0281b37d0261b8e614c62ef00c79e7d664850fb"
vk = ecdsa.VerifyingKey.from_string(bytes.fromhex(vk_string), ecdsa.SECP256k1)

# the generation signature is 9737957703d4eb54efdff91e15343266123c5f15aaf033292c9903015af817f1
message = b'Hello World'

# put your signature for Hello World in the line below
sig_hex = "aec300825740810dc91c57ab5bfe948f07298c0d49327e91435b88b3194f5ce388dcbe6fbbd3709b093a3546c265fa70a79751a9643b62b96b0eb7ebcff8e087"
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