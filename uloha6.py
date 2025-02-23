import cv2
import os
import numpy as np

mosaicFolder = "mozaika"
mosaic_path = os.path.join(mosaicFolder, "mozaikaCervena.jpg")

mosaic = cv2.imread(mosaic_path)

print(f"rozmery: {mosaic.shape[0]} x {mosaic.shape[1]} px")
print(f"pocet kanalov: {mosaic.shape[2]}")
print(f"datovy typ: {mosaic.dtype}")
print(f"velkost v pamati: {mosaic.size * mosaic.itemsize} B ({round(mosaic.size * mosaic.itemsize / 1024, 2)} KB)")

print("Done.")
