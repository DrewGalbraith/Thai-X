from pythainlp.parse import dependency_parsing

def dynamic_pos(text):
    # Perform dependency parsing
    parsing_results = dependency_parsing(text, tag="list")
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

sentence = "พี่น้องชาวบ้านกำลังเลี้ยงสตางค์ในสวน"


# eg.
# dynamic_pos(sentence)  # ['NOUN -> พี่น้อง | ชาวบ้าน | สตางค์ | สวน', 'AUX -> กำลัง', 'VERB -> เลี้ยง', 'ADP -> ใน']