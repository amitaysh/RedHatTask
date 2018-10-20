"""
re_handling.py: handles regular expression actions
"""

import re


class ReHandling(object):
    """Will convert string to regex and will search regex matches in data"""
    def __init__(self, regex_args):
        self._regex_args = regex_args
        self.pattern = self._convert_string_to_regex()

    def _convert_string_to_regex(self):
        """compile regex pattern from string. re.escape is used to remove broken regex"""
        res = re.compile(re.escape(self._regex_args), re.MULTILINE)
        if not res:
            raise Exception('Not possible, but seems like given regular expression is broken or empty')
        return res

    def search_regex_in_data(self, data):
        """return ALL matches per line"""
        # no way for exception here since pattern was compiled earlier
        return re.finditer(self.pattern, data)
