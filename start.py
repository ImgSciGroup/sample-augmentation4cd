import random

import cv2

from args import  args
from config.MyPoint import Point

#最初
def start01(pt):
    pt_arr1 = []
    la=args.la22
    i1=0
    a=args.patch
    while(i1<args.times):
        i = random.randint(a, la.shape[0] - a)
        j = random.randint(a, la.shape[1] - a)
        if(la[i,j]==255):
            pt_arr1.append(Point(i,j))
            i1+=1
    pt_arr0 = []
    i0=0
    while (i0 < args.times):
        i = random.randint(a, la.shape[0] - a)
        j = random.randint(a, la.shape[1] - a)
        if (la[i, j] == 0):
            pt_arr0.append(Point(i, j))
            i0 += 1


    for i in range(len(pt_arr0)):
        pt.append(pt_arr0[i])
    for i in range(len(pt_arr1)):
        pt.append(pt_arr1[i])

    return pt_arr1, pt_arr0

def save_img(im1,im2,la,iter,x,y,sort):
    a=args.patch
    b=args.patch_ban
    temp_x=x
    temp_y=y
    x=x-b
    y=y-b
    x1=x+a
    y1=y+a
    im3=im1[x:x1,y:y1]
    im4=im2[x:x1,y:y1]
    la1=la[x:x1,y:y1]
    cv2.imwrite(args.path+"/im1/"+str(iter)+"_"+str(sort)+"_"+str(temp_x)+"_"+str(temp_y)+".bmp",im3)
    cv2.imwrite(args.path + "/im2/" + str(iter) +"_"+str(sort)+ "_" + str(temp_x)+"_"+str(temp_y) + ".bmp", im4)
    cv2.imwrite(args.path + "/label/" + str(iter)+"_" + str(sort)+"_" + str(temp_x)+"_"+str(temp_y) + ".bmp", la1)
    if (sort == 0):
        args.num_0 += 1
    else:
        args.num_1 += 1

def save_img1(im1,im2,la,iter,pt,sort):
    a = args.patch
    b = args.patch_ban
    for i in range(len(pt)):

        x=pt[i].x-b
        y=pt[i].y-b
        x1=x+a
        y1=y+a
        im3=im1[x:x1,y:y1]
        im4=im2[x:x1,y:y1]
        la1=la[x:x1,y:y1]
        cv2.imwrite(args.path+"/im1/"+str(iter)+"_"+str(sort)+"_"+str(pt[i].x)+"_"+str(pt[i].y)+".bmp",im3)
        cv2.imwrite(args.path + "/im2/" + str(iter) +"_"+str(sort)+ "_" + str(pt[i].x) + "_" + str(pt[i].y) + ".bmp", im4)
        cv2.imwrite(args.path + "/label/" + str(iter)+"_" + str(sort)+"_" + str(pt[i].x) + "_" + str(pt[i].y) + ".bmp", la1)
        if(sort==0):
            args.num_0+=1
        else:
            args.num_1+=1

