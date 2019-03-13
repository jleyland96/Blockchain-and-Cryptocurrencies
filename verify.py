import ecdsa

# put the hex of your public key in the line below
vk_string="f13d1d92e0bffcdbee0309ada8f882572842e8b3f639704605872fde6770e552e26e62c5724c14a3deaa260593db03227d8830179529f73da8704a3e1abedc2c"
vk = ecdsa.VerifyingKey.from_string(bytes.fromhex(vk_string), ecdsa.SECP256k1)

# the generation signature is 9737957703d4eb54efdff91e15343266123c5f15aaf033292c9903015af817f1
message = b'9737957703d4eb54efdff91e15343266123c5f15aaf033292c9903015af817f1'

# put your signature for Hello World in the line below
sig_hex = "08d7cbf6883ca98981602dbd41380c02a3360c82e45922b9bda0be30da51caaa2c6162aae7778a30e1ac768ac6b86a3deefb6ebabcda7fb5269fdfdb75c24b26"
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
