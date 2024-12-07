import random

PC1 = [
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4
]

PC2 = [
    14, 17, 11, 24, 1, 5, 3, 28,
    15, 6, 21, 10, 23, 19, 12, 4,
    26, 8, 16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55, 30, 40,
    51, 45, 33, 48, 44, 49, 39, 56,
    34, 53, 46, 42, 50, 36, 29, 32
]

def generate_random_key():
    return ''.join(random.choice('01') for _ in range(64))

def generate_subkeys(key):
    permuted_key = ''.join(key[PC1[i] - 1] for i in range(56))
    left, right = permuted_key[:28], permuted_key[28:]
    subkeys = []
    shifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

    for shift in shifts:
        left = left[shift:] + left[:shift]
        right = right[shift:] + right[:shift]
        combined_key = left + right
        subkey = ''.join(combined_key[PC2[i] - 1] for i in range(48))
        subkeys.append(subkey)
    return subkeys

def test_key_schedule():
    key = generate_random_key()
    subkeys = generate_subkeys(key)
    assert len(subkeys) == 16
    assert all(len(subkey) == 48 for subkey in subkeys)
    print("Key schedule test passed")

if __name__ == "__main__":
    test_key_schedule()