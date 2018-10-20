"""
output_handler.py: responsible for finding the required type of output and printing in relevant format
"""

base_string = '({0}:{1}) {2}'


class OutputType(object):
    """Class to decide on output type according to given flags"""
    def __init__(self):
        pass

    @staticmethod
    def find_type(flags):
        """Return relevant method according to given flag"""
        if flags.underscore:
            return UnderscoreOutput()
        elif flags.color:
            return ColorOutput()
        elif flags.machine:
            return MachineOutput()
        else:
            return RegularOutput()


class RegularOutput(OutputType):
    """
    If no flags given - regular output: file name + line number + actual line.
    in case of multiple matches on same line - only 1 line will be printed.
    """
    def __init__(self):
        super(RegularOutput, self).__init__()

    def print_output(self, results):
        """Print given results in pre-define format"""
        duplicated_line_number = -1  # here to indicate if there are multiple matches per line
        for res in results:
            if duplicated_line_number is not res['no_line']:  # print output only if it's not same line as before
                print base_string.format(res['file_name'], res['no_line'], res['line'])
            duplicated_line_number = res['no_line']


class UnderscoreOutput(OutputType):
    """
    If -u flag given - underscore output: file name + line number + actual line + '^' under matched text.
    in case of multiple matches on same line - line will be printed several times with underscore for current match.
    """
    def __init__(self):
        super(UnderscoreOutput, self).__init__()

    def print_output(self, results):
        """Print given results in pre-define format"""
        for res in results:
            # calculate output to be printed
            temp_str = base_string.format(res['file_name'], res['no_line'], res['line'])
            # calculate position of matched text. please note that line length is excluded due to nature of 'start_pos'
            current_match_location = len(base_string.format(res['file_name'], res['no_line'], '')) + res['start_pos']
            # calculate index of matched text. in case of several matches per line - str.find() will return 1st match
            # so 'current_match_location' will limit the search for current match
            index = temp_str.find(res['matched_text'], current_match_location)
            if index == -1:
                continue
            print temp_str
            print ''.ljust(index) + '^' * len(res['matched_text'])  # print spaces and then '^'


class ColorOutput(OutputType):
    """
    If -c flag given - color output: file name + line number + actual line + color matched text.
    in case of multiple matches on same line - line will be printed several times will color word for current match.
    """
    def __init__(self):
        super(ColorOutput, self).__init__()

    def print_output(self, results):
        """Print given results in pre-define format"""
        for res in results:
            # define color code
            color_text = '\033[94m' + res['matched_text'] + '\033[0m'
            # define start position index of matched word
            start_pos = res['start_pos']
            # define end position index of matched word
            end_pos = start_pos+len(res['matched_text'])
            # define length of rest of the line
            rest_line = start_pos+len(res['matched_text'])
            # calculate colored line: (line from start till match) + (replace match with colored match) + (rest of line)
            fixed_line = res['line'][:start_pos] + \
                         res['line'][start_pos:end_pos].replace(res['matched_text'], color_text) + \
                         res['line'][rest_line:]
            print base_string.format(res['file_name'], res['no_line'], fixed_line)


class MachineOutput(OutputType):
    """
    If -m flag given - machine output: file_name:no_line:start_pos:matched_text
    in case of multiple matches on same line - new entry will be printed for each match
    """
    def __init__(self):
        super(MachineOutput, self).__init__()

    def print_output(self, results):
        """Print given results in pre-define format"""
        for res in results:
            print '{0}:{1}:{2}:{3}'.format(res['file_name'], res['no_line'], res['start_pos'], res['matched_text'])
            # print results in requested format. assumption was made here that last section will be only matched text
            # if meant to print the whole line - just change res['matched_text'] to res['line'] in previous line
