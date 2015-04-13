# -*- coding: utf-8 -*-
#2015-04-02 
#陈胡
#     通过查找指定项目目录,把最近更新的,指定类型的文件按照目录结构,打包成可以直接在目标主机上面解压的,程序更新包 zip格式
# 参数:
# 1.    要查找的目录 target_dir
# 2.    需求单编号   jira_id
# 3.    文件名列表,读取文件得到 file_names
#
#
#
import os
import zipfile
from myutils import *
import shutil

product_dir = "product"
target_dir = ""
jira_id = ""
file_names = []
seed = 0
for line in open('pack_files.txt'):
	if seed==0:
		target_dir=line.replace("\n", "")
	elif seed==1:
		jira_id = line.replace("\n", "")
	else :
		file_names.append(line.replace("\n", ""))
	seed=seed+1
print("target_dir is : %s" % target_dir)
print("jira_id is : %s" % jira_id)
print "file_names are : " ,file_names 
f = listfiletopack1(target_dir,file_names)
for fl in f :
	print fl
	f = fl[len(target_dir)+1:len(fl)]
	print f
	index = f.rfind(os.sep)
	destDir = os.path.join(jira_id,f[:index])
	copyFiles(fl,os.path.join(product_dir,destDir))
#改变当前目录到 $product_dir
os.chdir(product_dir)
resultdir = os.path.abspath(os.path.join(os.curdir,jira_id));
#压缩文件夹
zip_dir(resultdir,resultdir+".zip")
#删除临时存放文件的文件夹
shutil.rmtree(resultdir)
	

