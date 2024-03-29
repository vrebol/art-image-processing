import numpy as np
import cv2
from matplotlib import pyplot as plt
import os
import json

def readfromdir(name):
    path = name
    images = []
    j=0
    for image in os.listdir(path):
        print(j)
        newpath = path + "/" + image
        I = cv2.imread(newpath)
        I = cv2.cvtColor(I, cv2.COLOR_BGR2RGB)
        images.append(I)
        j+=1
        """ if j == 100:
            break """

    return images
    pass

def retrieveimagesfromid(ids):
    path = "wikiart-saved/images/"
    images = []
    for author in os.listdir(path):
        newpath = path + "/" + author
        for year in os.listdir(newpath):
            newpath1 = newpath + "/" + year
            for image in os.listdir(newpath1):
                nameofimage = os.path.splitext(image)[0]
                if int(nameofimage) in ids:
                    newpath2 = newpath1 + "/" + image
                    I = cv2.imread(newpath2)
                    I = cv2.cvtColor(I, cv2.COLOR_BGR2RGB)
                    images.append(I)
    return images
    pass

def retrieveauthor(path):
    images = []
    for filename in os.listdir(path):
        newpath = path + "/" + filename
        for image in os.listdir(newpath):
            newpath1 = newpath + "/" + image
            I = cv2.imread(newpath1)
            I = cv2.cvtColor(I, cv2.COLOR_BGR2RGB)
            images.append(I)
    return images
    pass

def retrievestyle(path,style):
    ids = []
    for filename in os.listdir(path):
        if filename != "artists.json":
            newpath = path + "/" + filename
            file = open(newpath, encoding='utf-8')
            data = json.load(file)
            for i in data:
                if i["style"] == style:
                    ids.append(i["contentId"])
            file.close()
    return retrieveimagesfromid(ids)
    pass

def retrievestyle1(path,style):
    ids = []
    for filename in os.listdir(path):
        if filename != "artists.json":
            newpath = path + "/" + filename
            file = open(newpath, encoding='utf-8')
            data = json.load(file)
            for i in data:
                if i["style"] == style:
                    ids.append(i["contentId"])
            file.close()
    return ids
    pass

def retrieveauthorstyle(path,style):
    ### probably wont be needed
    pass

def retrieve(style, author):
    path = ""
    if style is None and author is None:
        return 0
    elif style is None and author is not None:
        path = "wikiart-saved/images/" + author
        return retrieveauthor(path)
    elif style is not None and author is None:
        path = "wikiart-saved/meta/"
        return retrievestyle(path,style)
    else:
        path = "wikiart-saved/meta/" + author
        return retrieveauthorstyle(path,style)

def retrievestyleids():
    path = "wikiart-saved/meta/"
    ids1 = retrievestyle1(path,"Realism")
    ids2 = retrievestyle1(path,"Impressionism")
    ids3 = retrievestyle1(path,"Expressionism")
    ids4 = retrievestyle1(path,"Post-Impressionism")
    dict = {}
    dict["Realism"] = ids1
    dict["Impressionism"] = ids2
    dict["Expressionism"] = ids3
    dict["Post-Impressionism"] = ids4
    return dict
    pass


if __name__ == "__main__":
    b = retrieve("Expressionism",None)
    print(len(b))
    plt.imshow(b[0])
    plt.show()
