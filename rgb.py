import numpy as np
import cv2
from matplotlib import pyplot as plt
from imagereader import readfromdir
from skimage import data


#Povprečni rgb value za vsako obdobje
#Heatmap za vsako od rgb komponent za vsako obdobje

def averagecomponent(list):
    averageR = 0
    averageG = 0
    averageB = 0
    for i in list:
        averageR += np.average(i[:,:,0])
        averageG += np.average(i[:,:,1])
        averageB += np.average(i[:,:,2])
    averageR = round(averageR/len(list))
    averageG = round(averageG/len(list))
    averageB = round(averageB/len(list))
    print(averageR,averageG,averageB)
    return np.array([[[averageR,averageG,averageB]]])

#component 0 = r, 1 = g, 2 = b
def getheatmap(component,list):
    heatmap = np.zeros((25,25))
    j = 0
    k = 0
    for i in list:
        heatmap[j,k] = round(np.average(i[:,:,component]))
        j+=1
        if j == 25:
            j=0
            k+=1
    return heatmap

    


if __name__ == "__main__":
    
    a = np.load('real.npy',allow_pickle=True)

    #example of getting average color for style
    """ avgColor = averagecomponent(a)

    plt.imshow(avgColor)
    plt.axis('off')
    plt.show()
     """
    hm = getheatmap(2,a)
    
    plt.imshow(hm,vmin=0,vmax=255,cmap='Blues')
    

    plt.axis('off')

    plt.show()
    

   

    

