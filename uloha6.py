import cv2
import os
import numpy as np

# Priečinok a cesta k mozaike
mosaicFolder = "mozaika"
mosaic_path = os.path.join(mosaicFolder, "mozaika1.jpg")

# Načítanie existujúcej mozaiky
mosaic = cv2.imread(mosaic_path)

if mosaic is None:
    print(f"Chyba: Súbor {mosaic_path} neexistuje!")
    exit(1)

# Výpis základných informácií o obrázku
print(f"rozmery: {mosaic.shape[0]} x {mosaic.shape[1]} px")
print(f"pocet kanalov: {mosaic.shape[2]}")
print(f"datovy typ: {mosaic.dtype}")
print(f"velkost v pamati: {mosaic.size * mosaic.itemsize} B ({round(mosaic.size * mosaic.itemsize / 1024, 2)} KB)")

# Predpokladaná veľkosť jednotlivých obrázkov v mozaike
img_height = mosaic.shape[0] // 2  # Polovica výšky mozaiky
img_width = mosaic.shape[1] // 2   # Polovica šírky mozaiky

# Vystrihnutie tretieho obrázka (ľavý dolný kvadrant)
third_image = mosaic[img_height:img_height * 2, 0:img_width].copy()

# Zachovanie len červeného kanála (R)
only_red = np.zeros_like(third_image)
only_red[:, :, 2] = third_image[:, :, 2]  # Kopírujeme len červený kanál

# Nahradenie tretieho obrázka v mozaike upravenou verziou
mosaic[img_height:img_height * 2, 0:img_width] = only_red

# Uloženie mozaiky
mosaic_result_path = os.path.join(mosaicFolder, "mozaika_upravena.jpg")
cv2.imwrite(mosaic_result_path, mosaic)

# Zobrazenie mozaiky
cv2.imshow("Mozaika s upravenym tretim obrazkom", mosaic)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Done.")
