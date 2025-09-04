import numpy as np
import matplotlib.pyplot as plt
import cv2

# Take notice that OpenCV handles the image as a numpy array when opening it 
img = cv2.imread('/home/Motawe/Downloads/shapes.jpg')
out = img.copy()

hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_red = np.array([0, 120, 70])
upper_red = np.array([10, 255, 255])


mask_r = cv2.inRange(hsv_img, lower_red, upper_red)

out[mask_r > 0] = [255,0,0]

lower_blue = np.array([100, 50, 50])
upper_blue = np.array([130, 255, 255])

mask_b = cv2.inRange(hsv_img, lower_blue, upper_blue)

out[mask_b > 0] = [0,0,0]

lower_black = np.array([0,0,0])
upper_black = np.array([130, 255, 30])

mask_ = cv2.inRange(hsv_img, lower_black, upper_black)

out[mask_ > 0] = [0,0,255]
# Change all pixels that fit within the blue mask to black
# Change all pixels that fit within the red mask to blue
# Change all pixels that fit within the black mask to red

fig, axes = plt.subplots(1, 2)
axes[0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
axes[0].set_title('Original Image')
axes[0].axis('off')

axes[1].imshow(cv2.cvtColor(out, cv2.COLOR_BGR2RGB))
axes[1].set_title('Processed Image')
axes[1].axis('off')

plt.show()