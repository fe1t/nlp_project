#!/usr/bin/python
# - * - coding: utf-8 - * -

with open("trainer.crf", "r") as f:
    data = f.readlines()

for _data in data:
    if len(_data.split(' ')) != 7:
        print list(_data)
        print _data
        break
