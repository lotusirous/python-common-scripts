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

# fix random seed for reproducibility
np.random.seed(7)
