import cv2

from config.MyPoint import Point
from args import  args
from count import count_white_black, getGailv
from hautu import hua, writetxt
from model.FMUnt import FMUnet
from start import start01, save_img, save_img1
from train import  train_net
from test import test
from adddemo import add, add1

if __name__ == "__main__":

    iter=1
    # 第一次train,test
    im1=args.im1
    im2=args.im2
    im22=args.im22
    la=args.la
    pt_com=[]
    net=FMUnet(3,3)
    pt_all1=[]
    pt_all0=[]
    pt_1,pt_0=start01(pt_com)
    list=[]
    length=len(pt_0)
    for i in range(0,len(pt_0) *2):
        list.append([])
    for i in range(0,length* 2):
        if (i < len(pt_0)):
            list[i].append(pt_1[i])
        else:
            list[i].append(pt_0[i - len(pt_0)])
    a=args.patch_ban
    save_img1(im1,im2,la,iter,pt_1,1)
    save_img1(im1,im2,la,iter,pt_0,0)
    pt_all1.append(pt_1)
    pt_all0.append(pt_0)
    loss_to=[]
    device='cpu'
    modelName="siam"
    f_acc=open('txt/test_acc.txt', 'w')
    f_init=open('txt/params.txt', 'w')
    f_init.write("condi:"+str(args.condi)+"  epoch:"+str(args.epoch)+" fc:"+str(args.fc))
    f_time=open('txt/test_time.txt', 'w')
    f_acc_train = open('txt/train_acc.txt', 'w')
    f_time_train = open('txt/train_time.txt', 'w')
    f_landsat_c = open('txt/f_landsat_c.txt', 'w')
    f_landsat_uc = open('txt/f_landsat_uc.txt', 'w')
    f_epoch_loss=open('txt/f_epoch_loss.txt', 'w')
    f_nums=open('txt/f_nums.txt', 'w')
    batch_size=3
    condi=args.condi
    while(iter<=2):
            loss_to=train_net(f_acc_train,f_time_train,f_epoch_loss,iter,net,device,args.path,args.epoch,3,modelName,is_Transfer=False)
            test(net, iter, f_acc, f_time,modelName)
            iter+=1
            for i in range(0, length):
                list[i] = add1(iter, list[i], im1, im2, la, im22, 1, pt_com, pt_1[i])
                pt_all1.append(list[i])
            for i in range(length,length * 2):
                list[i] = add(iter, list[i], im1, im2, la, im22,0,pt_com,pt_0[i-length])
                pt_all0.append(list[i])
            batch_size+=1
    while(True):
        loss_to=train_net(f_acc_train,f_time_train,f_epoch_loss,iter, net, device, args.path,args.epoch, 3, modelName, is_Transfer=False)
        test(net, iter, f_acc, f_time, modelName)
        image1 = cv2.imread(args.path + "/pred/result/pre_" + (str(iter - 2) + ".png"))
        image2 = cv2.imread(args.path + "/pred/result/pre_" + (str(iter - 1) + ".png"))
        image3 = cv2.imread(args.path + "/pred/result/pre_" + (str(iter) + ".png"))
        black, white = count_white_black(image1, image2, image3)
        if (black < condi and white < condi):
            for i in range(len(loss_to)):
                f_epoch_loss.write(str(loss_to[i])+"\n")
            break
        if(black>=condi):
            for i in range(length, length * 2):
                list[i] = add(iter, list[i], im1, im2, la, im22, 0, pt_com, pt_0[i - length])
                pt_all0.append(list[i])
        if(white>=condi):
                for i in range(0, length):
                    list[i] = add1(iter, list[i], im1, im2, la, im22, 1, pt_com, pt_1[i])
                    pt_all1.append(list[i])
        iter+=1
        batch_size+=1
    hua(pt_all1,1)
    hua(pt_all0,0)
    writetxt(pt_all0,f_landsat_uc)
    writetxt(pt_all1,f_landsat_c)
    # cv2.imshow("ss",im22)
    cv2.imwrite("./data/LEVER-138/pred/res.png",la)
    cv2.waitKey(0)
    f_nums.write("0： "+str(args.num_0)+"---1："+str(args.num_1))
    f_acc.close()
    f_time.close()
    f_landsat_c.close()
    f_landsat_uc.close()
    f_acc_train.close()
    f_time_train.close()
    f_epoch_loss.close()
    f_init.close()
    f_nums.close()