#!/usr/bin/python
# - * - coding: utf-8 - * -

# 1COLUMNS : isCommonDict(w-0), isDictName(w_0), isPrefixOrg(w_0), isPrefixPer(w_0), isInPrefixOrg(w_-7 - w_-2), CLASS
# 2COLUMNS : isCommonDict(w-0), isDictName(w_0), isOrgName(w_0), isPrefixOrg(w_0), isPrefixPer(w_0), isInPrefixOrg(w_-7 - w_-2), CLASS
# CLASS : {per, per_start, per_cont, per_end, org, org_start, org_cont, org_end}

import glob, sys, re

def convert_to_utf(filenames):
    for _file in filenames:
        with open(_file, "r") as f:
            data = f.read().decode('TIS-620')
        with open(_file, "w") as f:
            f.write(data.encode('utf8'))

def read_format(f):
    return [ _data.rstrip() for _data in f.readlines() ]

expr = re.compile(r'(.*?)\((per_start|per_cont|per_end|org_start|org_cont|org_end|per|org)\)')
taboo = ["org", "per", "loc"]
trainer_files = glob.glob("./train/*")
person_files = glob.glob("./dictionary/person/*")
org_files = glob.glob("./dictionary/org/*")
common_files = glob.glob("./dictionary/common/*")
# convert_to_utf(common_files)
learner = list()
common_dict = common_files[2]
name_dict = person_files[6]
prefix_org = org_files[15]
prefix_person = person_files[-1]
w27_prefix_org = 0
with open(common_dict, 'r') as f:
    common_dict = read_format(f)
with open(name_dict, 'r') as f:
    name_dict = read_format(f)
with open(prefix_org, 'r') as f:
    prefix_org = read_format(f)
with open(prefix_person, 'r') as f:
    prefix_person = read_format(f)

# trainer_files = ["./train/98JUL5_2.txt"]
for trainer in trainer_files:
    with open(trainer, "r") as f:
        data = filter(lambda x: x != "\r\n" and x != " ", f.read().split('|'))

    for _data in data:
        row = list()
        row.append(_data)
        row.append(1 if _data in common_dict else 0)
        row.append(1 if _data in name_dict else 0)
        check_org = _data in prefix_org
        w27_prefix_org = 7 if check_org else w27_prefix_org - 1
        row.append(1 if check_org else 0)
        row.append(1 if _data in prefix_person else 0)
        row.append(1 if w27_prefix_org > 1 else 0)
        matched = expr.match(_data)
        if matched:
            word = matched.group(1)
            _class = matched.group(2)
            row[0] = word
            row.append(_class.upper())
        else:
            row.append("OTHER")
        learner.append(row)
        if w27_prefix_org < 0:
            w27_prefix_org = 0

# if want True False
"""
with open("trainer.ctf", "w") as f:
    for _learner in learner:
        f.write(" ".join([ str(__learner) if type(__learner) == bool else __learner for __learner in _learner]) + "\n")
"""

# if want 0 1
with open("trainer.crf", "w") as f:
    for _learner in learner:
        f.write(" ".join([ str(__learner) for __learner in _learner ]) + "\n")
