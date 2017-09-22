#!/usr/bin/env python2
from __future__ import absolute_import

import os

from pwn import *
from pwnlib.commandline import common


parser = common.parser_commands.add_parser(
    'x',
    help = 'exec exploit.py'
)

parser.add_argument(
    'cmd','',
    nargs='?',
    help='[r | l | a]')

def main(args):
    if args.cmd is not None:
        cmd = 'python exploit.py {0}'.format(args.cmd)
    else:
        cmd = 'python exploit.py a'
    os.system(cmd)

if __name__ == '__main__':
    pwnlib.commandline.common.main(__file__)
