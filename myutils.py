#-*- coding: utf-8 -*-
#2015-04-02 
#陈胡
import os
import zipfile
import datetime
import codecs

#本函数 通过指定要查找的文件和文件所在的大致目录,查找到文件,并返回文件的绝对路径的列表
# path : 要查找所要打包文件的目录的绝对路径,比如/Volumes/HDD1/work/AAA/workspaces_60/lcims70_hn_lt/webapps
# targetfile : 要打包的文件列表,要求包含文件名和上级目录组成的,比如 iptype/iptype_init.jsp,iptype/iptype_input.jsp,iptype/iptype_perform.jsp
# 返回值 : 要打包的文件绝对路径列表

localtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
file_prefix = datetime.datetime.now().strftime("%Y-%m-%d")
file = codecs.open(file_prefix+'_log.txt', 'a', encoding='utf-8')
def listfiletopack(path,targetfile):
	fis = []
	for root, dirs, files in os.walk(path):
		for f in files:
			fi = os.path.join(root, f)
			subp = os.path.split(fi)
			sub = subp[0]#文件路径
			fn = subp[1]#文件名
			subd = sub[sub.rfind(os.sep)+1:len(sub)]#文件名的上级文件夹名称
			subf = os.path.join(subd,fn)
			if targetfile.count(subf)>0:
				fis.append(fi)
	return fis;
def listfiletopack1(path,targetfile):
	fis = []
	finds = []
	for root, dirs, files in os.walk(path):
		for f in files:
			fi = os.path.join(root, f)
			for tgf in targetfile :
				if tgf in fi:
					fis.append(fi)
					finds.append(tgf)
	line = "%s	Input files number is %d ! \n\n" % (localtime,len(targetfile))
	file.write(line.decode('unicode_escape'))
	line = "%s	I hava found  %d  files ! \n\n" % (localtime,len(fis))
	file.write(line.decode('unicode_escape'))
	
	missing_files = list(set(targetfile).difference(set(finds))) # targetfile中有而finds中没有的
	if(len(missing_files)>0) :
		line  = "%s	missing file count	:	%d \n\n" %(localtime,len(missing_files))
		file.write(line.decode('unicode_escape'))
		line = "%s	The folowing files are missing: \n\n" % (localtime)
		file.write(line.decode('unicode_escape'))
		for f in missing_files :
			tf = str(f)+'\n\n'
			file.write(tf)
		line = "%s	end missing! \n\n" % (localtime)
		file.write(line.decode('unicode_escape'))
	return fis;
	
# 本函数通过指定要打包的文件夹和要打包的文件,把文件拷贝到文件夹内
# sourceFile : 要打包的文件绝对路径
# destDir : 要存放被打包的文件的目录,一般为 jira单号+要打包文件的相对路径,根目录为从webapps下面开始
# 返回值: 无
def copyFiles(sourceFile,destDir):
	if os.path.isfile(sourceFile):
		if not os.path.exists(destDir):
			os.makedirs(destDir)	
		targetfile = os.path.join(os.path.join(os.path.abspath(os.curdir),destDir),os.path.basename(sourceFile))
		open(targetfile,"wb").write(open(sourceFile,"rb").read())

# 本函数通过指定要打包的文件夹的绝对路径,和打包后zip文件的名称的绝对路径,来把文件夹内的文件打包成zip文件
# dirname : 要打包的文件夹的绝对路径
# zipfilename : 最终生成的zip文件的绝对路径
def zip_dir(dirname,zipfilename):
	filelist = []
	if os.path.isfile(dirname):
		filelist.append(dirname)
	else :
		for root, dirs, files in os.walk(dirname):
			for name in files:
				filelist.append(os.path.join(root, name))		 
	zf = zipfile.ZipFile(zipfilename, "w", zipfile.zlib.DEFLATED)
	for tar in filelist:
		arcname = tar[len(dirname):]
		zf.write(tar,arcname)
	zf.close()
# 本函数自动根据当前操作系统类型,把路径分隔符替换成当前操作系统的分隔符,防止把linux和ms winddows分隔符写混淆
# filename : 文件路径
def format_file_sep(filename):
	return filename.replace("\\", os.sep).replace("/", os.sep)


