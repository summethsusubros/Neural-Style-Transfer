import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow

image_content= plt.imread('content.jpg')
plt.imshow(image_content)

image_style= plt.imread('style.jpg')
plt.imshow(image_style)
