import os
import random
import shutil

filePath = "/public/home/zlj/OPenMMLab_AI/mmpretrain/dataset/"
class1=os.listdir(filePath)
# os.mkdir("/data/"+"train/")
# os.mkdir("/data/"+"val/")
for i in class1:
    depath=filePath+i
    print(depath)
    declass=os.listdir(depath)
    delen=len(declass)
    offset=int(delen*0.7)
    random.shuffle(declass)
    sub_class1=declass[:offset]
    sub_class2=declass[offset:]
    os.mkdir("/public/home/zlj/OPenMMLab_AI/mmpretrain/data/train/"+i)
    os.mkdir("/public/home/zlj/OPenMMLab_AI/mmpretrain/data/val/"+i)
    for j in sub_class1:
        oldname=depath+"/"+j
        newname="/public/home/zlj/OPenMMLab_AI/mmpretrain/data/train/"+i+"/"+j
        shutil.copyfile(oldname,newname)
    for j in sub_class2:
        oldname=depath+"/"+j
        newname="/public/home/zlj/OPenMMLab_AI/mmpretrain/data/val/"+i+"/"+j
        shutil.copyfile(oldname,newname)


