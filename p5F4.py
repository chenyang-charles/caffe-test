import cPickle as pickle
import numpy as np

"""
Get images with largest average activations
"""
mat = pickle.load( open('result_pool5', 'rb'))
#print mat.shape

maxImgs = np.zeros((256, 5577))

for i in range(0, 256): 
    activation = sorted(list(np.ndenumerate(mat[:, i, :, :])), key=lambda x:x[1], reverse=True)
    maxImgs[i] = [val[0][0] for val in activation]
    #print len(maxImgs[i])

"""

"""

