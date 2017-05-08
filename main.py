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

def cycle_list(start, prefix_checklist):
    start = (start - 7) % 8
    end = (start - 2) % 8
    ans = list()
    while start != end:
        ans.append(prefix_checklist[start])
        start = (start + 1) % 8
    ans.append(prefix_checklist[end])
    return ans

expr = re.compile(r'(.*?)\((per_start|per_cont|per_end|org_start|org_cont|org_end|per|org|loc_start|loc_cont|loc_end|loc)\)')
taboo = ["org", "per", "loc"]
trainer_files = glob.glob("./train/*")
person_files = glob.glob("./dictionary/person/*")
org_files = glob.glob("./dictionary/org/*")
common_files = glob.glob("./dictionary/common/*")
# convert_to_utf(common_files)
learner = list()
common_dict = "./dictionary/common/common_dict.txt"
name_dict = "./dictionary/person/name.txt"
prefix_org = "./dictionary/org/org_prefix.txt"
prefix_person = "./dictionary/person/prefix_person.txt"
# w27_prefix_org = 0
w27_prefix_org = [0, 0, 0, 0, 0, 0, 0, 0]
count = 0

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
        data = filter(lambda x: x != "\r\n" and x != " " and x != "", f.read().split('|'))

    for _data in data:
        row = list()
        _data = _data.replace("\r\n", "").replace(" ", "").replace("\n", "")
        row.append(_data)
        mem_class = "OTHER"
        matched = expr.match(_data)
        if matched:
            _data = matched.group(1)
            if _data == " " or _data == "":
                continue
            _class = matched.group(2)
            row[0] = _data
            if not ("loc" in _class):
                mem_class = _class.upper()
        row.append(1 if _data in common_dict else 0)
        row.append(1 if _data in name_dict else 0)
        # check_org = _data in prefix_org
        # backup_w27_prefix_org = w27_prefix_org
        # w27_prefix_org = 7 if check_org else w27_prefix_org - 1
        if _data in prefix_org:
            w27_prefix_org[count] = 1
            row.append(1)
        else:
            w27_prefix_org[count] = 0
            row.append(0)
        # row.append(1 if _data in prefix_org else 0)
        row.append(1 if _data in prefix_person else 0)
        row.append(1 if 1 in cycle_list(count, w27_prefix_org) else 0)
        row.append(mem_class)
        learner.append(row)
        count = (count + 1) % 8

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
