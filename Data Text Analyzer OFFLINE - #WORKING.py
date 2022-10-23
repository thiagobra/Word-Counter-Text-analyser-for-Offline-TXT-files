# Word Counter Text analyser for Offline TXT files.
# Ouput to an Excel CSV file in the end.

from collections import Counter
from string import punctuation
from time import time
import sys
from pprint import pprint

from pathlib import Path
data = Path('C:\\Users\\Thiago\\Desktop\\marx.txt').read_text() #CHOOSE THE FOLDER WHERE THE .TXT IS

def freq_dist(data):
    """
    :param data: file-like object opened in binary mode or
                 sequence of byte strings separated by '\n'
    :type data: an iterable sequence
    """
    #For readability   
    #return Counter(word for line in data
    #    for word in line.translate(
    #    None,bytes(punctuation.encode('utf-8'))).decode('utf-8').split())

    punc = punctuation.encode('utf-8')
    words = (word for line in data for word in line.translate(punc).split())
    
    return Counter(words)

start = time()
word_dist = freq_dist(data.splitlines())
print('elapsed: {}'.format(time() - start))
pprint(word_dist.most_common(100))

#BELOW IT WILL EXPORT THE OUTPUT INTO A SCV FILE
import csv

with open('data52.csv', 'w', newline='') as f:#CHOOSE THE NAME OF THE .CSV FILE THAT WILL BE GENERATED
    writer = csv.writer(f)
    writer.writerows(word_dist.most_common(100))
