from camel_tools.morphology.database import MorphologyDB
from camel_tools.morphology.analyzer import Analyzer
from camel_tools.utils.dediac import dediac_ar
from aligner.align_text_api import align_api
from scripts.explainability.ex_explainability import explain_error
import nltk
import itertools

db = MorphologyDB.builtin_db()

# Create analyzer with no backoff
# analyzer = Analyzer(db, backoff="ADD_ALL")


analyzer = Analyzer(db)


def is_atb_tok_valid(original_word, atb_tok_list):
    if original_word != atb_tok_list.replace("+", "").replace("_", ""):
        return False
    return True


def get_all_atb_tok(word, word_type):
    analyses = analyzer.analyze(word)
    posible_atb_splits = []
    for an in analyses:
        # if is_atb_tok_valid(word, dediac_ar(an['atbtok'])):
        if word_type == "correct":
            if an['source'] == 'lex':
                posible_atb_splits.append(dediac_ar(an['atbtok']))
        else:
            posible_atb_splits.append(dediac_ar(an['atbtok']))

    return list(set(posible_atb_splits))


def get_combinations(*args):
    list_cmb = []
    for combination in itertools.product(*args):
        list_cmb.append(combination)
    return list_cmb


def call_get_combinations(get_combinations, args):  # with star
    return get_combinations(*args)


def explain_multi_word_error():
    return ""


def align_single_instance(instance):
    a = " ".join(instance[0].replace("+", "").split("_"))
    i = 0
    b = []
    for e in instance:
        if i > 0:
            b.extend(e.replace("+", "").split("_"))
        i += 1
    return a, " ".join(b)


def get_aligned_combinations(raw_toks, correct_w_possible_tokenizations):
    list_combinations = []
    for e in raw_toks:
        new_l = correct_w_possible_tokenizations[:]
        new_l.insert(0, [e])
        combinations = call_get_combinations(get_combinations, new_l)
        for c in combinations:
            list_combinations.append(align_single_instance(c))
    # print("combs", list_combinations)
    return sorted(list_combinations, key=lambda element: (element[0], element[1]))


def get_atb_multi_word(corrected_multi_word):
    list_atb_toks = []
    for w in corrected_multi_word.split():
        list_atb_toks.append(get_all_atb_tok(w, "correct"))
    # print(list_atb_toks)
    return list_atb_toks


def sort_aligned_combinations(raw_word, corrected_multi_word):
    combos = get_aligned_combinations(raw_word, get_atb_multi_word(corrected_multi_word))

    d = {}
    i = 0
    for e in combos:
        d[i] = (e, nltk.edit_distance(e[0].split(), e[1].split()))
        i += 1
    # print(d)

    index_sort = sorted(d, key=lambda k: d[k][1])
    sorted_d = {}
    i = 0
    for idx in index_sort:
        sorted_d[i] = d[idx]
        i += 1
    # print(sorted_d)
    return sorted_d[0]


def get_explained_error(word, corrected_multi_word):
    try:
        raw_word = get_all_atb_tok(word, "source")
        cmbs_best = sort_aligned_combinations(raw_word, corrected_multi_word)
        alignments = align_api([cmbs_best[0][0]], [cmbs_best[0][1]])
        multi_word_explain = []
        i = 0
        list_err_types = []
        for al in alignments:
            pair_explain = {}
            if len(al.split("\t")) == 4:
                pair_words = al.split("\t")[0], al.split("\t")[2]
                exp_err = explain_error(al.split("\t")[0], al.split("\t")[2])
                pair_explain["raw_correct_pair"] = (pair_words)
                pair_explain["error_type"] = exp_err
                list_err_types.append(exp_err)
                multi_word_explain.append(pair_explain)
            i += 1
        # print(multi_word_explain)
        new_l = list(set(list_err_types))
        if 'uc' in new_l:
            new_l.remove('uc')
        f_new_l = []
        for e in new_l:
            for k in e.split("+"):
                f_new_l.append(k)
    except:
        f_new_l = ['XM']

    return list(set(f_new_l))


# print(get_explained_error("فكانت", "فبعد أن كانت"))

def get_explained_error_subclass(word, corrected_multi_word):
    try:
        raw_word = get_all_atb_tok(word, "source")
        cmbs_best = sort_aligned_combinations(raw_word, corrected_multi_word)
        alignments = align_api([cmbs_best[0][0]], [cmbs_best[0][1]])
        multi_word_explain = []
        i = 0
        list_err_types = []
        for al in alignments:
            pair_explain = {}
            if len(al.split("\t")) == 4:
                pair_words = al.split("\t")[0], al.split("\t")[2]
                exp_err = explain_error(al.split("\t")[0], al.split("\t")[2])
                pair_explain["raw_correct_pair"] = (pair_words)
                pair_explain["error_type"] = exp_err
                list_err_types.append(exp_err)
                multi_word_explain.append(pair_explain)
            i += 1
        # print(multi_word_explain)
        new_l = list(set(list_err_types))
        if 'uc' in new_l:
            new_l.remove('uc')
        f_new_l = []
        for e in new_l:
            for k in e.split("+"):
                f_new_l.append(k)
    except:
        f_new_l = ['XM']

    return list(set(f_new_l))

# print(get_explained_error("فكانت", "فبعد أن كانت"))
