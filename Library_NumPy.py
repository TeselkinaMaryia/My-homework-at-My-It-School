import numpy as np

array_ = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], int)
print(array_.reshape(2, 6),
      array_ * 5,
      array_ > 6,
      np.max(array_),
      np.argmax(array_),
      sep='\n')


