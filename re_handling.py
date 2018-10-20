#!/usr/bin/python
"""
lala
"""

import re


class ReHandling(object):
    def __init__(self, regex_args):
        self._regex_args = regex_args
        self.pattern = self._convert_string_to_regex()

    def _convert_string_to_regex(self):
        res = re.compile(re.escape(self._regex_args), re.MULTILINE)
        if not res:
            raise Exception('Given regular expression is broken or empty')
        return res

    def search_regex_in_data(self, data):
        return re.finditer(self.pattern, data)
