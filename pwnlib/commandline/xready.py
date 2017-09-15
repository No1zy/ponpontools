#!/usr/bin/env python2
from __future__ import absolute_import

import re

from pwn import *
from pwnlib.commandline import common

from mako.lookup import TemplateLookup

parser = common.parser_commands.add_parser(
    'xready',
    help = 'Generate an exploit template'
)

parser.add_argument('binary', nargs='?', help='Target binary')
parser.add_argument('--host', help='Remote host')
parser.add_argument('--port', help='Remote port', type=int)
parser.add_argument('--libc', '-l', help='libc',)
parser.add_argument('--arch', '-a', help='Execution file architecture',)

def main(args):
    cache = None

    lookup = TemplateLookup(
        directories      = [os.path.join(pwnlib.data.path, 'templates')],
        module_directory = cache
    )

    if not (args.binary):
        log.error("Must specify --path or a exe")

    template = lookup.get_template('exploit.py')
    output = template.render(binary=args.binary,
                             host=args.host,
                             port=args.port,
                             libc=args.libc,
                             arch=args.arch,)
    # Fix Mako formatting bs
    output = re.sub('\n\n\n', '\n\n', output)

    f = open('exploit.py', 'w')
    f.write(output)
    f.close()

    f = open('cmd', 'w')
    f.write('')
    f.close()
    
    if not sys.stdout.isatty():
        try: os.fchmod(sys.stdout.fileno(), 0700)
        except OSError: pass

if __name__ == '__main__':
    pwnlib.commandline.common.main(__file__)
