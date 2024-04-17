import test_sentences

from dynamic_grammar import dynamic_grammar_generator
from nltk import CFG, ChartParser, RecursiveDescentParser, ShiftReduceParser, BottomUpChartParser, BottomUpLeftCornerChartParser, LeftCornerChartParser, LeftCornerChartParser
from nltk.app import rdparser
from nltk.app.rdparser_app import RecursiveDescentApp as RDA
from nltk.parse import recursivedescent as rdp


# rdparser()  # uncomment to run the recursive descent parser demo

with open("thai_grammar.txt", "r") as infile:
    thai_phrase_struct_rules = infile.read()
print(thai_phrase_struct_rules)

thai_cfg = CFG.fromstring(thai_phrase_struct_rules)

sentence = input("\n\nEnter your Thai sentence here: ")
new_cfg = dynamic_grammar_generator(sentence, thai_cfg, lang='th')

RDA(grammar=new_cfg, sent=sentence).mainloop()  # un/comment to toggle visualization tool
