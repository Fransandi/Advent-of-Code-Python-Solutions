'''
=========================================
|| 🎄 Advent of Code 2022: Day 7 🗓
|| Link: https://adventofcode.com/2022
|| Template by: @fransandi
|| Solution by: @fransandi
=========================================
'''

TOTAL_SPACE = 70000000
REQUIRED_SPACE = 30000000

class Node():
    def __init__(self, name, size, parent):
        self.name = name
        self.size = size
        self.children = []
        self.parent = parent
        self.is_file = size>0

### Part One
def part_one(input):
    root = build_tree(input)
    directories_size = get_directories_size(root)
    return sum([size for size in directories_size.values() if size<=100000])

### Part Two
def part_two(input):
    root = build_tree(input)
    directories_size = get_directories_size(root)
    needed_space = REQUIRED_SPACE - (TOTAL_SPACE - directories_size['/'])
    return next(size for size in sorted(directories_size.values()) if size>=needed_space)


def build_tree(input):
    root = Node('/', 0, None)
    cur = root
    
    for line in [line.strip() for line in input]:
        if line == '$ ls': continue

        # Change directories
        if line.startswith('$ cd'):
            directory = line.split()[-1]
            if directory == '/': cur = root
            elif directory == '..': cur = cur.parent
            else: cur = next(child for child in cur.children if child.name == directory)
        # Add directory or file to current node children
        else:
            output = line.split()
            name, size = output[1], 0 if output[0]=='dir' else int(output[0])
            child = Node(name, size, cur)
            cur.children.append(child)
            # Add the file size value to all its parent directories
            if child.size>0:
                temp = child.parent
                while temp:
                    temp.size += child.size
                    temp = temp.parent
    return root
        
def get_directories_size(root):
    directories_size, queue = {}, [root]
    while queue:
        node = queue.pop(0)
        if not node.is_file: directories_size[node.name]=node.size
        queue += node.children
    return directories_size
