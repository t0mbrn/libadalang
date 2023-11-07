# coding=utf-8

import os
import argparse
import errno

from os import listdir
from os.path import isfile, join

parser = argparse.ArgumentParser(description='Extracts interface definitions')
parser.add_argument('-P', '--path', required=True, help='Out-Path of generate_rst.py')

args = parser.parse_args()

if (not os.path.isdir(args.path)):
    raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), args.path)

if args.path[len(args.path)-1] != '/':
    args.path.append('/')

# Retrieving files
file_list = [f for f in listdir(args.path) if isfile(join(args.path, f))]

# alternatively use os.walk, when having to parse subdirs too

# Genrating file names
file_names = []
for file in file_list:
    file_names.append({"path" : file, "name" : ((str(file).removesuffix(".rst")).replace('-', '.')).title()})

# Sortieren
file_names = sorted(file_names, key=lambda file: file["name"])
#print(file_names)

# Generating index.rst
index_path = "index.rst"
if not isfile(index_path):
    # try to resolve index.rst file path if the current working directory is not the directory
    # where sphinx-quickstart was used
    path_parts = reversed(args.path.split("/"))
    for part in path_parts:
        if part != "out":
            index_path = '../' + index_path
        else:
            index_path = '../' + index_path
            break

# Copying head of file
lines = []
with open(index_path, "r") as index:
    line : str = index.readline()
    while("============================" not in line):
        lines.append(line)
        line = index.readline()
    lines.append(line)


# Overwriting file
with open(index_path, "w") as index:
    index.writelines(lines)
    index.write("\n")
    index.write(".. toctree::\n")
    index.write("   :maxdepth: 4\n")
    index.write("\n")
    for file in file_names:
        index.write("    %s <%s>\n" % (file["name"], args.path + file["path"]))
    index.write("\n")
    index.write("Indices and tables\n")
    index.write("==================\n")
    index.write("\n")
    index.write("* :ref:`genindex`\n")
    index.write("* :ref:`search`\n")






