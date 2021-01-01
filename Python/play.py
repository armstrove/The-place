# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random
import re

answer="Hellow my firend."

words_of_answer=answer.split(" ")
random.shuffle(words_of_answer)

#for word in words_of_answer:
#    print("{}".format(word))
for i,word in enumerate(words_of_answer):
    print("{}.{}".format(i,word))