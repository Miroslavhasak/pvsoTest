import cv2
import os
import numpy as np

outputFolder = "photo"
mosaicFolder = "mozaika"

image_filenames = [f"snimka{i+1}.jpg" for i in range(4)]
images = []

for filename in image_filenames:
    path = os.path.join(outputFolder, filename)
    if os.path.exists(path):
        img = cv2.imread(path)
        images.append(cv2.resize(img, (500, 500)))  
    else:
        print(f"Chyba: Súbor {filename} neexistuje!")
        exit(1)  
        
mosaic = np.vstack([np.hstack([images[0], images[1]]), np.hstack([images[2], images[3]])])
mosaic_path = os.path.join(mosaicFolder, "mozaika1.jpg")

cv2.imwrite(mosaic_path, mosaic)

cv2.imshow("Mozaika", mosaic)
cv2.waitKey(0)
cv2.destroyAllWindows()

print('Done.')

# vytvorenie mozaiky