#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 10:44:42 2019
@author: Hesham El Abd
@Description: Extract the song lyrics from MetroLyrics DataBase 
@DataSource: https://www.kaggle.com/gyani95/380000-lyrics-from-metrolyrics
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pickle
import os
## Loading the DataBase: 
data=pd.read_csv("Data/380000-lyrics-from-metrolyrics/lyrics.csv")
data=data.dropna()
# Average song length:
songCorpa=""
for song in data.lyrics.to_list():
    songCorpa+=song+"$"
##############################
# save the DataBase 
with open("DataBase_Four.pickle","wb") as output_:
    pickle.dump(songCorpa,output_)

    










    

        
    