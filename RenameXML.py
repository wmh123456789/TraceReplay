# Rename the trace file(.xml) with the endtime(YYYYMMDDHHMMSS)

import os
from bs4 import BeautifulSoup 
from Replay import *


def Timestamp2Sec(timestamp):
	if len(timestamp) != 14:
		print 'ERROR: The format of the timestamp is not "YYYYMMDDHHMMSS"'
		return -1
	else:
		day = int(timestamp[6:8])
		hour = int(timestamp[8:10])
		minute = int(timestamp[10:12])
		second = int(timestamp[12:14])
		# print day,hour,minute,second
		return second+minute*60+hour*3600+day*86400

def Sec2Timestamp(sec,yyyymm):
	if len(yyyymm) != 6:
		print 'ERROR: The format of the timestamp head is not "YYYYMM"'
		return '-1'
	else:
		day = int(sec)/86400
		sec -= day*86400
		hour = int(sec)/3600
		sec -= hour*3600
		minute = int(sec)/60
		sec -= minute*60
		# print day,hour,minute,sec
		return yyyymm+str(day)+str(hour)+str(minute)+str(sec)


def ReassignTimestamp(RootPath,starttime = None):
	xml = XMLFile(RootPath)
	starttime = xml.soup.recode.locationpoints.loctp['timestamp']
	yyyymm = starttime[0:6]
	# lp = xml.soup.recode.locationpoints.loctp
	# print lp
	# while lp.next != None :
	# 	if lp.next.next != None and lp.next.next != '\n':
	# 		print lp.next.next
	# 		lp = lp.next.next
	# 	pass

	for lp in xml.soup.findAll('loctp'):
		print lp
	print 'finished'
	

	# for dir0,dirs,files in os.walk(RootPath):
	# 	for afile in files:
	# 		print afile
	# 		xml = XMLFile(os.path.join(dir0,afile))
	# 		if starttime == None:
	# 			starttime = xml.soup.recode.locationpoints.loctp['timestamp']
	# 		yyyymm = starttime[0:6]
	# 		print  xml.soup.recode.locationpoints.loctp.next



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
	# RootPath = r"C:\Users\XiaoMing-OfficePC\Desktop\AEON Trace\XMLS"	
	# FilePath = r'C:\Users\XiaoMing-OfficePC\Desktop\AEON Trace\test\test.xml'

	# RenameXML(RootPath)
	
	# FixXMLBug(RootPath)
	# xml = XMLFile(FilePath)
	# xml.soup.recode['starttime'] = 'XXX'
	# xml.WriteXML(filepath = FilePath)
	# print xml.soup.recode.attrs

	RootPath = 'C:\Users\XiaoMing-OfficePC\Desktop\AEON Trace\XML_AEON_SIGNAL'
	FileName = 'Aeon_1F-21_14_75_90_00_03_0e.xml'
	ReassignTimestamp(os.path.join(RootPath,FileName))


	pass


if __name__ == '__main__':
	main()