#!/usr/bin/env python2
from __future__ import absolute_import

import argparse
import sys
from subprocess import Popen

from pwn import *
from pwnlib.commandline import common

parser = common.parser_commands.add_parser(
    'aslr',
    help = 'Confirm or change aslr'
)
parser.add_argument(
    'value',
    help = 'on | off',
    nargs='?'
)

def main(args):
    if args.value is None:
        cmd = 'sysctl -n kernel.randomize_va_space'
    elif args.value == 'on':
        cmd = 'sysctl -w kernel.randomize_va_space=2'
    elif args.value == 'off':
        cmd = 'sysctl -w kernel.randomize_va_space=0'
    else:
        return
    p = Popen(cmd, shell=True)
    p.wait()

if __name__ == '__main__':
    pwnlib.commandline.common.main(__file__)
