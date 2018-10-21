"""tests.py: handles some example unit-tests, many tests can be added here."""

import unittest
import re_handling
import output_handler
from cStringIO import StringIO
import sys
from contextlib import contextmanager

results = list()
results.append({'file_name': 'file', 'no_line': 0, 'start_pos': 3,
                'matched_text': 'matched', 'line': 'actual line for matched'})


class TestForInterview(unittest.TestCase):
    def test_re_handling_pass(self):
        """test regex pass"""
        string_for_regex = 'ing'
        regex = re_handling.ReHandling(string_for_regex)
        self.assertEqual(regex.pattern.pattern, string_for_regex, 'regex test failed')

    def test_re_handling_escape_char(self):
        """test regex with escape char"""
        string_for_regex = '%sing'
        regex = re_handling.ReHandling(string_for_regex)
        self.assertEqual(regex.pattern.pattern, '\\' + string_for_regex, 'regex test failed')

    def test_re_handling_search_pass(self):
        """test regex should find search"""
        string_for_regex = 'ing'
        string_to_search_in = 'find ing in data'
        regex = re_handling.ReHandling(string_for_regex)
        res = regex.search_regex_in_data(string_to_search_in).next()
        self.assertEqual(res.start(), 5, 'regex test failed')
        self.assertEqual(res.string, string_to_search_in, 'regex test failed')

    def test_re_handling_search_fail(self):
        """test regex should not find search"""
        string_for_regex = 'inggg'
        string_to_search_in = 'find ing in data'
        regex = re_handling.ReHandling(string_for_regex)
        res = regex.search_regex_in_data(string_to_search_in)
        self.assertEqual(len(list(res)), 0, 'regex test failed')

    def test_regular_output(self):
        """test regular output"""
        expected_string = '(file:0) actual line for matched'
        local_output = handle_stdout(output_handler.RegularOutput())
        self.assertEqual(local_output, expected_string, 'output test failed')

    def test_underscore_output(self):
        """test underscore output"""
        expected_string = '(file:0) actual line for matched\n                         ^^^^^^^'
        local_output = handle_stdout(output_handler.UnderscoreOutput())
        self.assertEqual(local_output, expected_string, 'output test failed')

    def test_color_output(self):
        """test color output"""
        expected_string = '(file:0) actual line for matched'
        local_output = handle_stdout(output_handler.ColorOutput())
        self.assertEqual(local_output, expected_string, 'output test failed')

    def test_machine_output(self):
        """test machine output"""
        expected_string = 'file:0:3:matched'
        local_output = handle_stdout(output_handler.MachineOutput())
        self.assertEqual(local_output, expected_string, 'output test failed')


def handle_stdout(output):
    saved_stdout = sys.stdout
    try:
        out = StringIO()
        sys.stdout = out
        output.print_output(results)
        local_output = out.getvalue().strip()
    finally:
        sys.stdout = saved_stdout
    return local_output


if __name__ == '__main__':
    unittest.main()
