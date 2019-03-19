import ecdsa

# put the hex of your public key in the line below
vk_string = "66a8b0f8335f83b324d264750f24c90e62bbe8ac5b9d01df5915c450af2651b4440086073a1891186148a719239156716648784ecc76d3c6319efc86082de680"
vk = ecdsa.VerifyingKey.from_string(bytes.fromhex(vk_string), ecdsa.SECP256k1)

# the generation signature is 9737957703d4eb54efdff91e15343266123c5f15aaf033292c9903015af817f1
message = b'Hello world'

# put your signature for Hello World in the line below
sig_hex = "1e6737f815f186ef2acea73ef439a259426fda205ee292cca248863d5ec080c4ff896fbbfb7d6388317a8cdaf58ec4d6b38a307221563fc796c1491c75e74fd9"
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
