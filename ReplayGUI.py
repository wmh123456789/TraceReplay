from Tkinter import *
import tkFileDialog
from Replay import *
from PIL import Image, ImageTk

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
		print 'Trace',trace.tag,'is added'

	
class Controler(DisplayFrame):
	"""docstring for Controler"""
	def __init__(self,size,title='',Caller=None):
		super(Controler, self).__init__(size,title)
		# self.label = Label(self.top,text='This is Controler',font = 'Helvetica -12 bold')
		# self.label.pack(fill=Y, expand=0)
		self.f_text = Frame(self.top)
		self.f_text.pack(side=TOP,expand=1,fill=X)
		self.f_bar = Frame(self.top)
		self.f_bar.pack(side=TOP,expand=1,fill=X)
		self.f_bottom = Frame(self.top)
		self.f_bottom.pack(side=BOTTOM,expand=1,fill=X)


		self.label1 = Label(self.f_text,text='SftX',font = 'Helvetica -12 bold')
		self.label1.pack(side=LEFT)
		self.text1 = Text(self.f_text,height=1,width=8)
		self.text1.pack(side=LEFT)
		self.label2 = Label(self.f_text,text='SftY',font = 'Helvetica -12 bold')
		self.label2.pack(side=LEFT)
		self.text2 = Text(self.f_text,height=1,width=8)
		self.text2.pack(side=LEFT)
		self.label3 = Label(self.f_text,text='Scale',font = 'Helvetica -12 bold')
		self.label3.pack(side=LEFT)
		self.text3 = Text(self.f_text,height=1,width=8)
		self.text3.pack(side=LEFT)


		self.ProgBar = Scale(self.f_bar,from_=0,to=100,orient=HORIZONTAL,command=Caller.OnProgBarMove)
		self.ProgBar.pack(fill=X,side=TOP)

		self.CoordLbl = Label(self.f_bottom,text='xl=0, yl=0; xr=0, yr=0',font = 'Helvetica -12 bold')
		self.CoordLbl.pack(side=LEFT)
		self.Btn_quit = Button(self.f_bottom,text='QUIT',command=self.top.quit,activeforeground='white',
								activebackground='red')
		self.Btn_quit.pack(side=RIGHT)

		self.Btn_Confirm = Button(self.f_bottom,text='Confirm',command = Caller.OnConfirm)
		self.Btn_Confirm.pack(side=RIGHT)

		# if len(self.TraceList) > 0:
		# 	TraceLen = TraceList[0].endtime - TraceList[0].starttime
		# else:
		# 	TraceLen = 1
		# 	print 'Warning: No trace is Added'
				

		# self.TracePath1 = Text(self.top)
		# self.input1.pack()
		# self.TracePath2 = Text(se)


	def AddTrace(self,trace):
		super(Controler,self).AddTrace(trace)
		TraceLen = self.TraceList[0].endtime - self.TraceList[0].starttime
		self.ProgBar.config(to=TraceLen)
		

class ShowPath(DisplayFrame):
	"""docstring for ShowPath"""
	def __init__(self,size,title='',mappath='pikachou.jpg'):
		super(ShowPath, self).__init__(size,title)
		self.SftX = 0.0
		self.SftY = 0.0
		self.Scale = 1.0
		
		# self.map =PhotoImage(file='pikachou.gif')
		self.C = Canvas(self.top,
						width= 1280,
						height= 1024,
						bg='white')
		self.Loadmap(mappath)
		self.recW = 15
		self.recH = 15
		self.recDict = {}
		self.recStyle = {'L':['red','green'],'R':['blue','white']}
		self.C.pack(expand=1)


	#reload
	def AddTrace(self,trace):
		# self.TraceList.append(trace)
		super(ShowPath,self).AddTrace(trace)
		rec = self.C.create_rectangle(0, 0, self.recW, self.recH, 
						fill=self.recStyle[trace.tag][0], 
						outline=self.recStyle[trace.tag][1])
		self.recDict.update({trace:rec})


	def Loadmap(self,mappath):
		image = Image.open(mappath) 
		self.map = ImageTk.PhotoImage(image) 
		# print dir(self.C)
		self.C.create_image(1280/2,1024/2,image=self.map)

class GUITop(object):
	"""docstring for GUITop"""
	def __init__(self,LTrace,RTrace):
		super(GUITop, self).__init__()
		self.LTrace = LTrace
		self.RTrace = RTrace
		self.FitTwoTraces(self.LTrace,self.RTrace)
		# print str(self.LTrace), '\n\n'
		# print str(self.RTrace)
		# self.arg = arg
		self.Show = ShowPath('1600x1200','Location Trace','TongFangD19.jpg')
		self.Con = Controler('330x100','Control Panel',Caller=self)		
		
		self.Con.AddTrace(self.LTrace)
		self.Con.AddTrace(self.RTrace)
		self.Show.AddTrace(self.LTrace)
		self.Show.AddTrace(self.RTrace)
		# print len(self.Con.TraceList)
		
		self.Show.top.mainloop()
		self.Con.top.mainloop()


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
		endtime = min([TA.endtime,TB.endtime])
		# TODO: clip the trace
		SecListA = TA.trace.keys()
		SecListA.sort()
		SecListB = TB.trace.keys()
		SecListB.sort()
		for i_time in SecListA:
			if not i_time in xrange(starttime,endtime+1):
				TA.trace.pop(i_time)
		TA.RefreshTrace()
		for i_time in SecListB:
			if not i_time in xrange(starttime,endtime+1):
				TB.trace.pop(i_time)
		TB.RefreshTrace()

		pass

	def OnConfirm(self,ev=None):
		self.Show.SftX = float(self.Con.text1.get(1.0,END))
		self.Show.SftY = float(self.Con.text2.get(1.0,END))
		self.Show.Scale = float(self.Con.text3.get(1.0,END))

		pass

	def OnProgBarMove(self,ev=None):
		# print self.Con.ProgBar.get()
		W = self.Show.recW
		H = self.Show.recH
		for trace in self.Show.TraceList:
			time = trace.starttime + self.Con.ProgBar.get()
			PosX = trace.trace[time].getX()* self.Show.Scale + self.Show.SftX
			PosY = trace.trace[time].getY()* self.Show.Scale + self.Show.SftY 
			rec = self.Show.recDict[trace]
			self.Show.C.coords(rec,(PosX, PosY, W+PosX, H+PosY))
		self.Con.CoordLbl.config(text = 'xl=%.1f, yl=%.1f'%(PosX,PosY))
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
	# print str(RTrace)
	# print LTrace.trace[LTrace.starttime].getTimeStamp()
	G = GUITop(LTrace,RTrace)


	pass

if __name__ == "__main__":
	
	main()
	# temptest()
	



	


