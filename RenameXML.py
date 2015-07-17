# Rename the trace file(.xml) with the endtime(YYYYMMDDHHMMSS)

import os
from bs4 import BeautifulSoup 
from Replay import *

RootPath = "C:\Users\XiaoMing-OfficePC\Desktop\AEON Trace\XMLS"
for dir0,dirs,files in os.walk(RootPath):
	for afile in files:
		xml = XMLFile(os.path.join(dir0,afile))
		# print xml.soup
		filename = xml.soup.recode['bid'] +'_'+ xml.soup.recode['endtime']+'.xml'
		filedate = xml.soup.recode['endtime'][0:8]
		if not os.path.isdir(os.path.join(dir0,filedate)):
			os.mkdir(os.path.join(dir0,filedate))
		filepath = os.path.join(dir0,filedate,filename)
		xml.WriteXML(filepath = filepath)




def main():
	pass


if __name__ == '__main__':
	main()