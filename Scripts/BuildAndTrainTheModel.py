#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 10:51:15 2019
@author: Hesham El Abd
@Description:using the building blocks of the transformer modules descriped in
as explain in Attention is all you need paper @(https://arxiv.org/abs/1706.03762). 
The impelmentation is based TensorFlow 2 
official tutorial @ https://www.tensorflow.org/beta/tutorials/text/transformer. 
As the current model is a language model, only the encoder part is used.
for more detials regard the building blocks, please check 
https://github.com/HeshamElAbd/SelfAttentionLangModel
"""
# import the modules
from SelfAttentionLangModel.Models import EncoderModels
import numpy as np
import tensorflow as tf
import pickle
# load the numerically encoded data set:
with open("Data/encodedSongCorpa.pickle","rb") as input_:
    encodedSongCorpa=pickle.load(input_)
## Prepare the data for training:
conditionalStringLength=120
numberOfExamplesPerEpoch=len(encodedSongCorpa)//conditionalStringLength
print("Number of Examples per epoch is {} Million Example".format(
        numberOfExamplesPerEpoch/1e6))
# Encode the corpa into a Tensor Flow DataSet
encodedSongCorpaDataSet=tf.data.Dataset.from_tensor_slices(encodedSongCorpa)
dumHolder=[]
for encodedCharStream in encodedSongCorpaDataSet.take(5):
    dumHolder.append(encodedCharStream.numpy())
print("The First five chars in the stream are {}".format(dumHolder))
# the training sequences is generating seqences of length 121 from the datastream.
trainingSequences=encodedSongCorpaDataSet.batch(conditionalStringLength+1,
                                                drop_remainder=True)
## parse the input sequences into training and test tensor
def parseSequenceStream(chunk):
    inputTensor=chunk[:-1]
    outputTensor=chunk[1:]
    return inputTensor, outputTensor
trainigDataSet=trainingSequences.map(parseSequenceStream)
batchSize=64 # a small batch size to train the model 
bufferSize=500 # 500 examples are located in the memory for shuffling
trainigDataSet=trainigDataSet.shuffle(bufferSize).batch(batchSize,drop_remainder=True)

## Building the model:
songModeler=EncoderModels.Modeler(embedding_dim=16,
                                vocabulary_size=86,
                                conditional_string_length=120,
                                num_heads=4,
                                num_encoder_layer=2,
                                num_neuron_pointwise=16,
                                return_attent_weights=False,
                                rate=0.1)
# Compile the model:
songModeler.compile(optimizer="adam",
        loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True))
# fitting the model
songModeler.fit(trainigDataSet,epochs=25)