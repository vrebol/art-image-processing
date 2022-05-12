import numpy as np
import cv2
from matplotlib import pyplot as plt
from skimage.color import rgb2hsv
from imagereader import readfromdir
from sklearn.cluster import KMeans
from reorganizer import readids, retrieveyears

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
        hm1[k,j] = np.average(hsvimage[:,:,0])
        hm2[k,j] = np.average(hsvimage[:,:,1])
        j+=1
        if j == 25:
            j=0
            k+=1
        l+=1
    return hm1,hm2

#component 0 = hue, 1 = saturation, 2 = value
def getheatmap(list,component):
    heatmap = np.zeros((25,25))
    j = 0
    k = 0
    for i in list:
        heatmap[k,j] = np.average(i[:,:,component])
        j+=1
        if j == 25:
            j=0
            k+=1
    return heatmap 

def computeavgs(component,list):
    avgs = np.zeros(625)
    j=0
    for i in list:
        hsvimage = rgb2hsv(i)
        if j == 0:
            plt.imshow(hsvimage)
        avgs[j] = np.mean(hsvimage[:,:,component])
        j+=1
        print(j)
    return avgs



if __name__ == "__main__":
    """ a = np.load('real.npy',allow_pickle=True)
    image = a[0]
    i1  = rgb2hsv(image)
    print(np.mean(i1[:,:,0]))
    
    avgs = computeavgs(2,a)

    with open('brireal.npy', 'wb') as f:
        np.save(f, avgs) """
    #hm1,hm2 = heatmaps(a)
    #print(a.shape)
    #print(b.shape)
    

    """ with open('hueexpr.npy', 'wb') as f:
        np.save(f, hm1)

    with open('satexpr.npy', 'wb') as f:
        np.save(f, hm2) """

    #hm = getheatmap(b,0)
    #print(hm)


    """ plt.imshow(a,vmin=0,vmax=1,cmap='hot')

    plt.axis('off')
    plt.colorbar()

    plt.show() """

    huereal = np.load('huereal.npy')
    satreal = np.load('satreal.npy')
    brireal = np.load('brireal.npy')

    hueimpr = np.load('hueimpr.npy')
    satimpr = np.load('satimpr.npy')
    briimpr = np.load('briimpr.npy')

    huepimp = np.load('huepimp.npy')
    satpimp = np.load('satpimp.npy')
    bripimp = np.load('bripimp.npy')

    hueexpr = np.load('hueexpr.npy')
    satexpr = np.load('satexpr.npy')
    briexpr = np.load('briexpr.npy')

    a = bripimp.reshape((25,25))

    plt.imshow(a,vmin=0,vmax=1,cmap='pink')

    plt.axis('off')

    plt.show()

    
    """ ids = readids()
    #moveimages(ids)
    years  =retrieveyears(ids)
    a = np.array((years["Realism"],years["Impressionism"], years["Post-Impressionism"],years["Expressionism"]),dtype=object)
    
    file1 = open("real1.txt", "w") 
    row = ["image_id\t","year\t","hue_mean\t", "saturation_mean\t", "brightness_mean\n"]
    file1.writelines(row)

    for i in range(len(hueimpr)):
        row = [str(ids["Realism"][i]) +".jpg\t",str(years["Realism"][i]) + "\t", str(huereal[i]) +"\t", str(satreal[i]) + "\t", str(brireal[i]) + "\n"]
        file1.writelines(row)
    file1.close()  """



    """ a = np.stack((huereal,satreal), axis=-1)
    a = a.reshape(625,2)
    kmeans = KMeans(n_clusters=10, random_state=0).fit(a)
    print(kmeans.cluster_centers_)
    akm = kmeans.cluster_centers_

    b = np.stack((hueimpr,satimpr), axis=-1)
    b = b.reshape(625,2)
    kmeans = KMeans(n_clusters=10, random_state=0).fit(b)
    print(kmeans.cluster_centers_)
    bkm = kmeans.cluster_centers_

    c = np.stack((huepimp,satpimp), axis=-1)
    c = c.reshape(625,2)
    kmeans = KMeans(n_clusters=10, random_state=0).fit(c)
    print(kmeans.cluster_centers_)
    ckm = kmeans.cluster_centers_

    d= np.stack((hueexpr,satexpr), axis=-1)
    d = d.reshape(625,2)
    kmeans = KMeans(n_clusters=10, random_state=0).fit(d)
    print(kmeans.cluster_centers_)
    dkm = kmeans.cluster_centers_

    plt.plot(akm[:,0],akm[:,1],'rx')
    plt.plot(bkm[:,0],bkm[:,1],'gx')
    plt.plot(ckm[:,0],ckm[:,1],'bx')
    plt.plot(dkm[:,0],dkm[:,1],'yx')

    plt.show() """

    
    

""" plt.plot(huereal,satreal,'rx')
    plt.plot(hueimpr,satimpr,'gx')
    plt.plot(huepimp,satpimp,'bx')
    plt.plot(hueexpr,satexpr,'yx')

    plt.show() """


