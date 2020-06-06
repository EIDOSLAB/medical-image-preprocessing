import cv2
import numpy as np

#assumption: all the images to process are grey-scale
def imgtonumpy(source):
	img = cv2.imread(path)
	if len(img.shape) > 1:
		img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	return img

def equalize_image(source):
	return cv2.equalizeHist(source)

#intended as contrast enhancement
def normalization(source):
	return cv2.normalize(source,None,0,255,cv2.cv.NORM_MINMAX)

#to binarize the image
def threshold(source, T = 0.5):
	T_int = int(np.round(255 * T))
	ret, equ = cv2.threshold(img, T_int, 255,cv2.THRESH_BINARY)
	return equ

#we assume here sorce dims <= target_dims
#we also assume all the input shapes are even
def shape_same(source, target_dims):
	delta_x = int((target_dims[0] - source.shape[0])/2)
	delta_y = int((target_dims[1] - source.shape[1])/2)
	dest = source.copy()
	if (delta_x > 0) or (delta_y > 0):
		dest = cv2.copyMakeBorder(dest,delta_x,delta_y,delta_y,delta_x,cv2.BORDER_CONSTANT,value=[0,0,0])
	return dest
