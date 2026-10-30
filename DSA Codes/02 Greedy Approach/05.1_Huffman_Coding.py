import heapq


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def huffman_codes(characters, frequencies):

    heap = []
    for i in range(len(characters)):
        node = Node(characters[i], frequencies[i])
        heapq.heappush(heap, node)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    root = heap[0]
    codes = {}

    def generate(node, current=""):
        if node is None:
            return
        if node.char is not None:  # leaf
            codes[node.char] = current if current else "0"
            return
        generate(node.left, current + "0")
        generate(node.right, current + "1")

    generate(root)
    return codes


s = "abcdef"
freq = [5, 9, 12, 15, 27, 45]

result = huffman_codes(s, freq)
print(result)
