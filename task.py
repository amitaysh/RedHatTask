#!/usr/bin/python
"""
This script will search regular expression in file(s) or in stdin, supplied by the user via command line.
It will print results per matching line.
If there are multiple matches per line - default is to print line only 1 time.
There are several flags that can be sent to script:
 > -u ( --underscore ) will print '^' under the matching text
 > -c ( --color ) will highlight matching text
 > -m ( --machine ) will generate machine readable output:
                  format: file_name:no_line:start_pos:matched_text
Assumption was taken that input is ASCII
"""

__author__ = 'Amitay Shahar'
__email__ = 'amitay.shahar2@gmail.com'

import cmd_parsing
import re_handling
import output_handler
import fileinput


class Task(object):
    """Class Task is a wrapper and will handle the actions according to task requirements"""
    def __init__(self):
        self.parsed_elements = None
        self.regex = None
        self.results = list()

    def run_task(self):
        """
        Will follow task requirements 1 by 1:
        1. parse args from cmd
        2. convert given string to regex object
        3. search regex in data (files or stdin)
        4. create object according to required output format
        5. print results in required structure
        """
        self.parsed_elements = cmd_parsing.CmdParsing()
        self.regex = re_handling.ReHandling(self.parsed_elements.args.regex)
        self._search_input()
        output_type = output_handler.OutputType().find_type(self.parsed_elements.args)
        output_type.print_output(self.results)

    def _search_input(self):
        """Go over input line-by-line, file-by-file and perform regex search on it, append results for later use"""
        try:
            for line in fileinput.input(files=self.parsed_elements.args.files_names, mode='r'):
                res = self.regex.search_regex_in_data(line)
                for item in res:
                    self.results.append({'file_name': fileinput.filename(), 'no_line': fileinput.filelineno(),
                                         'start_pos': item.start(), 'matched_text': item.group(), 'line': line.rstrip()})
        except Exception, err:
            raise Exception('OOPS! search in data failed: {0}'.format(err))


def main():
    """Main function, just initialize task and run it"""
    task = Task()
    task.run_task()


if __name__ == '__main__':
    main()
