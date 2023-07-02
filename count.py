import cv2

from args import args


def count_white_black(image1,image2,image3):
    t23_white = 0
    t12_white = 0
    t12_black = 0
    t23_black = 0
    for i in range(image1.shape[0]):
        for j in range(image1.shape[1]):
            (b, g, r) = image1[i, j]
            (b1, g1, r1) = image2[i, j]
            if ((b, g, r) == (b1, g1, r1)==(0,0,0)):
                t12_black+= 1
            if ((b, g, r) == (b1, g1, r1)==(255,255,255)):
                t12_white+= 1
    for i in range(image1.shape[0]):
        for j in range(image1.shape[1]):
            (b, g, r) = image3[i, j]
            (b1, g1, r1) = image2[i, j]
            if ((b, g, r) == (b1, g1, r1)==(0,0,0)):
                t23_black += 1
            if ((b, g, r) == (b1, g1, r1)==(255,255,255)):
                t23_white += 1
    return (abs(t12_black-t23_black)/(image1.shape[0]*image1.shape[1])),(abs(t12_white-t23_white)/(image1.shape[0]*image1.shape[1]))
def getGailv(im1,im2):
    im1 = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
    im2 = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)
    la=args.la22
    n=im1.shape[0]
    m=im1.shape[1]
    b=0
    w=0
    w1=0
    b1=0
    # for i in range(n):
    #     for j in range(m):
    #         if im1[i,j]==255 and la[i,j]==255:
    #             w=w+1
    #         elif im1[i,j]==0 and la[i,j]==0:
    #             b=b+1
    #         else:
    #             continue
    # for i in range(n):
    #     for j in range(m):
    #         if im2[i,j]==255 and la[i,j]==255:
    #             w1 = w1 + 1
    #         elif im2[i, j] == 0 and la[i, j] == 0:
    #             b1 = b1 + 1
    #         else:
    #             continue
    for i in range(n):
        for j in range(m):
            if im1[i,j]==255 :
                w=w+1
            else:
                b=b+1
    for i in range(n):
        for j in range(m):
            if im2[i,j]==255 :
                w1 = w1 + 1
            else:
                b1=b1+1
    print(b)
    print(b1)
    print(w)
    print(w1)
    return abs(b-b1)/(n*m),abs(w-w1)/(n*m)

