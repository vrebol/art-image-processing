import numpy as np
import cv2
from matplotlib import pyplot as plt
from skimage.color import rgb2hsv
from imagereader import readfromdir

#heatmaps for saturation and hue
#scatter plot with hue and saturation

def heatmaps(list):
    hm1 = np.zeros((25,25))
    hm2 = np.zeros((25,25))
    l=0
    j = 0
    k = 0
    for i in list:
        print(l)
        hsvimage = rgb2hsv(i)
        hm1[j,k] = np.average(hsvimage[:,:,0])
        hm2[j,k] = np.average(hsvimage[:,:,1])
        j+=1
        if j == 25:
            j=0
            k+=1
        l+=1
    return hm1,hm2

#component 0 = hue, 1 = saturation, 2 = value
""" def getheatmap(list,component):
    heatmap = np.zeros((25,25))
    j = 0
    k = 0
    for i in list:
        heatmap[j,k] = np.average(i[:,:,component])
        j+=1
        if j == 25:
            j=0
            k+=1
    return heatmap """


if __name__ == "__main__":
    """ a = np.load('expr.npy',allow_pickle=True)
    hm1,hm2 = heatmaps(a) """
    #print(a.shape)
    #print(b.shape)

    """ with open('hueexpr.npy', 'wb') as f:
        np.save(f, hm1)

    with open('satexpr.npy', 'wb') as f:
        np.save(f, hm2) """

    #hm = getheatmap(b,0)
    #print(hm)

    a = np.load('huereal.npy')
    b = np.load('hueimpr.npy')
    c = np.load('huepimp.npy')
    d = np.load('hueexpr.npy')

    print(np.average(a))
    print(np.average(b))
    print(np.average(c))
    print(np.average(d))

    """ plt.imshow(a,vmin=0,vmax=1,cmap='hot')

    plt.axis('off')
    plt.colorbar()

    plt.show() """
    


