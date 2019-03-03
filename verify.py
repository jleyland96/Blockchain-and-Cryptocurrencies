import ecdsa

# put the hex of your public key in the line below
vk_string="7f7170c84020cc8b8ed97c05250bf578aa1883dc3ce88e1b07e856b6bd16af22454fe273aad9a9255d3904799fd69ea62a1d95754df25961a7bc13b55e88a05b"
vk = ecdsa.VerifyingKey.from_string(bytes.fromhex(vk_string), ecdsa.SECP256k1)

# the generation signature is 9737957703d4eb54efdff91e15343266123c5f15aaf033292c9903015af817f1
message = b'9737957703d4eb54efdff91e15343266123c5f15aaf033292c9903015af817f1'

# put your signature for Hello World in the line below
sig_hex = "be5ce7290429304758cc2f23271b7173460b3e8b63ab46a3e23080f83eb85e228d99ecb1adc02f1da11ad410915d36ae212d486b9e21f1af7581fd92fb8dcdf1"
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