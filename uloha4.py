import cv2
import os
import numpy as np

mosaicFolder = "mozaika"
mosaic_path = os.path.join(mosaicFolder, "mozaika1.jpg")

mosaic = cv2.imread(mosaic_path)

img_height = 500
img_width = 500

second_image = mosaic[0:500, 500:1000]
rotated_image = np.zeros((img_height, img_width, 3), dtype=np.uint8)  

for i in range(img_height):
    for j in range(img_width):
        rotated_image[j, img_width - 1 - i] = second_image[i, j]  

mosaic[0:500, 500:1000] = rotated_image

mosaic_result_path = os.path.join(mosaicFolder, "mozaikaOtocenie.jpg")
cv2.imwrite(mosaic_result_path, mosaic)

cv2.imshow("Mozaika s otocenym druhym obrazkom", mosaic)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Done.")
# otocenie snimky o 90 stupnov