# Thai Syntax Tree Parser
A syntax tree parser for thai

This tool takes in a sentence in Thai and builds all possible syntax trees for a user to see.

There are 2 principle steps taking place here: 
- Part-of-speech tagging and
- Recursive desent parsing.

## Part-of-speech tagging
This tool uses the [pythainlp.tag](https://pythainlp.github.io/dev-docs/api/tag.html) library for part-of-speech tagging.

## Recursive Descent Parsing
We use NLTK to build a Thai parser that operates on the principles of XBar theory. The first step is to create a context-free grammar (CFG). This will depend on the rules of X-bar theory, erring on the side of false positives (read: _overgeneration_). This is a simple .txt file. Then, using NLTK's `parse.RecursiveDescentParser`, all legal interpretations of the sentence are made into trees and offered to the user. Note, we limit the specifier count to _, per Thai's syntactic restrictions (_citation_).

### To Add:
- Why use RecDescPar instead of one of ther other options?
- How many specifiers can Thai have?
- Are specifiers alway right next to the head in Thai, too?
- Is there a limit to the number of legal adjuncts?
- Depending on the above answers, how can we distinguish between the two, especially for the first appearance of both? Maybe rank them wiht a PCFG?


## Extra

Using UTF-8 encoding will allow us to handle Thai orthography. A user will enter a Thai sentence and all parse trees possible under our rules will appear on the screen for them to select from. This will be coded in Python (and maybe some Latex) for easy accessibility.
