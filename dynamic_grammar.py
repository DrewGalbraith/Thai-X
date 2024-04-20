from pythainlp.parse import dependency_parsing
from nltk import CFG

def pos_tag(text:str, lang:str='th')-> list[list[str]]:

    # Perform dependency parsing
    if lang == 'th':
        parsing_results:list[list[str]] = dependency_parsing(text, tag="list")
    elif lang == 'en':
        parsing_results:list[list[str]] = dependency_parsing(text, tag="list")
    else:
        raise ValueError("Language not supported ATM.")
    
    return parsing_results

    
def dynamic_grammar_generator(sentence:str, lang:str='th')->CFG:


    # Perform POS tagging
    parsing_results = pos_tag(sentence, lang)

    # Build dictionary for cfg
    pos_dict = {}
    for item in parsing_results:
        if item[3] not in pos_dict:
            pos_dict[item[3]] = []  # Create key for PoS
        pos_dict[item[3]].append(item[2])  # Append word to PoS' value list

    # Build strings and append to cfg
    bottom_lvl_rules = ""
    for key, value in pos_dict.items():
        bottom_lvl_rules += f'''\n{key} -> "{'" | "'.join(value)}"'''

    return bottom_lvl_rules

# Example usage
# sentence = "พี่น้องชาวบ้านกำลังเลี้ยงสตางค์ในสวน"
# f= pos_tag(sentence)  # ['NOUN -> พี่น้อง | ชาวบ้าน | สตางค์ | สวน', 'AUX -> กำลัง', 'VERB -> เลี้ยง', 'ADP -> ใน']
