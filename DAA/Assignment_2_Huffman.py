"""Assignment 2: Huffman encoding using a greedy min-heap."""

# PRACTICAL TEST INPUT
# Run: python3 Assignment_2_Huffman.py
# At the text prompt, press Enter to use the assignment's example text, or type:
# mississippi
# The program prints one valid prefix code per character, the encoded bits,
# and the decoded text. Huffman codes can differ when frequencies tie.

from dataclasses import dataclass
import heapq


@dataclass
class HuffmanNode:
    frequency: int
    symbol: str = None
    left: object = None
    right: object = None


def build_huffman_codes(text):
    """Return a dictionary of character-to-bitstring Huffman codes and the tree."""
    if not text:
        raise ValueError("Text must not be empty")

    frequencies = {}
    for character in text:
        frequencies[character] = frequencies.get(character, 0) + 1

    # The counter makes ties deterministic and prevents comparing tree nodes.
    heap = []
    counter = 0
    for character, frequency in frequencies.items():
        node = HuffmanNode(frequency, character)
        heapq.heappush(heap, (frequency, counter, node))
        counter += 1

    if len(heap) == 1:
        root = heap[0][2]
        return {root.symbol: "0"}, root

    while len(heap) > 1:
        left_frequency, _, left = heapq.heappop(heap)
        right_frequency, _, right = heapq.heappop(heap)
        parent = HuffmanNode(left_frequency + right_frequency, None, left, right)
        heapq.heappush(heap, (parent.frequency, counter, parent))
        counter += 1

    root = heap[0][2]
    codes = {}

    def walk(node, prefix):
        if node.symbol is not None:
            codes[node.symbol] = prefix
            return
        walk(node.left, prefix + "0")
        walk(node.right, prefix + "1")

    walk(root, "")
    return codes, root


def encode(text, codes):
    return "".join(codes[character] for character in text)


def decode(bits, root):
    if root.symbol is not None:
        if any(bit != "0" for bit in bits):
            raise ValueError("Invalid bit for a single-symbol tree")
        return root.symbol * len(bits)

    decoded = []
    node = root
    for bit in bits:
        if bit not in "01":
            raise ValueError("Encoded input must contain only 0 and 1")
        node = node.left if bit == "0" else node.right
        if node.symbol is not None:
            decoded.append(node.symbol)
            node = root
    if node is not root:
        raise ValueError("Encoded input ends in the middle of a code")
    return "".join(decoded)


if __name__ == "__main__":
    example = "ABCCDEBABFFBACBEBDFAAAABCDEEDCCBFEBFCAEFBACBEBDFAAAABC"
    text = input("Enter text (press Enter to use the assignment example): ") or example
    codes, tree = build_huffman_codes(text)
    encoded = encode(text, codes)

    print("Huffman codes:")
    for character in sorted(codes):
        print(f"  {character!r}: {codes[character]} ({text.count(character)} occurrence(s))")
    print("Encoded bits:", encoded)
    print("Decoded text:", decode(encoded, tree))
    print(f"Average code length: {len(encoded) / len(text):.2f} bits per character")
    print("Building the tree: O(k log k), where k is the number of distinct characters.")



"""
Theory to remember:
- Huffman Coding: A compression technique that assigns shorter binary codes to frequently occurring characters.
- Greedy Algorithm: Makes the best available choice at each step.
- Min-Heap: A data structure where the smallest element is at the top.
- Prefix-Free Code: No character's code is the prefix of another character's code.
- Lossless Compression: Original data can be recovered without losing information.
How to explain orally:

"I implemented Huffman coding using a greedy approach and a min-heap. It counts character frequencies, combines the two least frequent characters, builds a binary tree, and generates binary codes."

Example: Input AAABBC
Character	Frequency	Code
A	3	0
B	2	11
C	1	10

Encoded output: 000111110

Remember these terms:
- Left edge = 0
- Right edge = 1
- heapq: Python library for heap operations.
- encode(): Converts text into binary codes.
- decode(): Converts binary codes back into text.
Complexity: O(n + k log k), where n = input length and k = distinct characters.

"""