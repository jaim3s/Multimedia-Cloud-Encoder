import heapq
from collections import Counter

class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ''

    def __lt__(self, other):
        return self.freq < other.freq

def print_codes(node, val=''):
    new_val = val + str(node.huff)
    if node.left:
        print_codes(node.left, new_val)
    if node.right:
        print_codes(node.right, new_val)
    if not node.left and not node.right:
        print(f"{node.symbol}: {new_val}")

def huffman_code(s):
    #frequency = Counter(s)
    frequency = {"A" : 0.05, "B" : 0.1, "C" : 0.15, "D" : 0.27, "E" : 0.2, "F" : 0.23}
    heap = [Node(freq, symbol) for symbol, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        left.huff = '0'
        right.huff = '1'
        
        new_node = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
        heapq.heappush(heap, new_node)

    root = heap[0]
    print_codes(root)

string = "ABRACADABRA"
freq = {"A" : 0.05, "B" : 0.1, "C" : 0.15, "D" : 0.27, "E" : 0.2, "F" : 0.23}
huffman_code(string)
