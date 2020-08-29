import sys
import os


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

for entry in entries:
    if not entry.is_file():
        continue
    path, name = os.path.split(entry.path)
    name, ext = os.path.splitext(name)
    if ext.lower() != '.md':
        continue
    for entry2 in entries:
        if not entry2.is_dir:
            continue
        if entry2.path.endswith(name):
            md_dir_pairs.append((entry, entry2))
            break

for (file_ent, dir_ent) in md_dir_pairs:
    handle_md_pair(file_ent.path, dir_ent.path)
