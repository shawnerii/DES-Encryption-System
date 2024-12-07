from permutations import initial_permutation, final_permutation
from sbox import sbox_substitution, expand

def encrypt_block(block, subkeys):
    permuted_block = initial_permutation(block)
    left, right = permuted_block[:32], permuted_block[32:]

    for subkey in subkeys:
        expanded_right = expand(right)
        xored = ''.join(str(int(b1) ^ int(b2)) for b1, b2 in zip(expanded_right, subkey))
        new_right = ''.join(str(int(bit_l) ^ int(bit_r)) for bit_l, bit_r in zip(left, sbox_substitution(xored)))
        left, right = right, new_right

    combined_block = right + left
    return final_permutation(combined_block)

def decrypt_block(block, subkeys):
    permuted_block = initial_permutation(block)
    left, right = permuted_block[:32], permuted_block[32:]

    for subkey in reversed(subkeys):
        expanded_right = expand(right)
        xored = ''.join(str(int(b1) ^ int(b2)) for b1, b2 in zip(expanded_right, subkey))
        new_right = ''.join(str(int(bit_l) ^ int(bit_r)) for bit_l, bit_r in zip(left, sbox_substitution(xored)))
        left, right = right, new_right

    combined_block = right + left
    return final_permutation(combined_block)

def test_encrypt_decrypt():
    subkeys = ["0" * 48] * 16
    block = "0" * 64
    encrypted = encrypt_block(block, subkeys)
    decrypted = decrypt_block(encrypted, subkeys)
    assert decrypted == block
    print("Encrypt/decrypt test passed")

if __name__ == "__main__":
    test_encrypt_decrypt()