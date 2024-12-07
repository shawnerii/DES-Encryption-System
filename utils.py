def pad_text(text):
    padding_len = 8 - (len(text) % 8)
    return text + chr(padding_len) * padding_len

def unpad_text(text):
    padding_len = ord(text[-1])
    return text[:-padding_len]

def text_to_bin(text):
    return ''.join(f"{ord(c):08b}" for c in text)

def bin_to_text(binary_string):
    chars = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]
    return ''.join(chr(int(b, 2)) for b in chars)

def test_utils():
    text = "Hello"
    padded = pad_text(text)
    unpadded = unpad_text(padded)
    assert unpadded == text
    print("Utils test passed")

if __name__ == "__main__":
    test_utils()