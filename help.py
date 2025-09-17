import cv2
import numpy as np

name = 'TraneTechnologieslogo'
img = cv2.imread(f'images/{name}.png',cv2.IMREAD_UNCHANGED)

print(img.shape)

new_img = np.zeros((img.shape[1]+20,img.shape[1]+20,4))
print(new_img.shape)
print(int((new_img.shape[0]-img.shape[0])/2))

new_img[int((new_img.shape[0]-img.shape[0])/2):int((new_img.shape[0]+img.shape[0])/2),10:new_img.shape[1]-10,:] = img

ratio = new_img.shape[0]/new_img.shape[1]

img_small = cv2.resize(new_img, (int(275/ratio),275))
print(img_small.shape)

cv2.imwrite(f'images/{name}_small.png', new_img)