import numpy as np
from PIL import Image
from numpy import savetxt
from os import linesep

img = Image.open("/content/pagpu/3/testImage1.png")
imgArray = np.asarray(img)
print(imgArray.shape)
print((imgArray[:,:,0]/255).max())
colors = ["red", "green", "blue"]
for i in range(3):
    np.savetxt(f'imgs/1/{colors[i]}.txt', imgArray[:,:,i]/255)


pil_image=Image.fromarray(imgArray)
pil_image.show()