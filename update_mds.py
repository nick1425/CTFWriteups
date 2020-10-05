#!/usr/bin/python3
import sys
import os
import itertools

LOG = True


def match(dir_entry: os.DirEntry, file_entry: os.DirEntry):
    if not dir_entry.is_dir() or not file_entry.is_file():
        return False
    _, dir_name = os.path.split(dir_entry.name)
    _, file_name = os.path.split(file_entry.name)
    return dir_name + '.md' == file_name


def handle_md_pair(file_path, dir_path):
    def process_line(l):
        if not l.startswith('![](../.gitbook'):
            return l
        return '![](' + l[len('![](..'):]

    src = open(file_path, 'r')
    dst = open(os.path.join(dir_path, 'README.md'), 'w')
    for line in src:
        dst.write(process_line(line)+'\n')

    src.close()
    dst.close()


if len(sys.argv) != 2:
    print('usage: update_mds path')
    sys.exit()
path = sys.argv[1]
if not os.path.isdir(path):
    print('ERROR, expected valid dir got \'{}\''.format(path))

entries = []
for entry in os.scandir(path):
    entries.append(entry)

md_dir_pairs = []

for file_entry, dir_entry in itertools.product(entries, entries):
    if match(dir_entry, file_entry):
        md_dir_pairs.append((file_entry, dir_entry))

for (file_ent, dir_ent) in md_dir_pairs:
    if LOG:
        print('match', file_ent.name, dir_ent.name)
    handle_md_pair(file_ent.path, dir_ent.path)
