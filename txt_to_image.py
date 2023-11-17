import numpy as np
from PIL import Image
from numpy import savetxt
from os import linesep

def img_from_array(lines):
  mat = np.zeros((imgArray.shape[0],imgArray.shape[1]))

  for i, line in enumerate(lines):
    mat[i, :] = np.array(line.split(' '))[:-1].astype(float)

  img = Image.fromarray(np.uint8(mat * 255) , 'L')
  img.show()

img = Image.open("testImage1(1).png")
imgArray = np.asarray(img)

with open('./imgs/1/output_gpu(1).txt') as f:
    lines = f.readlines()

img_from_array(lines)