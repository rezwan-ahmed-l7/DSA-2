import heapq


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def huffman(text):
    # Frequency
    freq = {}
    for c in text:
        freq[c] = freq.get(c, 0) + 1

    heap = [Node(c, f) for c, f in freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    codes = {}

    def generate(node, curr=""):
        if not node:
            return
        if node.char:
            codes[node.char] = curr if curr else "0"
            return
        generate(node.left, curr + "0")
        generate(node.right, curr + "1")

    generate(heap[0])
    return codes


text = "aabbc"
print(huffman(text))
