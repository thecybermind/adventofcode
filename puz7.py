# import pprint

# fs = {
#   '<subdirname>': (size, { ... }),
#   '<filename>': filesize,
#   '#': dirsize,
#   '.': dirname,
# }
fs = {'.': '/', '#': 0}
pwd = []

def change_dir(dirname):
    global pwd
    if dirname == '..':
        if pwd:
            pwd.pop()
    elif dirname == '/':
        pwd = []
    else:
        pwd.append(dirname)

def find_pwd():
    global pwd
    d = fs
    for subdir in pwd:
        d = d[subdir]
    return d

def add_to_dir(name, size):
    d = find_pwd()
    d[name] = size

def get_sizes_r(d):
    for name, entry in d.items():
        if name == '#' or name == '.':
            continue
        if isinstance(entry, dict):
            get_sizes_r(entry)
            d['#'] += entry['#']
        else:
            d['#'] += entry

def size_list_r(d):
    lst = []
    for name, entry in d.items():
        if isinstance(entry, dict):
            lst.extend(size_list_r(entry))        
    
    lst.append( (d['.'], d['#']) )
    
    return lst       

with open('input7.txt') as inp:
    for line in inp:
        line = line.strip()
        
        if line.startswith('$ cd '):
            dirname = line[5:]
            change_dir(dirname)
        elif line == '$ ls':
            pass
        # ls listing
        else:
            size, name = line.split(' ', maxsplit=1)
            if size == 'dir':
                size = {'.': name, '#': 0}
            else:
                size = int(size)
            add_to_dir(name, size)

# recursively iterate through all directories storing sizes of each dir
get_sizes_r(fs)
# pprint.pp(fs, indent=2)

# part 1
# To begin, find all of the directories with a total size of at most 100000, then calculate the sum of their total sizes.
sizes = size_list_r(fs)
# pprint.pp(sizes, indent=2)

total_part1 = sum( size for _,size in sizes if size <= 100000 )
print(f'Part 1 total: {total_part1}')

# part 2
# find smallest directory to delete that will provide enough space for an update
# total drive size is 70000000, space needed is 30000000
total_storage = 70000000
space_used = fs['#']
space_free = total_storage - space_used
space_needed = 30000000 - space_free

dir_part2 = min( size for _,size in sizes if size >= space_needed )
print(f'Part 2 directory to delete: {dir_part2}')

