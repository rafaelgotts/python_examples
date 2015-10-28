# coding: utf-8

# Rafael Gottsfritz
# md5sum on python

# pymd5sum.py

from hashlib import md5
from os.path import exists, isfile
from sys import exit, argv

path_filename = str(argv[1])

if not exists(path_filename):
    print("pymd5sum: {}: Arquivo ou diretório não encontrado".format(path_filename))
    exit(1)

if not isfile(path_filename):
    print("pymd5sum: {}: É um diretório".format(path_filename))
    exit(1)

file = open(path_filename, 'rb')

md5sum = md5(file.read())

# filename = path_filename.split('/')[-1]

print("{}  {}".format(md5sum.hexdigest(), path_filename))