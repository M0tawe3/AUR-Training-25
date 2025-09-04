import numpy as np
import matplotlib.pyplot as plt
import cv2

def convolve(image, kernel):
    
    kernel = np.flipud(np.fliplr(kernel))

    k_h, k_w = kernel.shape
    img_h, img_w = image.shape

    padded_image = np.pad(image, ((k_h // 2, k_h // 2), (k_w // 2, k_w // 2)))

    filtered = np.zeros((img_h, img_w))

    for i in range(img_h):
        for j in range(img_w):
            filtered[i, j] = np.sum(padded_image[i:i + k_h, j:j + k_w] * kernel)

    filtered = np.clip(filtered, 0, 255)

    return filtered

# Load image
img = cv2.imread('/home/Motawe/Downloads/image.jpg', cv2.IMREAD_GRAYSCALE)
fig, axes = plt.subplots(2, 2, figsize=(8, 8))

axes[0, 0].imshow(img, cmap='gray')
axes[0, 0].set_title('Original Image')
axes[0, 0].axis('off')

axes[0, 1].imshow(convolve(img, np.ones((5, 5)) / 25), cmap='gray')
axes[0, 1].set_title('Box Filter')
axes[0, 1].axis('off')

axes[1, 0].imshow(convolve(img, np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])), cmap='gray')
axes[1, 0].set_title('Horizontal Sobel Filter')
axes[1, 0].axis('off')

axes[1, 1].imshow(convolve(img, np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])), cmap='gray')
axes[1, 1].set_title('Vertical Sobel Filter')
axes[1, 1].axis('off')

plt.show()