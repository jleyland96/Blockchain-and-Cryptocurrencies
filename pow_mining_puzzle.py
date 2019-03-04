import hashlib
import json
import time


def compute_target_val(difficulty=0.001):
    # calculating the target value for difficulty 0.001
    initial_target = 0x00000000FFFF0000000000000000000000000000000000000000000000000000
    target = initial_target / difficulty
    return hex(int(target))


def find_valid_nonce():
    target_val = compute_target_val(difficulty=0.001)
    print("Target val:", target_val)
    current_nonce = 0

    while True:
        example_block_header['nonce'] = current_nonce

        # Simplified conversion of block header into bytes:
        block_serialised = json.dumps(example_block_header, sort_keys=True).encode()

        # Double SHA256 hashing of the serialised block
        block_hash = hashlib.sha256(hashlib.sha256(block_serialised).digest()).hexdigest()

        # IF WE HAVE A VALID NONCE
        if int(block_hash, 16) < int(target_val, 16):
            break

        current_nonce += 1

    print('VALID NONCE! Hash with nonce ' + str(example_block_header['nonce']) + ': ' + block_hash)
    print("Target (int):", int(target_val, 16))
    print("Hash   (int):", int(block_hash, 16))
    print("Target (hex):", target_val)
    print("Hash   (hex):", block_hash)
    print("\n")


# An example block header - do not change any fields except nonce and coinbase_addr
example_block_header = {'height': 1478503,
                        'prev_block': '0000000000000da6cff8a34298ddb42e80204669367b781c87c88cf00787fcf6',
                        'total': 38982714093,
                        'fees': 36351,
                        'size': 484,
                        'ver': 536870912,
                        'time': 1550603039.882228,
                        'bits': 437239872,
                        'nonce': 0,                     # You may change this field of the block. 553137 is valid.
                        'coinbase_addr': 'dwmr15',      # You should change this field of the block to your studentID
                        'n_tx': 2,
                        'mrkl_root': '69224771b7a2ed554b28857ed85a94b088dc3d89b53c2127bfc5c16ff49da229',
                        'txids': ['3f9dfc50198cf9c2b0328cd1452513e3953693708417440cd921ae18616f0bfc', '3352ead356030b335af000ed4e9030d487bf943089fc0912635f2bb020261e7f'],
                        'depth': 0}


# Simplified conversion of block header into bytes:
block_serialised = json.dumps(example_block_header, sort_keys=True).encode()
# Double SHA256 hashing of the serialised block
block_hash = hashlib.sha256(hashlib.sha256(block_serialised).digest()).hexdigest()
print('Hash with nonce ' + str(example_block_header['nonce'])+': '+block_hash, "\n")

# Find valid nonce by incrementing from 0
start = time.time()
find_valid_nonce()  # Returns 553137
end = time.time()
# Print time taken to find the valid nonce
print("it took", end-start, "second to calculate a valid nonce")





