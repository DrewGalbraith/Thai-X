import test_sentences

from dynamic_grammar import dynamic_grammar_generator
from nltk import CFG, ChartParser, RecursiveDescentParser, ShiftReduceParser, BottomUpChartParser, BottomUpLeftCornerChartParser, LeftCornerChartParser, LeftCornerChartParser
from nltk.app import rdparser
from nltk.app.rdparser_app import RecursiveDescentApp as RDA
from nltk.parse import recursivedescent as rdp
from nltk.parse.chart import LeftCornerChartParser as LCP


# rdparser()  # uncomment to run the recursive descent parser demo

with open("thai_grammar.txt", "r") as infile:
    thai_phrase_struct_rules = infile.read()
print(thai_phrase_struct_rules)

sentence = input("\n\nEnter your Thai sentence here: ")  # e.g. "คุณรู้จักผู้ชายมัฟฟินไหม?"
wd_rules = dynamic_grammar_generator(sentence, lang='th')

thai_cfg = CFG.fromstring(thai_phrase_struct_rules + wd_rules)

RDA(grammar=thai_cfg, sent=sentence).mainloop()  # un/comment to toggle visualization tool
