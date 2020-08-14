import settings
import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow


def image_normalisation(image):
  image = cv2.resize(image,(settings.WIDTH,settings.HEIGHT),interpolation = cv2.INTER_AREA)
  image = np.expand_dims(image,axis=0)
  image = image - np.array(settings.IMAGENET_MEAN_RGB_VALUES).reshape((1,1,1,3))
  return image

def image_display(image):
  image = image + np.array(settings.IMAGENET_MEAN_RGB_VALUES).reshape((1,1,1,3))
  image = np.clip(image[0],0,255).astype('uint8')
  plt.imshow(image)
