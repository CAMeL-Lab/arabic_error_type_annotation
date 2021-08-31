import codecs
from scripts.explainability.ex_get_explanation_raw_correct import explain_error


def _normalize_punct(s):
    from unicodedata import category
    if len(s) > 2 and category(s[0])[0] == 'P' and s[1] == ' ':
        return s[2:] + s[0]
    elif len(s) == 2 and category(s[0])[0] == 'P' and s[1] == ' ':
        return s[0]
    return s


def annotate(aligned_file, annot_file_out):
    i = 0
    lines = []
    fw = codecs.open(annot_file_out, "w", "utf8")
    with codecs.open(aligned_file, "r", "utf8") as f:
        for l in f:
            if i > 0:
                raw_word = l.split("\t")[0]
                raw_word = raw_word.replace("\r", "")
                correct_word = l.split("\t")[1].replace("\n", "").replace("\r", " ")
                correct_word = _normalize_punct(correct_word)
                if correct_word.startswith(" "):
                    correct_word = correct_word[1:]
                try:
                    explain = explain_error(raw_word, correct_word)
                    line = "\t".join([raw_word, correct_word, "+".join(list(set(explain.split("+"))))]) + "\n"
                    lines.append(line)
                    fw.write(line)
                except:
                    line = "\t".join([raw_word, correct_word, "unk"]) + "\n"
                    lines.append(line)
                    fw.write(line)
            i += 1
    fw.close()
    return "".join(lines)
