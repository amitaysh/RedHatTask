#!/usr/bin/python
"""
lala
"""


class CustomPrint(object):
    def __init__(self, results, flags):
        self._results = results
        self.base_string = 'File Name: {0}. Line Number: {1}. Matching Line: {2}'
        if flags.underscore:
            self._underscore_print()
        elif flags.color:
            self._color_print()
        elif flags.machine:
            self._machine_print()
        else:
            self._regular_print()

    def _underscore_print(self):
        for res in self._results:
            temp_str = self.base_string.format(res['filename'], res['no_line'], res['line'])
            current_match_location = len(self.base_string) + res['start_pos']
            index = temp_str.find(res['matched_text'], current_match_location)
            print temp_str
            print ''.ljust(index) + '^' * len(res['matched_text'])

    def _color_print(self):
        for res in self._results:
            color_text = '\033[94m' + res['matched_text'] + '\033[0m'
            start_pos = res['start_pos']
            end_pos = start_pos+len(res['matched_text'])
            rest_line = start_pos+len(res['matched_text'])
            fixed_line = res['line'][:start_pos] + \
                         res['line'][start_pos:end_pos].replace(res['matched_text'], color_text) + \
                         res['line'][rest_line:]
            print self.base_string.format(res['filename'], res['no_line'], fixed_line)

    def _machine_print(self):
        for res in self._results:
            print '{0}:{1}:{2}:{3}'.format(res['filename'], res['no_line'], res['start_pos'], res['matched_text'])
            # or if meant to print the whole line - just change res['matched_text'] to res['line'] in previous line

    def _regular_print(self):
        duplicated_line_number = -1
        for res in self._results:
            if duplicated_line_number is not res['no_line']:
                print self.base_string.format(res['filename'], res['no_line'], res['line'])
            duplicated_line_number = res['no_line']

