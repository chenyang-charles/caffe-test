import cPickle as pickle
import numpy as np
import os.path
import Image

def get_maxImg(filename, unit_number, unit_size, img_number):
	"""
	Get images with largest average activations
	"""
	mat = pickle.load( open(filename, 'rb'))
	#print mat.shape

	maxImgs = []
	#maxImgs = np.zeros((unit_number, unit_size * img_number))

	for i in range(0, unit_number): 
		activation = sorted(list(np.ndenumerate(mat[:, i, :, :])), key=lambda x:x[1], reverse=True)
		maxImg = [val[0] for val in activation]
		maxImgs.append(maxImg)
		#print len(maxImgs[i])

	return maxImgs

"""
def add_occluder(imgFile):

	# Add occluder to images

	base_dir = os.path.dirname(imgFile)
	while open(imgFile) as fp
		for 
"""

def getImg(index):
	"""
	Read the image listed in the list file with given index
	"""
	lines = 0
	with open("/home/chengyang/SUN2012/Images/a/abbey/index") as fp:
		for line in fp:
			if lines == index and line.strip().split():
				filePath = os.path.join("/home/chengyang/SUN2012/Images/a/abbey", line.strip().split()[0])
				img = Image.open(filePath).resize((227, 227))
				return img
			
			lines = lines + 1
				
def theoreticRF(info, size, stride):
	"""
	Find the theoretic RF part of original images of given info
	"""
	index = info[0]
	#raw_input("Enter")
	x = info[1]
	y = info[2]

	img = getImg(index)
	img_pixels = img.load()

	RF = Image.new('RGB', (size, size), "white")
	RF_pixels = RF.load()

	#RF_pixels = img_pixels[x*stride : x*stride + size, y*stride : y*stride + size]

	for i in range(0, size):
		for j in range(0, size):
			#print i, j, i + x*stride, j + y*stride
			RF_pixels[i, j] = img_pixels[i + x*stride, j + y*stride]

	return RF

maxImgs = get_maxImg('result_pool5', 256, 13*13, 33)

for i in range(0,  len(maxImgs)):
	for j in range(0, 5):
		RF = theoreticRF(maxImgs[i][j], 163, 5)
		RF.save("RFs/" + str(i) + "_" + str(j) + ".jpg")
	
	print i, "/", len(maxImgs), " finished"

