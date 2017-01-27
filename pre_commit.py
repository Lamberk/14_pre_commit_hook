#! /usr/bin/python3

from subprocess import Popen

import sys


def shell_command(command):
    proc = Popen(command)
    proc.wait()
    return proc.returncode


code = shell_command(['python3', 'tests.py'])
sys.exit(code)
