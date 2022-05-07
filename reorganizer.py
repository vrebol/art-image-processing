import os
from shutil import move
from imagereader import retrievestyleIds

def moveimages(ids):
    path = "wikiart-saved/images/"
    #print(ids["Realism"])
    user = os.getenv('USERNAME')
    real_dir = '/Users/{}/Desktop/projektnaoo/art-image-processing/realism/'.format(user)
    impr_dir = '/Users/{}/Desktop/projektnaoo/art-image-processing/impressionism/'.format(user)
    pimp_dir = '/Users/{}/Desktop/projektnaoo/art-image-processing/post-impressionism/'.format(user)
    expr_dir = '/Users/{}/Desktop/projektnaoo/art-image-processing/expressionism/'.format(user)
   
    for author in os.listdir(path):
        newpath = path + "/" + author
        for year in os.listdir(newpath):
            newpath1 = newpath + "/" + year
            for image in os.listdir(newpath1):
                nameofimage = os.path.splitext(image)[0]  
                if int(nameofimage) in ids["Realism"]:
                    print("hello")
                    newpath2 = newpath1 + "/" + image
                    move(newpath2,real_dir)
                elif int(nameofimage) in ids["Impressionism"]:
                    print("hello")
                    newpath2 = newpath1 + "/" + image
                    move(newpath2,impr_dir)
                elif int(nameofimage) in ids["Post-Impressionism"]:
                    print("hello")
                    newpath2 = newpath1 + "/" + image
                    move(newpath2,pimp_dir)
                elif int(nameofimage) in ids["Expressionism"]:
                    print("hello")
                    newpath2 = newpath1 + "/" + image
                    move(newpath2,expr_dir)
    pass

if __name__ == "__main__":
    ids = retrievestyleIds()
    moveimages(ids)
    pass