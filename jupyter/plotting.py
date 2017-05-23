%matplotlib inline
from __future__ import print_function # support python 2

# vector utils
import matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from IPython.display import display, Image





# display image in Jupyter
imgpath = "/home/trongkha/sample.png"
display(Image(filename=imgpath))


# convert image to array
# https://stackoverflow.com/questions/22187094/numpy-asarray-image-open-does-not-work
from scipy import misc

# mode='L' convert image to black and white color, reduce dimention.
# https://docs.scipy.org/doc/scipy-0.18.1/reference/generated/scipy.misc.imread.html
image = misc.imread(paths[1], mode='L')/255 
image.shape # check demension, shape format is (row, col)
