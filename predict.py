#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 18:45:05 2020

@author: sudhanshukumar
"""

import numpy as np
import tensorflow as tf
from keras.models import load_model
from keras.preprocessing import image

class dogcat:
    def __init__(self,filename):
        self.filename =filename


    def predictiondogcat(self):
        # load model
        model = tf.keras.models.load_model('dance2.h5')

        # summarize model
        #model.summary()
        imagename = self.filename
        test_image = image.load_img(imagename, target_size = (224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = model.predict(test_image)

        if result[0][0] == 1:
            prediction = 'bharatanatyam'
            return [{ "image" : prediction}]
        elif result[0][1] == 1:
            prediction = 'kathak'
            return [{"image": prediction}]
        elif result[0][2] == 1:
            prediction = 'kathakali'
            return [{"image": prediction}]
        elif result[0][3] == 1:
            prediction = 'Kuchipudi'
            return [{"image": prediction}]
        elif result[0][4] == 1:
            prediction = 'manipuri'
            return [{"image": prediction}]
        elif result[0][5] == 1:
            prediction = 'mohiniyattam'
            return [{"image": prediction}]
        elif result[0][6] == 1:
            prediction = 'odissi'
            return [{"image": prediction}]
        elif result[0][7] == 1:
            prediction = 'sattriya'
            return [{"image": prediction}]



