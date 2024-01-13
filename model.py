import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.layers import Input, Conv2D, Dense, Flatten, Dropout
from tensorflow.keras.layers import GlobalMaxPooling2D, MaxPooling2D
from tensorflow.keras.layers import BatchNormalization
from tensorflow.keras.models import Model
from tensorflow.keras.models import load_model

class styleModels:
  def __init__(self, model_type):
    if model_type == "baroque":
       self.model = load_model('models/baroque_model.h5')
    elif model_type == "new":
       self.model = load_model('models/New_hampshire_mode.h5')
    elif model_type == "cubism":
      self.newHampshire_model = load_model('models/cubism.h5')
    elif model_type == "impressionism":
      self.model = load_model('models/expressionism.h5')
    elif model_type == "pop_art":
       self.model = load_model('models/pop_art.h5')
    elif model_type == "surrealism":
       self.model = load_model('models/surrealism.h5')
    
   
    return
  def process_image(self,file_path, processing_type):
    pass
    
    processing_type = processing_type.lower()
    if processing_type == "baroque":
      #generate the image and return to the server
      self.baroque_model.predict(file_path)
      return 
    elif processing_type == "new":
      return
      
  