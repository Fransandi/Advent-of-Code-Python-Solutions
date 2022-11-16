'''
=========================================
|| 🎄 Advent of Code 2021: Day 18 🗓
|| Link: https://adventofcode.com/2021
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''

from itertools import permutations
import math

OPEN = '['
CLOSE = ']'
PAIR = -1

### Part One
def part_one(input):
    snailfish_numbers = [line for line in input]
    root = build_tree(snailfish_numbers.pop(0))

    while snailfish_numbers:
        # Merge two snailfish numbers in one binary tree
        left_branch = root
        right_branch = build_tree(snailfish_numbers.pop(0))
        root = Node(PAIR, None, left_branch, right_branch)
        left_branch.parent = right_branch.parent = root
        
        reduce_number(root)
            
    return magnitude(root)

### Part Two
def part_two(input):
    max_magnitude = 0
    for pair in permutations(input, 2):
        max_magnitude = max(max_magnitude, part_one(list(pair)))

    return max_magnitude


class Node():
    def __init__(self, chars, parent = None, left = None, right = None):
        self.chars = chars
        self.parent = parent
        self.left = left
        self.right = right
        self.val = -1
        if isinstance(chars, int): self.val = int(chars)

def build_tree(line):
    tree = Node(line.strip()[1:-1])
    build_node(tree)
    return tree

def build_node(node):
    if node.val == PAIR:
        node.left = Node(get_left_half(node.chars), node)
        node.right = Node(get_right_half(node.chars), node)
        build_node(node.left)
        build_node(node.right)

def get_left_half(val):
    if val[0]!=OPEN: return int(val[0])
    count = 0
    for i, char in enumerate(val):
        if char == OPEN: count+=1
        if char == CLOSE: count-=1
        if count == 0: return val[1:i]

def get_right_half(val):
    if val[-1]!=CLOSE: return int(val[-1])
    count = 0
    for i, char in reversed(list(enumerate(val))):
        if char == OPEN: count+=1
        if char == CLOSE: count-=1
        if count == 0: return val[i+1:-1]

def reduce_number(root):    
    node = next_node_to_explode(root)
    if node: explode(node)
    else:
        node = next_node_to_split(root)
        if node: split(node)
        else: return
    
    # If any action was taken, reduce the number again
    reduce_number(root)

def next_node_to_explode(root):
    stack = [(root, 1)]
    while stack:
        node, depth = stack.pop()
        if node.val==PAIR and depth>4 and node.left.val!=PAIR and node.right.val!=PAIR: return node        
        if node.right: stack.append((node.right, depth+1))
        if node.left: stack.append((node.left, depth+1))
    
    return None

def next_node_to_split(root):
    stack = [root]
    while stack:
        node = stack.pop()
        if node.val>=10: return node
        if node.right: stack.append((node.right))
        if node.left: stack.append((node.left))
    
    return None

def explode(node):
    # Update explosion values to the left
    pointer = node
    while pointer.parent and pointer == pointer.parent.left:
        pointer = pointer.parent
    
    if pointer.parent: 
        pointer = pointer.parent.left
        while pointer.right: 
            pointer = pointer.right
        pointer.val+=node.left.val

    # Update explosion values to the right
    pointer = node
    while pointer.parent and pointer == pointer.parent.right:
        pointer = pointer.parent

    if pointer.parent:
        pointer = pointer.parent.right
        while pointer.left: 
            pointer = pointer.left
        pointer.val+=node.right.val

    # Set the exploded node value to 0, and remove its children nodes
    node.val, node.left, node.right = 0, None, None

def split(node):    
    node.left=Node(math.floor(node.val/2), node)
    node.right=Node(math.ceil(node.val/2), node)
    node.val=PAIR

def magnitude(node):
    # Base case: the node is a regular number
    if node.val!=PAIR: return node.val

    return (3*magnitude(node.left))+(2*magnitude(node.right))
