#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 15 14:55:36 2018

@author: patiljeevanr
"""

from nltk.tokenize import sent_tokenize, word_tokenize

#nltk.download()

example_text = "Hello Mr. Smith, how are you doing today? The whether is great and python is awesome. The sky is pinkish-blue. You should not eat cardboard."

print(sent_tokenize(example_text))

print(word_tokenize(example_text))

for i in word_tokenize(example_text):
    print(i)