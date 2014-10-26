from Tkinter import *
from Replay import *

class DisplayFrame(object):
	"""docstring for DisplayFrame"""
	def __init__(self,size,title=''):
		super(DisplayFrame, self).__init__()
		self.top = Tk()
		self.top.geometry(size)
		self.top.title(title)
		self.TraceList = []
		print 'DisplayFrame is loaded'


	def AddTrace(self,trace):
		self.TraceList.append(trace)

	


class Controler(DisplayFrame):
	"""docstring for Controler"""
	def __init__(self,size,title='',Caller=None):
		super(Controler, self).__init__(size,title)
		# self.label = Label(self.top,text='This is Controler',font = 'Helvetica -12 bold')
		# self.label.pack(fill=Y, expand=0)
		self.Btn_quit = Button(self.top,text='QUIT',command=self.top.quit,activeforeground='white',
								activebackground='red')
		self.Btn_quit.pack(side=BOTTOM)
		if len(self.TraceList) > 0:
			TraceLen = TraceList[0].endtime - TraceList[0].starttime
		else:
			TraceLen = 1
			print 'Warning: No trace is Added'
		self.ProgBar = Scale(self.top,from_=0,to=TraceLen,orient=HORIZONTAL,command=Caller.OnProgBarMove)
		self.ProgBar.pack(fill=X,side=BOTTOM)

	


class ShowPath(DisplayFrame):
	"""docstring for ShowPath"""
	def __init__(self,size,title=''):
		super(ShowPath, self).__init__(size,title)
		# self.label = Label(self.top,text='This is ShowPath',font = 'Helvetica -12 bold')
		# self.label.pack(fill=Y, expand=1)
		self.C = Canvas(self.top,bg='white')
		self.recW = 5
		self.recH = 5
		self.recDict = {}
		self.recStyle = {'L':['red','green'],'R':['blue','white']}
		# self.rec = self.C.create_rectangle(0, 0, self.recW, self.recH, fill="red", outline='green')
		self.C.pack(expand=1)

	#reload
	def AddTrace(self,trace):
		self.TraceList.append(trace)
		rec = self.C.create_rectangle(0, 0, self.recW, self.recH, 
						fill=self.recStyle[trace.tag][0], 
						outline=self.recStyle[trace.tag][1])
		self.recDict.update({trace:rec})

class GUITop(object):
	"""docstring for GUITop"""
	def __init__(self,LTrace,RTrace):
		super(GUITop, self).__init__()
		self.LTrace = LTrace
		self.RTrace = RTrace
		# self.arg = arg
		self.Con = Controler('800x600','Control Panel',Caller=self)		
		self.Show = ShowPath('400x300','Location Trace')
		self.Con.AddTrace(self.LTrace)
		self.Con.AddTrace(self.RTrace)
		self.Show.AddTrace(self.LTrace)
		self.Show.AddTrace(self.RTrace)

		self.Con.top.mainloop()
		self.Show.top.mainloop()


	def CheckTraceLength(self,TraceList):
		if len(TraceList)>1:
			starttime = TraceList[0].starttime
			endtime   = TraceList[0].endtime
			for trace in TraceList:
				if (trace.starttime != starttime) or (trace.endtime != endtime):
					print 'Warning: Start or End time-points of traces are not unified'
					return 0
				else:
					return 1
		else:
			print 'Error: Not enough traces to check length...'
			return -1

	def FitTwoTraces(slef,TA,TB):
		starttime = max([TA.starttime,TB.starttime])
		# TODO: clip the trace

		pass

	def OnProgBarMove(self,ev=None):
		# print self.Con.ProgBar.get()
		
		W = self.Show.recW
		H = self.Show.recH
		for trace in self.Show.TraceList:
			time = trace.starttime + self.Con.ProgBar.get()
			PosX = trace.trace[time].getX()
			PosY = trace.trace[time].getY()
			rec = self.Show.recDict[trace]
			self.Show.C.coords(rec,(PosX, PosY, W+PosX, H+PosY))
		return self.Con.ProgBar.get()
		pass



def main():
	
	rootpath = 'E:\= Workspaces\Git\TraceReplay\LocateRecord'
	filename = '\\10100120_101001200004_20141017132945_1.xml'
	lp = LocPoint(['20141017132946','114.0','36.9'])
	xml = XMLFile(rootpath+filename)
	LTrace = LocTrace([xml.timestamplist_L,xml.Xlist_L,xml.Ylist_L],tag='L')
	RTrace = LocTrace([xml.timestamplist_R,xml.Xlist_R,xml.Ylist_R],tag='R')
	LTrace.LinearInterpolation()
	RTrace.LinearInterpolation()
	# print str(LTrace)
	print LTrace.trace[LTrace.starttime].getTimeStamp()
	G = GUITop(LTrace,RTrace)


	pass

if __name__ == "__main__":
	main()




	


