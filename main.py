from key_schedule import generate_random_key, generate_subkeys
from des_encrypt_decrypt import encrypt_block, decrypt_block
from utils import pad_text, unpad_text, text_to_bin, bin_to_text
import os

def main():
    plaintext = "From fairest creatures we desire increase, That thereby beauty's rose might never die, But as the riper should by time decease, His tender heir might bear his memory: But thou contracted to thine own bright eyes, Feed'st thy light's flame with self-substantial fuel, Making a famine where abundance lies, Thy self thy foe, to thy sweet self too cruel: Thou that art now the world's fresh ornament, And only herald to the gaudy spring, Within thine own bud buriest thy content, And tender churl mak'st waste in niggarding: Pity the world, or else this glutton be, To eat the world's due, by the grave and thee. When forty winters shall besiege thy brow, And dig deep trenches in thy beauty's field, Thy youth's proud livery so gazed on now, Will be a tattered weed of small worth held: Then being asked, where all thy beauty lies, Where all the treasure of thy lusty days; To say within thine own deep sunken eyes, Were an all-eating shame, and thriftless praise."

    output_dir = os.path.abspath(os.path.dirname(__file__))
    encrypted_file_path = os.path.join(output_dir, "encrypted_output.txt")
    decrypted_file_path = os.path.join(output_dir, "decrypted_output.txt")

    padded_text = pad_text(plaintext)
    key = generate_random_key()
    subkeys = generate_subkeys(key)
    binary_text = text_to_bin(padded_text)

    encrypted_text = ''.join(encrypt_block(binary_text[i:i+64], subkeys) for i in range(0, len(binary_text), 64))

    try:
        with open(encrypted_file_path, "w") as enc_file:
            enc_file.write(encrypted_text)
        print(f"Encrypted text saved to {encrypted_file_path}")
    except Exception as e:
        print(f"Failed to save encrypted text: {e}")

    decrypted_binary_text = ''.join(decrypt_block(encrypted_text[i:i+64], subkeys) for i in range(0, len(encrypted_text), 64))
    decrypted_text = unpad_text(bin_to_text(decrypted_binary_text))
    
    try:
        with open(decrypted_file_path, "w") as dec_file:
            dec_file.write(decrypted_text)
        print(f"Decrypted text saved to {decrypted_file_path}")
    except Exception as e:
        print(f"Failed to save decrypted text: {e}")

    print("Original text:", plaintext)
    print("Decrypted text:", decrypted_text)
    assert plaintext == decrypted_text, "Decryption failed!"

if __name__ == "__main__":
    main()