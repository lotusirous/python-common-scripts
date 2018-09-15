%matplotlib inline

# ploting
import matplotlib
import matplotlib.pyplot as plt

# 
import numpy as np
import pandas as pd

# Keras library

from keras.models import Sequential
from keras.layers import Input, Convolution2D, MaxPooling2D, Dense, Dropout, Flatten
from keras.utils import np_utils # utilities for one-hot encoding of ground truth values


# Model visualization
from keras.utils import plot_model
from keras.utils.vis_utils import model_to_dot
from IPython.display import Image, display, SVG

# fix random seed for reproducibility
np.random.seed(7)


def build_model():
  
    model = Sequential()
  
    # Architechure goes here.
    figure = SVG(model_to_dot(model, show_shapes=True).create(prog='dot', format='svg'))
    display(figure)
  
    return model
