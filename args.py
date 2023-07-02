import cv2
class args():
         im1=cv2.imread("data/LEVER-138/pred/image1/pre.tif")
         im2=cv2.imread("data/LEVER-138/pred/image2/post.tif")
         la=cv2.imread("data/LEVER-138/pred/label/gt.bmp")
         # d1=[0.8725642381105965,0.8853203689467315,0.8853203689467315]
         im22 = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)
         im11=cv2.cvtColor(im1,cv2.COLOR_BGR2GRAY)
         la22 = cv2.cvtColor(la, cv2.COLOR_BGR2GRAY)
         condi=0.007
         epoch=20
         num_1=0
         num_0=0
         times=3
         patch=16
         patch_ban=8
         # fc=2
         fc=3.5
         gailv=0.9475980065044398
         gailv1=0.77
         path="data/LEVER-138"