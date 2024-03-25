from nltk.parse import recursivedescent as rdp
from nltk import CFG, ChartParser, RecursiveDescentParser, ShiftReduceParser, BottomUpChartParser, BottomUpLeftCornerChartParser, LeftCornerChartParser, LeftCornerChartParser
from nltk.app import rdparser
# https://github.com/emilmont/pyStatParser

# rdparser()  # un/comment to toggle visualization tool

# with open("english_grammar.txt", "r") as infile:
#     eng_cfg = infile.read()

# grammar = CFG.fromstring(eng_cfg)
# parser = RecursiveDescentParser(grammar)
# sent = 'the cat chased the dog'.split()
# for tree in parser.parse(sent):
#     print(tree)
# Input Thai sentence
