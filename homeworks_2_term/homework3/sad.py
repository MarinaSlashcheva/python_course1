#!/usr/bin/python3.5
import argparse
import os
import shutil
from subprocess import run

parser = argparse.ArgumentParser(description='I didn`t figure out yet what this parser do')
parser.add_argument('command',
                    type=str,
                    choices=['store', 'diff'],
                    help='What to do with the query')
parser.add_argument('path',
                    type=str,
                    help='Path to the file or folder')

args=parser.parse_args()
command = args.command
path = args.path

home_path = '/home/march/sad/' # Creating the directory for storage path information
if os.path.exists(home_path) != True:
    run('mkdir ~/sad/', shell=True)

if command == 'store':
    if os.path.isfile(path):
        shutil.copy(path, home_path)
        print('copied a file')
    if os.path.isdir(path):
        where_to = home_path + path
        copy_command = 'cp -r ' + path + ' ' + where_to
        run(copy_command, shell=True)
        print('copied a folder')

if command == 'diff':
    old_version = home_path + path
    new_version = path
    run(['diff', old_version, new_version])