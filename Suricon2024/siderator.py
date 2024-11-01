import argparse
import textwrap
import re


parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent('''
siderator.py
Brought to you by:
@da_667
Processes a file containing Suricata (or Snort, I guess...) rules with a blank SID number, automatically applies a new sid number, and writes the output to a new file, for inclusion in your suricata.yaml or snort.conf. For example:

alert tcp any any -> any any (msg:"test_rule"; sid:; rev:1;)

becomes:

alert tcp any any -> any any (msg:"test_rule"; sid:1000000; rev:1;)
'''))

#Setting up the argparser arguments for the input file, output file and sid number. There are default values assign for each argument.

parser.add_argument('-i', dest='infile', required=False, type=str, default="rules.txt", help='File containing a line-separated list of Suricata or Snort rules. Default Value:CURRENT_DIRECTORY/rules.txt')

parser.add_argument('-o', dest='outfile', required=False, type=str, default="local.rules", help='File you wish to write the output of this script to. Will NOT append to an existing file. Default Value:CURRENT_DIRECTORY/local.rules')

parser.add_argument('-s', dest='sid', required=False, type=int, default=1000000, help='Sid number to begin incrementing from. Useful if you want to merge the output from this script into an existing local.rules file. Integer values only. Consider checking sidallocation.org for guidance on how to assign sid numbers to avoid overlapping with existing rulesets. Default Value:1000000')

args = parser.parse_args()

#This turns out to be much simpler than I thought. A with/open opens up the input file and output file for reading and writing respectively. We do some clean-up actions (strip blank space, ignore blank lines, and ignore lines that begin with an octothorpe (#)). We then use regex to replace instances of "sid:" to "sid:[value of args.sid]", and increment the value of args.sid. We also have to insert a newline, because line.strip() blows away the newline char.

with open(args.infile, 'r') as input, open(args.outfile, 'w') as output:
    for line in input:
        line = line.strip
        if line and not line.startswith('#'):
            new_line = re.sub(r'sid:',f'sid:{args.sid}',line)
            output.write(new_line + "\n")
            args.sid+=1
