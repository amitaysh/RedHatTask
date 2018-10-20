# RedHatTask
Red-Hat Task:

This script will search regular expression in file(s) or in stdin (if no files supplied), supplied by the user via command line.
It will print results per matching line.
If there are multiple matches per line - default is to print line only 1 time.
There are several flags that can be sent to script:
 * -u ( --underscore ) will print '^' under the matching text
 * -c ( --color ) will highlight matching text
 * -m ( --machine ) will generate machine readable output:
                  format: file_name:no_line:start_pos:matched_text

Assumption was taken that input is ASCII 
                  
Example: (example_input.txt file is supplied, random text generated from Google)

task.py ling example_input.txt -m

will return:

example_input.txt:3:44:ling
example_input.txt:11:31:ling
