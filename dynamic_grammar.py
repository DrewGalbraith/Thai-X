from pythainlp.parse import dependency_parsing
from nltk import CFG

def pos_tag(text, lang='th'):


    # Perform dependency parsing
    if lang == 'th':
        parsing_results = dependency_parsing(text, tag="list")
    elif lang == 'en':
        parsing_results = dependency_parsing(text, tag="list")
    else:
        raise ValueError("Language not supported ATM.")
    
    return parsing_results
    
def dynamic_grammar_generator(sentence:str, cfg:CFG, lang:str='th'):


    # Perform POS tagging
    parsing_results = pos_tag(sentence, lang)

    # Build dictionary for cfg
    pos_dict = {}
    for item in parsing_results:
        if item[3] not in pos_dict:
            pos_dict[item[3]] = []
        pos_dict[item[3]].append(item[2])

    # Build strings for cfg
    append_to_cfg = []
    for key, value in pos_dict.items():
        append_to_cfg.append(f"{key} -> {' | '.join(value)}")

    return append_to_cfg

# eg.
# dynamic_pos(sentence)  # ['NOUN -> พี่น้อง | ชาวบ้าน | สตางค์ | สวน', 'AUX -> กำลัง', 'VERB -> เลี้ยง', 'ADP -> ใน']