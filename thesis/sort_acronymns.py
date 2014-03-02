#!/usr/bin/env python

import sys
import re
ac_file = sys.argv[1]

line_map = {}
header = '''\\chapter*{LIST OF ABBREVIATIONS}
\\addcontentsline{toc}{chapter}{LIST OF ABBREVIATIONS}
\\vspace{7mm}
\\begin{acronym}[BLAST]
'''

footer= '''
\\end{acronym}
'''
with open(ac_file) as infile:
    for line in infile:
        if not line.startswith("\\acro"):
            continue
        ac_pattern = re.search("\{(.*)\}\{(.*)\}",line)
        abbreviation = ac_pattern.group(1)
        line_map[abbreviation.lower()] = line

with open(ac_file,'w') as outfile:
    outfile.write(header)
    for key in sorted(line_map):
        outfile.write(line_map[key])
    outfile.write(footer)