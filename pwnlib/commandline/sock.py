#!/usr/bin/env python2
from __future__ import absolute_import

import argparse
import sys
from subprocess import Popen

from pwn import *
from pwnlib.commandline import common

parser = common.parser_commands.add_parser(
    'sock',
    help = 'local socat command'
)
parser.add_argument(
    'elf',
    type=file,
    help='Socat file'
)

def main(args):
    elf  = args.elf.name
    proc = Popen('killall socat 2> /dev/null', shell=True)
    proc.wait()

    if not elf:
        parser.print_usage()
        return

    cmd = '''
    socat tcp-listen:4444,reuseaddr,fork exec:./{0} &
    '''.format(elf)

    proc = Popen(cmd, shell=True)
    print('exec: {0}'.format(elf))
    print('port: 4444')

if __name__ == '__main__':
    pwnlib.commandline.common.main(__file__)
