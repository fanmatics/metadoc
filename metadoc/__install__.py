#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import nltk
import time
from .extract.pos import do_train

def install():
  REQUIRED_CORPORA = [
    'brown', # Required for FastNPExtractor
    'punkt', # Required for WordTokenizer
    'wordnet', # Required for lemmatization and Wordnet
    'maxent_ne_chunker',
    'stopwords',
    'words' 
  ]

  for each in REQUIRED_CORPORA:
    print(('[+] Downloading corpus:  "{0}"'.format(each)))
    nltk.download(each)

  print('[+] Training tagger now.')
  do_train()

if __name__ == "__main__":
  install()