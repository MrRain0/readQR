#-*- coding: utf-8 -*-
# encoding: utf-8
import zbar
import os
from PIL import Image
from os import listdir

rootpath='your path'
dirname_list=listdir(rootpath)
h=[]
def qrScan(imgname):
    #创建图片扫描对象
    scanner = zbar.ImageScanner()
    #设置对象属性
    scanner.parse_config('enable')
    #打开含有二维码的图片
    img = Image.open(imgname).convert('L')
    #获取图片的尺寸
    width, height = img.size

    box = (0,0,width,height)
    cutimg = img.crop(box)
    #建立zbar图片对象并扫描转换为字节信息
    qrCode = zbar.Image(width, height, 'Y800', cutimg.tostring())
    scanner.scan(qrCode)
    data = ''
    for s in qrCode:
        data += s.data
    # 删除图片对象
    del img
    # 输出解码结果
    print repr(data)
    return data
#可以同过简单后缀名判断，筛选出你所需要的文件(这里以.png为例)
for dirname in dirname_list:
    filepath = rootpath + '/' + dirname
    filename_list = listdir(filepath)
    for filename in filename_list:
        if filename[-3:]=='jpg':
            qrdata = qrScan(filepath+'/'+filename)
            qrlist = qrdata.split('\n')
            if(len(qrlist) == 4):
                newname = qrlist[0] + '.jpg'
                if not os.path.exists(filepath + '/' + newname):
                    os.rename(os.path.join(filepath,filename),os.path.join(filepath,newname))
                    # if necessary
                    dirnameU = dirname.decode('gbk').encode('utf-8')
                    newnameU = newname.decode('gbk').encode('utf-8')
                    listline = ''
                    f = open("stored_text.txt","a")
                    f.writelines(listline)
                    f.close()
    
