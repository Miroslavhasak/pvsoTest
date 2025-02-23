import cv2
import os
import numpy as np

mosaicFolder = "mozaika"
mosaic_path = os.path.join(mosaicFolder, "mozaika1.jpg")

mosaic = cv2.imread(mosaic_path)

third_image = mosaic[500:1000, 0:500] 

only_red = np.zeros_like(third_image)
only_red[:, :, 2] = third_image[:, :, 2] 

mosaic[500:1000, 0:500] = only_red

mosaic_result_path = os.path.join(mosaicFolder, "mozaikaCervena.jpg") 
cv2.imwrite(mosaic_result_path, mosaic)

cv2.imshow("Mozaika s upravenym tretim obrazkom", mosaic)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Done.")
# cervena