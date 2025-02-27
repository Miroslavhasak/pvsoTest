from ximea import xiapi
import cv2
import numpy as np

def focusPeakingStack(image,filterPeaks,intensity,colorChanel):
    # ColorChanel = 0-blue 1-green 2-red
    # filterPeaks Value - filters small peaks - 100 good
    # intensity - 35 good
    filterMatrixFocusPeaking = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]], np.float32)
    imageFocus = cv2.filter2D(image, -1, filterMatrixFocusPeaking)
    imageFocusAlpha = np.sum(imageFocus, axis=-1) > filterPeaks  #filterPeaks Value - filters small peaks - 100 good
    imageFocusAlpha = np.uint8(imageFocusAlpha * 255)

    image[:, :, colorChanel] = image[:, :, colorChanel] + (imageFocusAlpha * intensity) # intensity - 35 good
    return image

loadCamera = 1
imageName="saved_image_24.2_"
imagesNum = 4

cam = xiapi.Camera()

#Open camera
if loadCamera:
    print('Opening first camera...')
    cam.open_device()

    #Camera Settings
    cam.set_exposure(50000)
    cam.set_param('imgdataformat', 'XI_RGB32')
    cam.set_param('auto_wb', 1)
    print('Exposure was set to %i us' % cam.get_exposure())

#Open camera END

#Image
img = xiapi.Image()

#Taking pictures
if loadCamera:
    print('Starting the camera')
    cam.start_acquisition() #Turn on camera

    #Taking pictures
    i = 0
    key = 0
    while i < imagesNum and key != ord('c'):
        key = cv2.waitKey()
        cam.get_image(img)
        image = img.get_image_data_numpy()

        image = cv2.resize(image, (700, 700))
        cv2.imshow("Picture taken", image)
        if key == ord(' '):
            # Get Image

            # Save the image
            #fileName = f"saved_image_{i}.jpg"
            fileName = imageName+f"{i}.jpg"
            cv2.imwrite(fileName, image)
            print('Image number taken No. %i.' % i)

            i = i + 1

    print('Stopping the camera')
    cam.stop_acquisition()

    #Stop communication with the camera
    cam.close_device()

#Processing the images
#Loading the images
i=0
imgMemory = [None] * imagesNum
imagesNames = [None] * imagesNum
for i in range(imagesNum):
    #imagesNames[i]= f"saved_image_{i+1}.jpg"
    imagesNames[i] = imageName+f"{i}.jpg"
    imgMemory[i] = cv2.imread(imagesNames[i])

#Image editing
#Image 1 - Kernel mask (3x3)
filterMatrix = np.array([[-1, 0, 1],[-1, 1, 1], [-1, 0, 1]], np.float32)
filterMatrixFocusPeaking = np.array([[0, 1, 0],[1, -4, 1], [0, 1, 0]], np.float32)

#imgMemory[0]=cv2.filter2D(imgMemory[0],-1,filterMatrixFocusPeaking)

#Image 2 - 90deg rotate
img90 = np.zeros(imgMemory[1].shape,dtype=np.uint8)
for i in range(len(imgMemory[1])):
    for j in range(len(imgMemory[1])):
        img90[i, len(imgMemory[1])-j-1] = imgMemory[1][j ,i]

imgMemory[1]=img90

#Image 3 - RGB only Red
imgMemory[2][:,:,0]=0
imgMemory[2][:,:,1]=0
imgRed=imgMemory[2]

imgMemory[2]=imgRed

#Show the pictures
Mozaic=1
if Mozaic:
    #Mozaic
    bigImageTop = np.concatenate((imgMemory[0],imgMemory[1]), axis=1)
    bigImageBottom = np.concatenate((imgMemory[2],imgMemory[3]), axis=1)
    bigImage = np.concatenate((bigImageTop, bigImageBottom), axis=0)

    # Filter
    bigImage[1:len(imgMemory[1]), 1:len(imgMemory[1])] = cv2.filter2D(bigImage[1:len(imgMemory[1]),1:len(imgMemory[1])], -1, filterMatrixFocusPeaking)

    bigImage = cv2.resize(bigImage, (1000, 1000))

    cv2.imshow("OnePicture", bigImage)

    cv2.imwrite('Mosaic_Picture_2x2.jpg', bigImage)

    #Picture info
    parameterMsg=f"The Image parameters:\n- Resolution: {bigImage.shape[1:3]} \n- Size: {bigImage.size} \n- Data type: {bigImage.dtype}"
    print(parameterMsg)




#Waites for the user to end the session by pressing any key
cv2.waitKey(0)
cv2.destroyAllWindows()

print('End of session')


