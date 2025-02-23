import cv2
import os
import numpy as np

mosaicFolder = "mozaika"
mosaic_path = os.path.join(mosaicFolder, "mozaika1.jpg")

mosaic = cv2.imread(mosaic_path)

kernel = np.array([[0, -1, 0],
                   [-1, 4, -1],
                   [0, -1, 0]]) 

first_image = mosaic[0:500, 0:500]  
first_image_filtered = cv2.filter2D(first_image, -1, kernel)

mosaic[0:500, 0:500] = first_image_filtered

mosaic_kernel = os.path.join(mosaicFolder, "mozaikaKernel.jpg")
cv2.imwrite(mosaic_kernel, mosaic)

cv2.imshow("Mozaika s aplikovanym kernelom", mosaic)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Done.")

# mozaika s kernelom