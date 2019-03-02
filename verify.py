import ecdsa

# put the hex of your public key in the line below
vk_string="3a9fd072166663770ff14efb7c44e3af236a717e2a583aa80983e72179e18bab802448740e9366a7289b208827e5862b037871b790d073df152fe373591658cd"
vk = ecdsa.VerifyingKey.from_string(bytes.fromhex(vk_string), ecdsa.SECP256k1)

# the generation signature is 9737957703d4eb54efdff91e15343266123c5f15aaf033292c9903015af817f1
message = b'9737957703d4eb54efdff91e15343266123c5f15aaf033292c9903015af817f1'

# put your signature for Hello World in the line below
sig_hex = "fa0e493b503173e98e42f854b7290a7ef467d28323af71948130f8b764e9f7ebd411f24683c459117882ec4109a859d50de91cda95173196113a07d4ea4c2b97"
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