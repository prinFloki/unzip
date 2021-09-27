import argparse #parser for commandline options
import socket
import shlex #easies the creation of lexical analyzer, and a parser too.
import subprocess #spawn processes
import sys #provides functions and variables that are used to manipulate runtime environnement
import textwrap #
import threading
def execute(cmd):
    cmd = cmd.strip()
    if not cmd:
        return
    output = subprocess.check_output(shlex.split(cmd),
                                stderr=subprocess.STDOUT)
    return output.decode()