# Thai-X 
Thai-X is a [X-bar](https://en.wikipedia.org/wiki/X-bar_theory) syntax tree parser for the [Thai language](https://en.wikipedia.org/wiki/Thai_language). It's goal is to take a sentence written in Thai and build/export all possible syntax trees for a user using X-Bar theory of syntax.

There are 3 principle steps taking place here: 
- Part-of-speech tagging,
- Tree building,
- Visualization.

## Part-of-speech tagging
This tool uses the [pythainlp.parse](https://pythainlp.github.io/dev-docs/api/parse.html) library for word-based part-of-speech tagging. This tool goes a few steps beyond part-of-speech tagging. First, it handles the seperation of words for Thai text. Thai orthography, unlike English, does not split words based on spaces, instead using whitespace for sentential or phrasal functions. Many part-of-speech taggers (e.g., [pythainlp.tag](https://pythainlp.github.io/dev-docs/api/tag.html) require pre-split words, which is notoriously difficult for rule-based systems working with Khmer-derivative orthographies like Thai (see [here](http://www.thai-language.com/ref/breaking-words#:~:text=Because%20Thai%20doesn%27t%20use%20space%20between%20words%2C%20the%20task%20of%20automatically%20separating%20Thai%20text%20into%20words%20has%20been%20a%20long%2Dstanding%20challenge%20in%20the%20field%20of%20computational%20linguistics.)). The rise of neural tools has overcome this difficulty. Beyond word-splitting, this tool performs the tagging and syntactic relationship labeling for a given sentence. However, this operates under [Universal Dependency](https://universaldependencies.org/) (UD) theory of syntax, not a constituency theory such as X-bar. We will thus use the word-splitting and part-of-speech labeling funcitons, but use our own parser. 

## Building the Syntax Trees
We use NLTK to build a Thai parser that operates on the principles of X-Bar theory. The first step is to create a context-free grammar (CFG). This will depend on the rules of X-bar theory, erring on the side of false positives (read: _overgeneration_). This is a simple .txt file. Then, using NLTK's `parse.RecursiveDescentParser`, all legal interpretations of the sentence are made into trees and offered to the user. Note, we limit the specifier count to _, per Thai's syntactic restrictions (_citation_).

### To Add:
- Why use RecDescPar instead of one of their other options?
- How many specifiers can Thai have?
- Are specifiers alway right next to the head in Thai, too?
- Is there a limit to the number of legal adjuncts?
- Depending on the above answers, how can we distinguish between the two, especially for the first appearance of both? Maybe rank them wiht a PCFG?
- How do we make sure the right X' lines up with the right XP in a given phrase? A rule like `X= N|V|Adj|Adv|P|D` will destroy that. Perhaps modifying [this file](https://github.com/nltk/nltk/blob/develop/nltk/parse/recursivedescent.py) from the [NLTK GitHub](https://github.com/nltk/nltk) will be a good place to start. This could even be an open source contribution!

## Visualization
Visualization is done with LaTeX and stored as .pngs or .pdfs, per user preference.

## Extra

Using UTF-8 encoding will allow us to handle Thai characters.
