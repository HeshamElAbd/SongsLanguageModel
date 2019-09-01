#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 10:54:08 2019
@author: Hesham El Abd
@Description:Combing all the database into a one DataBase ready for training 
the model. 
"""
# load the modules: 
import pickle

with open("DataBase_one.pickle","rb") as input_:
    dataBaseOne=pickle.load(input_)

with open("DataBase_Two.pickle","rb") as input_:
    dataBaseTwo=pickle.load(input_)
    
with open("DataBase_Three.pickle","rb") as input_:
    dataBaseThree=pickle.load(input_)

with open("DataBase_Four.pickle","rb") as input_:
    dataBaseFour=pickle.load(input_)

LyricDataBase=dataBaseOne+" "+dataBaseTwo+" "+dataBaseThree+" "+dataBaseFour
print("The size of the Final database is: "+str(len(LyricDataBase)/1e6)+
      " Million chars")
with open("Data/LyricsDataBase.pickle","wb") as output_:
    pickle.dump(LyricDataBase,output_)