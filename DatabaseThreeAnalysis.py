#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 10:27:15 2019
@author: Hesham El Abd
@Description: Extract the song lyrics from SongLyric DataBase 
@DataSource: https://www.kaggle.com/paultimothymooney/poetry
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pickle
import os
## Loading the DataBase: 
songCorpa=""
baseDir=os.path.join(os.getcwd()+"/Data/poetry/")
textFiles=os.listdir(baseDir)
for afile in textFiles:
    with open(os.path.join(baseDir+"/"+afile),"r") as input_:
        for line in input_:
            songCorpa+=line
        songCorpa+="$"
        
with open("DataBase_Three.pickle","wb") as output_:
    pickle.dump(songCorpa,output_)
    

        
    