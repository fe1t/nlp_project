#!/usr/bin/python
# - * - coding: utf-8 - * -
# 1COLUMNS : isCommonDict(w-0), isDictName(w_0), isPrefixOrg(w_0), isPrefixPer(w_0), isInPrefixOrg(w_-7 - w_-2), CLASS
# 2COLUMNS : isCommonDict(w-0), isDictName(w_0), isOrgName(w_0), isPrefixOrg(w_0), isPrefixPer(w_0), isInPrefixOrg(w_-7 - w_-2), CLASS
# CLASS : {per, per_start, per_cont, per_end, org, org_start, org_end}

import glob, sys

def convert_to_utf(filenames):
    for _file in filenames:
        with open(_file, "r") as f:
            data = f.read().decode('TIS-620')
        with open(_file, "w") as f:
            f.write(data.encode('utf8'))

taboo = ["org", "per", "loc"]
person_files = glob.glob("./dictionary/person/*")
org_files = glob.glob("./dictionary/org/*")
common_files = glob.glob("./dictionary/common/*")
# convert_to_utf(common_files)

with open(train, "r") as f:
    data = filter(lambda x: x != "\r\n" and x != " ", f.read().split('|'))

"""
for i in data[10:100]:
    if i == "ว่า":
        print i
"""

