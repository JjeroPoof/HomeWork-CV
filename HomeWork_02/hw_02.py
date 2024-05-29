import cv2
import numpy as np
from matplotlib import pyplot as plt
plt.rcParams['figure.figsize'] = [15, 5]

# Load your image
img = cv2.imread('Sea_03.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Compute the mean values for all three color channels (red, green, blue)
mean_r = np.mean(img[:, :, 0])
mean_g = np.mean(img[:, :, 1])
mean_b = np.mean(img[:, :, 2])

# Compute the coefficients kr, kg, kb
# Note: there are 3 coefficients to compute but we only have 2 equations.
# Therefore, you have to make an assumption, fix the value of one of the
# coefficients and compute the remining two
# Hint: You can fix the coefficient of the brightest colour channel to 1.
if mean_r >= mean_g and mean_r >= mean_b:
    kr = 1.0
    kg = mean_g / mean_r
    kb = mean_r / mean_r
elif mean_g >= mean_r and mean_g >= mean_b:
    kr = mean_r / mean_g
    kg = 1.0
    kb = mean_b / mean_g
else:
    kr = mean_r / mean_b
    kg = mean_g / mean_b
    kb = 1.0

# Apply color balancing to generate the balanced image
balanced = np.zeros_like(img)
balanced[:, :, 0] = img[:, :, 0] * kr
balanced[:, :, 1] = img[:, :, 1] * kg
balanced[:, :, 2] = img[:, :, 2] * kb

# Show the original and the balanced image side by side
plt.subplot(121), plt.imshow(img)
plt.subplot(122), plt.imshow(balanced)