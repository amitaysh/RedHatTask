#!/usr/bin/python
"""
lala
"""

import cmd_parsing
import re_handling
import custom_print
import fileinput


class Task(object):
    def __init__(self):
        self.parsed_elements = None
        self.regex = None
        self.results = list()
# no point going over input before verifying regex is ok

    def run_task(self):
        self.parsed_elements = cmd_parsing.CmdParsing()
        self.regex = re_handling.ReHandling(self.parsed_elements.args.regex)
        self._search_input()
        custom_print.CustomPrint(self.results, self.parsed_elements.args)

    def _search_input(self):
        for line in fileinput.input(files=self.parsed_elements.args.files_names, mode='r'):
            res = self.regex.search_regex_in_data(line)
            try:
                for item in res:
                    self.results.append({'filename': fileinput.filename(), 'no_line': fileinput.filelineno(),
                                         'start_pos': item.start(), 'matched_text': item.group(), 'line': line.rstrip()})
            except TypeError:
                raise Exception("hmmm that shouldn't happen, probably tried to iterate over non-iterable object.")


def main():
    task = Task()
    task.run_task()


if __name__ == '__main__':
    main()
