import math

import cv2
from scipy import spatial

from args import args
from config.MyPoint import Point
from start import save_img
from config.MyPoint import compare
import numpy as np
# 注释的是方差
# def add(iter,pt_arr,im1,im2,la,im22,sort,pt):
#     pt_temp=[]
#     for i in range(len(pt_arr)):
#         point=pt_arr[i]
#         t1=getarr(im22,point)
#         for j in range(point.x-8,point.x+8,15):
#             for k in range(point.y-8,point.y+8,15):
#                 if(j>=8 and k>=8 and j!=point.x and k!=point.y and j<im22.shape[0] and k<im22.shape[1]):
#                    if(compare(Point(j,k),pt)):
#                        continue
#                    t2=getarr(im22,Point(j,k))
#                    if(abs(t1-t2)<=args.fc):
#                        pt_temp.append(Point(j,k))
#                        pt.append(Point(j,k))
#                        save_img(im1,im2,la,iter,j,k,sort)
#     return  pt_temp
# def getarr(im22,point1):
#     sum1=0
#     for i in range(point1.x-8,point1.x+8):
#         for j in range(point1.y-8,point1.y+8):
#                if(i>=0 and j>=0 and i<im22.shape[0] and j<im22.shape[1]):
#                  sum1+=im22[i][j]
#     avg=sum1/256
#     t=0
#     for i in range(point1.x-8,point1.x+8):
#         for j in range(point1.y-8,point1.y+8):
#             if (i >= 0 and j >= 0 and i<im22.shape[0] and j<im22.shape[1]):
#                t+=(avg-im22[i][j])*(avg-im22[i][j])/256
#     return math.sqrt(t)
#余弦距离
# def add(iter,pt_arr,im1,im2,la,im22,sort,pt):
#     pt_temp=[]
#     for i in range(len(pt_arr)):
#         point=pt_arr[i]
#         for j in range(point.x-8,point.x+8,15):
#             for k in range(point.y-8,point.y+8,15):
#                 if(j>=8 and k>=8 and j!=point.x and k!=point.y and j<im22.shape[0] and k<im22.shape[1]):
#                    if(compare(Point(j,k),pt)):
#                        continue
#                    if(getcos(args.im1,args.im2,point)<0.18):
#                        pt_temp.append(Point(j,k))
#                        pt.append(Point(j,k))
#                        save_img(im1,im2,la,iter,j,k,sort)
#     return  pt_temp
# def getcos(im1,im2,point1):
#     sum1=0
#     vec1 = []
#     vec2 = []
#     vec1_1 = []
#     vec2_1 = []
#     vec1_2 = []
#     vec2_2 = []
#     for i in range(point1.x-8,point1.x+8):
#         for j in range(point1.y-8,point1.y+8):
#             vec1.append(im1[i][j][0])
#             vec2.append(im2[i][j][0])
#             vec1_1.append(im2[i][j][1])
#             vec1_2.append(im2[i][j][1])
#             vec2_1.append(im2[i][j][2])
#             vec2_2.append(im2[i][j][2])
#     cos_sim = 1 - spatial.distance.cosine(vec1, vec2)
#     cos_sim1 = 1 - spatial.distance.cosine(vec1_1, vec1_2)
#     cos_sim2 = 1 - spatial.distance.cosine(vec2_1, vec2_2)
#     d2 = []
#     d2.append(cos_sim)
#     d2.append(cos_sim1)
#     d2.append(cos_sim2)
#     d1 = []
#     d1.append(0.8725642381105965)
#     d1.append(0.8853203689467315)
#     d1.append(0.8853203689467315)
#     d1 = np.array(d1)
#     d2 = np.array(d2)
#     dis=np.linalg.norm(d1-d2)
#     return  dis
#皮尔逊
def add(iter,pt_arr,im1,im2,la,im22,sort,pt,startPoint):
    a = args.patch-1
    b = args.patch_ban
    pt_temp=[]
    for i in range(len(pt_arr)):
        point=pt_arr[i]
        for j in range(point.x-b,point.x+b,a):
            for k in range(point.y-b,point.y+b,a):
                if(j>=b and k>=b and j!=point.x and k!=point.y and (j+b)<im22.shape[0] and (k+b)<im22.shape[1]):
                   if(compare(Point(j,k),pt)):
                       continue
                   # t=pierxun(args.im11,im22,Point(j,k),startPoint)
                       # t1= getcos1(args.im1, args.im2, Point(j, k), startPoint)
                       # if (t1==3):
                   a1, a2 = getcos1(args.im1, args.im2, Point(j, k), startPoint)
                   if(a1 >= a2):
                        pt_temp.append(Point(j, k))
                        pt.append(Point(j, k))
                        save_img(im1, im2, la, iter, j, k, sort)
    return  pt_temp
def add1(iter,pt_arr,im1,im2,la,im22,sort,pt,startPoint):
    pt_temp=[]
    a = args.patch - 1
    b = args.patch_ban
    for i in range(len(pt_arr)):
        point=pt_arr[i]
        for j in range(point.x-b,point.x+b,a):
            for k in range(point.y-b,point.y+b,a):
                if(j>=b and k>=b and j!=point.x and k!=point.y and j<im22.shape[0] and k<im22.shape[1]):
                   if(compare(Point(j,k),pt)):
                       continue
                   # t1= getcos1(args.im1, args.im2, Point(j, k), startPoint)
                   # if (t1==3):
                   a1,a2= getcos1(args.im1, args.im2, Point(j, k), startPoint)
                   if (a1<=a2):
                       pt_temp.append(Point(j, k))
                       pt.append(Point(j, k))
                       save_img(im1, im2, la, iter, j, k, sort)
    return  pt_temp
# def pierxun(im1,im2,point1,startPoint):
#     a = args.patch - 1
#     b = args.patch_ban
#     im111=im1[point1.x-b:point1.x+b,point1.y-b:point1.y+b]
#     im222=im2[point1.x-b:point1.x+b,point1.y-b:point1.y+b]
#     im1_1=im1[startPoint.x-b:startPoint.x+b,startPoint.y-b:startPoint.y+b]
#     im2_2=im2[startPoint.x-b:startPoint.x+b,startPoint.y-b:startPoint.y+b]
#
#     # res1=getShang(im111)
#     # res1_1=getShang(im1_1)
#     #
#     # res2_1=getShang(im2_2)
#     # res2=getShang(im222)
#     #
#     # res3=res1_1-res2_1
#     # res4=res1-res2
#     # return abs(res4-res3)
#
#     fc1=getarr(im1,point1)
#     fc2=getarr(im1,startPoint)
#     fc3=getarr(im2,point1)
#     fc4=getarr(im2,startPoint)
#     fc5=fc1-fc3
#     fc6=fc2-fc4
#     return abs(fc5-fc6)
#
#     # t = 0.5 + 0.5 * np.corrcoef(im111, im222, rowvar=0)[0][1]
#     # t1 = 0.5 + 0.5 * np.corrcoef(im1_1, im2_2, rowvar=0)[0][1]
#     # return abs(t-t1)
# def getShang(image):
#     tmp = []
#     for i in range(256):
#         tmp.append(0)
#     val = 0
#     k = 0
#     res = 0
#     img = np.array(image)
#     for i in range(len(img)):
#         for j in range(len(img[i])):
#             val = img[i][j]
#             tmp[val] = float(tmp[val] + 1)
#             k = float(k + 1)
#     for i in range(len(tmp)):
#         tmp[i] = float(tmp[i] / k)
#     for i in range(len(tmp)):
#         if (tmp[i] == 0):
#             res = res
#         else:
#             res = float(res - tmp[i] * (math.log(tmp[i]) / math.log(2.0)))
#
#     return res
# def getarr(im22,point1):
#     sum1=0
#     for i in range(point1.x-8,point1.x+8):
#         for j in range(point1.y-8,point1.y+8):
#                if(i>=0 and j>=0 and i<im22.shape[0] and j<im22.shape[1]):
#                  sum1+=im22[i][j]
#     avg=sum1/256
#     t=0
#     for i in range(point1.x-8,point1.x+8):
#         for j in range(point1.y-8,point1.y+8):
#             if (i >= 0 and j >= 0 and i<im22.shape[0] and j<im22.shape[1]):
#                t+=(avg-im22[i][j])*(avg-im22[i][j])/256
#     return math.sqrt(t)
# #余弦
# def getcos(im1,im2,point2,startPoint1):
#
#     d1=getcos2(im1,im2,point2)
#     d2=getcos2(im1,im2,startPoint1)
#     # val=0
#     # for i in range(3):
#     #     if(d1[i]>=d2[i]):
#     #         val=val+1
#     # return  val
#     d1 = np.array(d1)
#     d2 = np.array(d2)
#     # dis=np.linalg.norm(d1-d2)
#     a1=np.mean(d1)
#     a2=np.mean(d2)
#     return  a1,a2
#
def getcos1(im1,im2,point2,startPoint1):

    d1=getcos2(im1,im2,point2)
    d2=getcos2(im1,im2,startPoint1)
    # val=0
    # for i in range(3):
    #     if(d1[i]<=d2[i]):
    #         val=val+1
    # return val
    d1 = np.array(d1)
    d2 = np.array(d2)
    # dis=np.linalg.norm(d1-d2)
    a1=np.mean(d1)
    a2=np.mean(d2)
    return  a1,a2
def getcos2(im1,im2,point1):
    a = args.patch - 1
    b = args.patch_ban
    vec1 = []
    vec2 = []
    vec1_1 = []
    vec2_1 = []
    vec1_2 = []
    vec2_2 = []
    for i in range(point1.x -b, point1.x + b):
        for j in range(point1.y - b, point1.y +b):
            vec1.append(im1[i][j][0])
            vec2.append(im2[i][j][0])
            vec1_1.append(im1[i][j][1])
            vec1_2.append(im2[i][j][1])
            vec2_1.append(im1[i][j][2])
            vec2_2.append(im2[i][j][2])
    # cos_sim = 1 - spatial.distance.cosine(vec1, vec2)
    # cos_sim1 = 1 - spatial.distance.cosine(vec1_1, vec1_2)
    # cos_sim2 = 1 - spatial.distance.cosine(vec2_1, vec2_2)
    cos_sim = 0.5 + 0.5 * np.corrcoef(vec1, vec2, rowvar=0)[0][1]
    cos_sim1 = 0.5 + 0.5 * np.corrcoef(vec1_1, vec1_2, rowvar=0)[0][1]
    cos_sim2 = 0.5 + 0.5 * np.corrcoef(vec2_1, vec2_2, rowvar=0)[0][1]
    d2 = []
    d2.append(cos_sim)
    d2.append(cos_sim1)
    d2.append(cos_sim2)
    return  d2
# # def getcos(im1,im2,point2,startPoint1):
# #
# #     d1=getcos2(im1,im2,point2)
# #     d2=getcos2(im1,im2,startPoint1)
# #     d1 = np.array(d1)
# #     d2 = np.array(d2)
# #     # dis=np.linalg.norm(d1-d2)
# #     a1=np.mean(d1)
# #     a2=np.mean(d2)
# #     return  a1,a2
# # def getcos2(im1,im2,point1):
# #     vec1 = []
# #     vec2 = []
# #     vec1_1 = []
# #     vec2_1 = []
# #     vec1_2 = []
# #     vec2_2 = []
# #     for i in range(point1.x - 8, point1.x + 8):
# #         for j in range(point1.y - 8, point1.y + 8):
# #             vec1.append(im1[i][j][0])
# #             vec2.append(im2[i][j][0])
# #             vec1_1.append(im1[i][j][1])
# #             vec1_2.append(im2[i][j][1])
# #             vec2_1.append(im1[i][j][2])
# #             vec2_2.append(im2[i][j][2])
# #     cos_sim = 0.5 + 0.5 * np.corrcoef(vec1, vec2, rowvar=0)[0][1]
# #     cos_sim1 = 0.5 + 0.5 * np.corrcoef(vec1_1, vec1_2, rowvar=0)[0][1]
# #     cos_sim2 = 0.5 + 0.5 * np.corrcoef(vec2_1, vec2_2, rowvar=0)[0][1]
# #     d2 = []
# #     d2.append(cos_sim)
# #     d2.append(cos_sim1)
# #     d2.append(cos_sim2)
# #     return  d2