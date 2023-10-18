import heapq
from collections import Counter

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    char_freq = Counter(text)
    min_heap = [HuffmanNode(char, freq) for char, freq in char_freq.items()]
    heapq.heapify(min_heap)

    while len(min_heap) > 1:
        left_node = heapq.heappop(min_heap)
        right_node = heapq.heappop(min_heap)
        new_node = HuffmanNode(None, left_node.freq + right_node.freq)
        new_node.left = left_node
        new_node.right = right_node
        heapq.heappush(min_heap, new_node)

    return heapq.heappop(min_heap)

def build_huffman_table(node, current_code, huffman_table):
    if node.char:
        huffman_table[node.char] = current_code
        return

    build_huffman_table(node.left, current_code + '0', huffman_table)
    build_huffman_table(node.right, current_code + '1', huffman_table)

def huffman_encoding(text):
    if not text:
        return "", {}

    root = build_huffman_tree(text)
    huffman_table = {}
    build_huffman_table(root, "", huffman_table)

    encoded_text = "".join(huffman_table[char] for char in text)
    return encoded_text, huffman_table

def huffman_decoding(encoded_text, huffman_table):
    if not encoded_text:
        return ""

    reversed_huffman_table = {code: char for char, code in huffman_table.items()}
    decoded_text = ""
    current_code = ""
    
    for bit in encoded_text:
        current_code += bit
        if current_code in reversed_huffman_table:
            decoded_text += reversed_huffman_table[current_code]
            current_code = ""

    return decoded_text

# Example usage
if __name__ == "__main__":
    text = "abbcccddddeeeee"
    encoded_text, huffman_table = huffman_encoding(text)
    print("Original text:", text)
    print("Encoded text:", encoded_text)
    print("Huffman table:", huffman_table)

    decoded_text = huffman_decoding(encoded_text, huffman_table)
    print("Decoded text:", decoded_text)
