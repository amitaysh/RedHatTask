#!/usr/bin/python
"""
lala
"""

import argparse


class CmdParsing(object):
    def __init__(self):
        self.args = self._get_args()

    @staticmethod
    def _get_args():
        parser = argparse.ArgumentParser(description="This script will search lines containing a match of a regular "
                                                     "expression from input (files or standard input).")
        parser.add_argument('regex', help='Regular expression pattern to search.')
        parser.add_argument('files_names', nargs='*', help="One or more files names to search within, if empty "
                                                           "or '-' is given, input will be taken from standard input.")
        group = parser.add_mutually_exclusive_group()
        group.add_argument('-u', '--underscore', action='store_true', help="print '^' under the matching text.")
        group.add_argument('-c', '--color', action='store_true', help='highlight matching text.')
        group.add_argument('-m', '--machine', action='store_true', help='generate machine readable output.')
        return parser.parse_args()
