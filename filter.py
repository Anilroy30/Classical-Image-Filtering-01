import cv2
import matplotlib.pyplot as plt
import numpy as np

# Load the image (using your Sample-1.jpg)
img = cv2.imread('Sample-1.jpg')  # Make sure this matches your file name exactly
if img is None:
    print("Error: Image not found! Check the file name and path.")
    exit()

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Apply different filters
mean_blur = cv2.blur(img_rgb, (7, 7))  # Mean filter
gaussian_blur = cv2.GaussianBlur(img_rgb, (7, 7), 0)  # Gaussian filter
median_blur = cv2.medianBlur(img_rgb, 7)  # Median filter

# Display results
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

axes[0, 0].imshow(img_rgb)
axes[0, 0].set_title('Original Image', fontsize=14, fontweight='bold')
axes[0, 0].axis('off')

axes[0, 1].imshow(mean_blur)
axes[0, 1].set_title('Mean Filter (Averaging)', fontsize=14, fontweight='bold')
axes[0, 1].axis('off')

axes[1, 0].imshow(gaussian_blur)
axes[1, 0].set_title('Gaussian Filter (Weighted Averaging)', fontsize=14, fontweight='bold')
axes[1, 0].axis('off')

axes[1, 1].imshow(median_blur)
axes[1, 1].set_title('Median Filter (Noise Reduction)', fontsize=14, fontweight='bold')
axes[1, 1].axis('off')

plt.tight_layout()
plt.savefig('output_filters.png', dpi=300, bbox_inches='tight')  # Save the output
plt.show()

print("Success! Output saved as 'output_filters.png'")
