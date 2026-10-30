def huffman_encode(text):
    if not text:
        return "", {}

    # Frequency count
    freq = {}
    for c in text:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1

    # nodes = [freq, unique_id, chars]
    nodes = []
    uid = 0
    for c, f in freq.items():
        nodes.append([f, uid, c])
        uid += 1

    codes = {c: "" for c in freq}

    while len(nodes) > 1:
        # Manual sort kore smallest duita ber kori
        nodes.sort(key=lambda x: x[0])

        left = nodes.pop(0)
        right = nodes.pop(0)

        # Code update
        for char in left[2]:
            codes[char] = "0" + codes[char]
        for char in right[2]:
            codes[char] = "1" + codes[char]

        # Merge
        merged = [left[0] + right[0], uid, left[2] + right[2]]
        uid += 1
        nodes.append(merged)

    # Encode
    encoded = ""
    for c in text:
        encoded += codes[c]

    return encoded, codes


def huffman_decode(encoded, codes):
    reverse = {code: char for char, code in codes.items()}
    decoded = ""
    current = ""

    for bit in encoded:
        current += bit
        if current in reverse:
            decoded += reverse[current]
            current = ""
    return decoded


text = "aabbc"
encoded, codes = huffman_encode(text)
decoded = huffman_decode(encoded, codes)

print("Original :", text)
print("Codes    :", codes)
print("Encoded  :", encoded)
print("Decoded  :", decoded)
