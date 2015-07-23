# Rename the trace file(.xml) with the endtime(YYYYMMDDHHMMSS)

import os
from bs4 import BeautifulSoup 
from Replay import *

def RenameXML(RootPath):
	for dir0,dirs,files in os.walk(RootPath):
		for afile in files:
			print afile
			xml = XMLFile(os.path.join(dir0,afile))
			# print xml.soup
			filename = xml.soup.recode['bid'] +'_'+ xml.soup.recode['endtime']+'.xml'
			filedate = xml.soup.recode['endtime'][0:8]
			if not os.path.isdir(os.path.join(dir0,filedate)):
				os.mkdir(os.path.join(dir0,filedate))
			filepath = os.path.join(dir0,filedate,filename)
			xml.WriteXML(filepath = filepath)


def FixXMLBug(RootPath):
	for dir0,dirs,files in os.walk(RootPath):
		for afile in files:
			print afile
			xml = XMLFile(os.path.join(dir0,afile))
			xml.soup.recode['starttime'] = xml.soup.recode.locationpoints.loctp['timestamp']
			xml.soup.recode.realpoints.realp['timestamp'] = xml.soup.recode['starttime']
			# print xml.soup.recode['starttime']
			xml.WriteXML(filepath = os.path.join(dir0,afile))

def main():
	RootPath = r"C:\Users\XiaoMing-OfficePC\Desktop\AEON Trace\XMLS"	
	# FilePath = r'C:\Users\XiaoMing-OfficePC\Desktop\AEON Trace\test\test.xml'

	RenameXML(RootPath)
	
	# FixXMLBug(RootPath)
	# xml = XMLFile(FilePath)
	# xml.soup.recode['starttime'] = 'XXX'
	# xml.WriteXML(filepath = FilePath)
	# print xml.soup.recode.attrs



	pass


if __name__ == '__main__':
	main()