# add a dimension to exists ndarray.
np.expand_dims(array, axis=0)

# Swap dimensions
# The follow example swaps dimension from 3 to 1.
a = np.ones((3,4,5,6))
np.rollaxis(a, 3, 1).shape
# >>> (3, 6, 4, 5)
