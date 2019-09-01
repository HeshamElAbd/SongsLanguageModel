#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 07:23:28 2019

@author: Hesham El Abd
@Description: Mapping the Song text corpa into a numpy array.  
"""
# load the modules:
import numpy as np
import pickle
import os
# load the data
with open("Data/LyricsDataBase.pickle","rb") as input_:
    seqData=pickle.load(input_)

# construct a char 2 Int map and an int to char map:
unique_char=sorted(set(seqData)) # unique chars in the Text corpa
indIdx=np.arange(len(unique_char)) # length matched array of int

char2idx=dict() # a dictionary for mapping a char to an int
for idx in range(len(unique_char)):
    char2idx[unique_char[idx]]=indIdx[idx]
    
idx2char=dict() # a dictionary for mapping an int to char
for idx in range(len(unique_char)):
    idx2char[indIdx[idx]]=unique_char[idx]

# save a local copy to enable the encoding and decoding of model inputs at later stages
os.makedirs("Res",exist_ok=True)
with open("Res/char2idx.pickle","wb") as output_:
    pickle.dump(char2idx,output_)

with open("Res/idx2char","wb") as output_:
    pickle.dump(idx2char,output_)

# Encode the text corpa
encodedSongCorpa=[char2idx[char] for char in seqData]
# save a local copy to the disk:
with open("Data/encodedSongCorpa.pickle","wb") as output_:
    pickle.dump(encodedSongCorpa,output_)








