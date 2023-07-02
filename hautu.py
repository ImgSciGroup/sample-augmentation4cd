from args import args


def hua(pt_all,temp):
    la=args.la
    for i in range(len(pt_all)):
        for j in range(len(pt_all[i])):
            for m in range(pt_all[i][j].x-8,pt_all[i][j].x+8):
                for n in range(pt_all[i][j].y-8,pt_all[i][j].y+8):
                    if(m>=0 and n>=0and m<la.shape[0] and n<la.shape[1]):
                        if(m==pt_all[i][j].x-8 or m==pt_all[i][j].x+7 or n==pt_all[i][j].y-8 or n==pt_all[i][j].y+7):
                            if(temp==1):
                                la[m,n] = (0,0,255)
                            else:
                                la[m,n]=(255,0,0)
def writetxt(pt_for,f):
    for i in range(len(pt_for)):
        for j in range(len(pt_for[i])):
            f.write(str(pt_for[i][j].x)+"-"+str(pt_for[i][j].y)+",")
        f.write("\n")