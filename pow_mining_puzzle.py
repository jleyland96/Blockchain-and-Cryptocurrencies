import hashlib
import json
import time

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


# Function to calculate a target value in Hex, given the difficulty value
def compute_target_val(difficulty=0.001):
    # calculating the target value for difficulty 0.001
    initial_target = 0x00000000FFFF0000000000000000000000000000000000000000000000000000
    target = initial_target / difficulty
    return hex(int(target))


# Function the find the first valid nonce by incrementing the nonce value and checking validity until valid
def find_valid_nonce():
    target_val = compute_target_val(difficulty=0.001)
    print("Target val:", target_val)
    current_nonce = 0

    # Start timing how long it takes to find a valid nonce
    start = time.time()
    while True:
        example_block_header['nonce'] = current_nonce

        # Simplified conversion of block header into bytes:
        block_serialised = json.dumps(example_block_header, sort_keys=True).encode()

        # Double SHA256 hashing of the serialised block
        block_hash = hashlib.sha256(hashlib.sha256(block_serialised).digest()).hexdigest()

        # IF WE HAVE A VALID NONCE
        if int(block_hash, 16) < int(target_val, 16):
            # Stop the clock
            end = time.time()
            break

        # Increment nonce value and try again
        current_nonce += 1

    print('VALID NONCE! Hash with nonce ' + str(example_block_header['nonce']) + ': ' + block_hash)
    print("Target (int):", int(target_val, 16))
    print("Hash   (int):", int(block_hash, 16))
    print("Target (hex):", target_val)
    print("Hash   (hex):", block_hash)
    print("it took", end-start, "second to calculate a valid nonce")
    print("\n")


# Print the target value at difficulty 7,454,968,648,263
print(compute_target_val(difficulty=7454968648263))

# Find a valid nonce
find_valid_nonce()  # First valid nonce = 553137





