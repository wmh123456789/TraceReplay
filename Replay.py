from Tkinter import *
from bs4 import BeautifulSoup 

def TestData():
	TimeStempList = ["20141017132946",
					"20141017132948",
					"20141017132949",
					"20141017132951",
					"20141017132952",
					"20141017132954",
					"20141017132956",
					"20141017132958",
					"20141017132959",
					"20141017133000",
					"20141017133002",
					"20141017133003",
					"20141017133005",
					"20141017133006",
					"20141017133008"]

	Xlist = ["114.0" ,
			"115.0" ,
			"115.0" ,
			"113.0" ,
			"109.0" ,
			"108.0" ,
			"106.0" ,
			"102.0" ,
			"100.0" ,
			"99.0" ,
			"98.0" ,
			"101.0" ,
			"102.0" ,
			"101.0" ,
			"101.0" ]
	
	Ylist = ["36.9",
			"37.9",
			"37.9",
			"37.9",
			"35.9",
			"35.9",
			"34.9",
			"34.9",
			"33.9",
			"34.9",
			"34.9",
			"34.9",
			"34.9",
			"35.9",
			"34.9"]
	return [TimeStempList,Xlist,Ylist]
	pass

class LocPoint(object):
	"""docstring for LocPoint"""
	'''
	Two ways to intitialize the Point:
	1 Give timestamp,x,y: [timestamp,x,y]
	2 Give x,y,sec,yyyymm: ['none',x,y,sec,yyyymm]
	sec is the count of the seconds of 'ddhhmmss'
	'''
	def __init__(self, arg):
		super(LocPoint, self).__init__()
		self.TIMESTAMPLENGTH = 14 
		self.timestamp = arg[0]
		self.x = float(arg[1])
		self.y = float(arg[2])
		# print self.timestamp
		if self.timestamp in ['-1','none']:
			if len(arg)>4:
				self.sec = int(arg[3])
				self.yyyymm = arg[4]
				self.timestamp = self.Sec2Timestamp(self.sec,self.yyyymm)
			else:
				print 'ERROR: Cannot find sec or yyyymm info when intitialize a point'
		else:
			self.sec = self.Timestamp2Sec(self.timestamp)
			self.yyyymm = self.timestamp[0:6]
		# print self.sec

	def getTimeStamp(self):
		# print self.timestamp
		return self.timestamp

	def getX(self):
		# print self.x
		return self.x

	def getY(self):
		# print self.y
		return self.y	

	def Timestamp2Sec(self,timestamp):
		if len(timestamp) != self.TIMESTAMPLENGTH:
			print 'ERROR: The format of the timestamp is not "YYYYMMDDHHMMSS"'
			return -1
		else:
			day = int(timestamp[6:8])
			hour = int(timestamp[8:10])
			minute = int(timestamp[10:12])
			second = int(timestamp[12:14])
			# print day,hour,minute,second
			return second+minute*60+hour*3600+day*86400
	

	def Sec2Timestamp(self,sec,yyyymm):
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
		pass


class LocTrace(object):
	"""docstring for LocTrace"""
	def __init__(self, arg, tag = 'unknown'):
		super(LocTrace, self).__init__()
		self.timestamplist = arg[0] #TimeStemp list
		self.xlist = arg[1] # X list
		self.ylist = arg[2] # Y list
		self.xmax = max(self.xlist)
		self.xmin = min(self.xlist)
		self.ymax = max(self.ylist)
		self.ymin = min(self.ylist)
		self.tag = tag
		self.trace = {}
		# intitialize the trace
		for timestamp,x,y in zip(self.timestamplist,self.xlist,self.ylist):
			lp = LocPoint([timestamp,x,y])
			self.trace.update({lp.sec:lp})
		SecList = self.trace.keys()
		SecList.sort()
		self.starttime = SecList[0]
		self.endtime = SecList[-1]

	def RefreshTrace(self):
		SecList = self.trace.keys()
		SecList.sort()
		self.starttime = SecList[0]
		self.endtime = SecList[-1]
		self.timestamplist = []
		self.xlist = []
		self.ylist = []
		for time in SecList:
			lp = self.trace[time]
			self.timestamplist.append(lp.timestamp)
			self.xlist.append(lp.x)
			self.ylist.append(lp.y)
			pass
		self.xmax = max(self.xlist)
		self.xmin = min(self.xlist)
		self.ymax = max(self.ylist)
		self.ymin = min(self.ylist)
		


	def __str__(self):
		SecList = self.trace.keys()
		SecList.sort()
		string = ''
		for i in SecList:
			string+= 'timestamp='+self.trace[i].timestamp
			string+= '\tposX='+str(self.trace[i].x)
			string+= '\tposY='+str(self.trace[i].y)
			string+= '\n'
		return string
		pass

	def LinearInterpolation(self):
		timelist = self.trace.keys()
		timelist.sort()
		start = timelist.pop(0)
		while timelist:
			end = timelist.pop(0)
			if end - start > 1:
				xlen = self.trace[end].x - self.trace[start].x
				ylen = self.trace[end].y - self.trace[start].y
				timestamphead = self.trace[start].timestamp[0:6]
				for i in xrange(start+1,end):
					xi = self.trace[start].x + xlen*(i-start)/(end-start)
					yi = self.trace[start].y + ylen*(i-start)/(end-start)
					pi = LocPoint(['none',xi,yi,i,timestamphead])
					self.trace.update({i:pi})
				pass
			start = end
		pass

	
class XMLFile(object):
	"""docstring for XMLFile"""
	def __init__(self, filepath):
		super(XMLFile, self).__init__()
		self.filepath = filepath
		self.soup = self.ReadXML(self.filepath)
		self.timestamplist_L, self.Xlist_L, self.Ylist_L = self.GetPointInfo(self.soup,'loctp')
		self.timestamplist_R, self.Xlist_R, self.Ylist_R = self.GetPointInfo(self.soup,'realp')
		# self.LTrace = LocTrace([xml.timestamplist_L,xml.Xlist_L,xml.Ylist_L])
		# self.RTrace = LocTrace([xml.timestamplist_R,xml.Xlist_R,xml.Ylist_R])

	def MergeXML(self,xmllist):
		pass


	def ReadXML(self,filepath):
		FileLines = open(filepath,'r').readlines()
		FileText = ' '.join(FileLines)
		# print FileText
		return BeautifulSoup(FileText.decode('GB2312').encode('utf8'))

	def GetPointInfo(self,soup,PType):
		soup.prettify()
		# print str(self.soup)
		LoctP = soup.findAll(PType)
		TimeStampList = [P['timestamp'] for P in LoctP]
		Xlist = [P['posx'] for P in LoctP]
		Ylist = [P['posy'] for P in LoctP]
		return TimeStampList,Xlist,Ylist




def main():
	rootpath = 'E:\= Workspaces\Git\TraceReplay\LocateRecord'
	filename = '\\10100120_101001200004_20141017132945_1.xml'
	lp = LocPoint(['20141017132946','114.0','36.9'])
	xml = XMLFile(rootpath+filename)
	LTrace = LocTrace([xml.timestamplist_L,xml.Xlist_L,xml.Ylist_L])
	RTrace = LocTrace([xml.timestamplist_R,xml.Xlist_R,xml.Ylist_R])
	LTrace.LinearInterpolation()
	
	print str(LTrace)

	pass


if __name__ == "__main__":
	main()