import numpy as np
import cv2
from matplotlib import pyplot as plt

            
""" def myhist3(image, n_bins):
    H = np.zeros((n_bins,n_bins,n_bins))
    delitelj = np.float64(256/n_bins)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            indexr = np.uint8(image[i,j,0]/delitelj)
            indexg = np.uint8(image[i,j,1]/delitelj)
            indexb = np.uint8(image[i,j,2]/delitelj)
            H[indexr,indexg,indexb] += 1
    H1 = np.float64(H/(image.shape[0] * image.shape[1]))
    return H1
    pass """
       


img = cv2.imread('data/impressionism/190477.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
Z = img.reshape((-1,3))
Z = np.float32(Z)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 3
ret,label,center=cv2.kmeans (Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

print(center)
print(label)
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((img.shape))

plt.imshow(res2)
plt.show()