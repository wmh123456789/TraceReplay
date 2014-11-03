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


	def ClearAllTrace(self):
		#ToDo: Renew all traces 
		pass
	
class Controler(DisplayFrame):
	"""docstring for Controler"""
	def __init__(self,size,title='',Caller=None):
		super(Controler, self).__init__(size,title)
		
		# Frames
		self.initFrame(Caller)
		# Canvas configure(Shift, Scale)
		self.initCanvas(Caller)
		# Trace option
		self.initTraceOpt(Caller)
		# Map related
		self.initMap(Caller)
		# Prograss Bar
		self.initPrograssBar(Caller)
		# Status show
		self.initStatus(Caller)
		# Buttons
		self.initButtons(Caller)

	def initFrame(self,Caller):
		# Create Frames
		self.f_CanOpt = Frame(self.top)
		self.f_TrcOpt = Frame(self.top)
		self.f_bar = Frame(self.top)
		self.f_bottom = Frame(self.top)
		self.f_map = Frame(self.top)
		# Pack Frames
		self.f_CanOpt.pack(side=TOP,expand=1,fill=X)
		self.f_TrcOpt.pack(side=TOP,expand=1,fill=X)
		self.f_map.pack(side=TOP,expand=1,fill=X)
		self.f_bar.pack(side=TOP,expand=1,fill=X)
		self.f_bottom.pack(side=BOTTOM,expand=1,fill=X)


	def initCanvas(self,Caller):
		self.label1 = Label(self.f_CanOpt,text='SftX',font = 'Helvetica -12 bold')
		self.label1.pack(side=LEFT)
		self.text1 = Text(self.f_CanOpt,height=1,width=9)
		self.text1.pack(side=LEFT)
		self.label2 = Label(self.f_CanOpt,text='SftY',font = 'Helvetica -12 bold')
		self.label2.pack(side=LEFT)
		self.text2 = Text(self.f_CanOpt,height=1,width=9)
		self.text2.pack(side=LEFT)
		self.label3 = Label(self.f_CanOpt,text='Scale',font = 'Helvetica -12 bold')
		self.label3.pack(side=LEFT)
		self.text3 = Text(self.f_CanOpt,height=1,width=9)
		self.text3.pack(side=LEFT)
		self.Btn_Confirm = Button(self.f_CanOpt,text='Confirm',command = Caller.OnConfirm)
		self.Btn_Confirm.pack(side=RIGHT)

	def initTraceOpt(self,Caller):
		self.lb_tracepath = Label(self.f_TrcOpt,text='TracePath',font = 'Helvetica -12 bold')
		self.lb_tracepath.pack(side=LEFT)
		self.tx_tracepath = Text(self.f_TrcOpt,height=1,width=22)
		self.tx_tracepath.pack(side=LEFT)
		self.lb_opt = Label(self.f_TrcOpt,text='TraceMode',font = 'Helvetica -12 bold')
		self.lb_opt.pack(side=LEFT)
		self.tx_opt = Text(self.f_TrcOpt,height=1,width=2)
		self.tx_opt.pack(side=LEFT)
		self.Btn_reload = Button(self.f_TrcOpt,text='Reload',command = Caller.OnReloadTrace)
		self.Btn_reload.pack(side=RIGHT)

	def initMap(self,Caller):
		self.lb_mappath = Label(self.f_map,text='MapPath',font = 'Helvetica -12 bold')
		self.lb_mappath.pack(side=LEFT)
		self.tx_mappath = Text(self.f_map,height=1,width=22)
		self.tx_mappath.pack(side=LEFT)
		self.lb_mappath = Label(self.f_map,text='Floor',font = 'Helvetica -12 bold')
		self.lb_mappath.pack(side=LEFT)
		self.Btn_loadmap = Button(self.f_map,text='Load',command = Caller.OnLoadMap)
		self.Btn_loadmap.pack(side=RIGHT)

	def initPrograssBar(self,Caller):
		self.ProgBar = Scale(self.f_bar,from_=0,to=100,orient=HORIZONTAL,command=Caller.OnProgBarMove)
		self.ProgBar.pack(fill=X,side=TOP)

	def initStatus(self,Caller):
		self.CoordLbl = Label(self.f_bottom,text='xl=0, yl=0; xr=0, yr=0',font = 'Helvetica -12 bold')
		self.CoordLbl.pack(side=LEFT)

	def initButtons(self,Caller):
		self.Btn_quit = Button(self.f_bottom,text='QUIT',command=self.top.quit,activeforeground='white',
								activebackground='red')
		self.Btn_quit.pack(side=RIGHT)


	def AddTrace(self,trace):
		super(Controler,self).AddTrace(trace)
		TraceLen = self.TraceList[0].endtime - self.TraceList[0].starttime
		self.ProgBar.config(to=TraceLen)
		

class ShowPath(DisplayFrame):
	"""docstring for ShowPath"""
	def __init__(self,size,title='',Caller=None):
		super(ShowPath, self).__init__(size,title)
		self.CurrFlr = Caller.CurrFlr
		self.MapParam = Caller.MapParam 
		self.SftX = self.MapParam[self.CurrFlr]['X']
		self.SftY = self.MapParam[self.CurrFlr]['H'] - self.MapParam[self.CurrFlr]['Y']
		self.Scale  = self.MapParam[self.CurrFlr]['K']
		self.width  = self.MapParam[self.CurrFlr]['W']
		self.height = self.MapParam[self.CurrFlr]['H']

		self.C = Canvas(self.top,
						width= self.width,
						height= self.height,
						bg='white')
		self.Loadmap(Caller.MapPath)
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
		self.C.create_image(self.width/2,self.height/2,image=self.map)

class GUITop(object):
	"""docstring for GUITop"""
	def __init__(self,LTrace,RTrace,MapParamPath = '',TracePath=''):
		super(GUITop, self).__init__()
		self.LTrace = LTrace
		self.RTrace = RTrace
		self.TracePath = TracePath
		self.MapParam = self.ParseMapParam(MapParamPath)
		self.FitTwoTraces(self.LTrace,self.RTrace)
		self.MapPath = 'TongFangD19_Floor_F19.png'
		self.CurrFlr = self.MapPath.split('.')[-2].split('_')[-1]

		self.Show = ShowPath(self.MapParam[self.CurrFlr]['sizeTxt'],'Location Trace',Caller=self)
		self.Con = Controler('450x180','Control Panel',Caller=self)		
		
		# Add traces
		self.Con.AddTrace(self.LTrace)
		self.Con.AddTrace(self.RTrace)
		self.Show.AddTrace(self.LTrace)
		self.Show.AddTrace(self.RTrace)
	
		# Data analysis
		self.TotalErr = 0.0
		self.TotalPts = 0
		self.AvgErr = 0.0


		# Start windows
		self.Show.top.mainloop()
		self.Con.top.mainloop()


	'''
	Parse the mpa params from .params file:
	Each line of .params file: BldName FlrName W H X Y K
	In the ShowPath class, coordinates of each locat point(lx,ly) is (px,py):
		px =  lx*K+X
		py = -ly*K+(H-Y)
	'''
	def ParseMapParam(self,ParamFile):
		lines = open(ParamFile).readlines()
		params = {}
		for line in lines:
			text = line.split('\t')
			param = {'BldName':text[0],
						'FlrName':text[1],
						'W':int(text[2]),
						'H':int(text[3]),
						'X':int(text[4]),
						'Y':int(text[5]),
						'K':float(text[6]),
						'sizeTxt':text[2]+'x'+text[3]}
			params.update({param['FlrName']:param})
		return params


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

	def FitTwoTraces(self,TA,TB):
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

	def OnReloadTrace(self,ev=None):
		xml = XMLFile(self.TracePath)
		self.LTrace = LocTrace([xml.timestamplist_L,xml.Xlist_L,xml.Ylist_L],tag='L')
		self.RTrace = LocTrace([xml.timestamplist_R,xml.Xlist_R,xml.Ylist_R],tag='R')
		self.LTrace.LinearInterpolation()
		self.RTrace.LinearInterpolation()
		self.FitTwoTraces(self.LTrace,self.RTrace)
		self.Con.ClearAllTrace()
		self.Show.ClearAllTrace()
		self.Con.AddTrace(self.LTrace)
		self.Con.AddTrace(self.RTrace)
		self.Show.AddTrace(self.LTrace)
		self.Show.AddTrace(self.RTrace)
		self.TotalErr = 0.0
		self.TotalPts = 0
		self.AvgErr = 0.0

		pass

	def OnLoadMap(self,ev=None):
		# Load map params
		
		# Load floor list
		
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
			PosX = lambda t:(trace.trace[t].getX()* self.Show.Scale + self.Show.SftX)  
			PosY = lambda t:(-1*trace.trace[t].getY()* self.Show.Scale + self.Show.SftY)  
			rec = self.Show.recDict[trace]
			self.Show.C.coords(rec,(PosX(time), PosY(time), W+PosX(time), H+PosY(time)))

			# Keep a trace on map 
			if '1' in self.Con.tx_opt.get(1.0,END):     # Points mode
				self.Show.C.create_rectangle(PosX(time), PosY(time), W+PosX(time), H+PosY(time), 
							fill=self.Show.recStyle[trace.tag][0], 
							outline=self.Show.recStyle[trace.tag][1])
			if '2' in self.Con.tx_opt.get(1.0,END):    # Lines mode
				if time > trace.starttime:
					#ToDo: Draw a line 
					self.Show.C.create_line(PosX(time-1),PosY(time-1),PosX(time),PosY(time),
							fill=self.Show.recStyle[trace.tag][0],
							width = 2.5)
					pass
			if '3' in  self.Con.tx_opt.get(1.0,END):    # Tag on trace
				#TODO: add a tag on the current point
				pass

		# Error Calculation
		ErrorDist = self.CalcDist(float(self.Show.TraceList[0].trace[time].x),
								float(self.Show.TraceList[0].trace[time].y),
								float(self.Show.TraceList[1].trace[time].x),
								float(self.Show.TraceList[1].trace[time].y))
		self.TotalErr += ErrorDist
		self.TotalPts += 1
		self.AvgErr = float(self.TotalErr/self.TotalPts)
		self.Con.CoordLbl.config(text = 'ErrorDst=%.2f; AvgErr=%.3f'%(ErrorDist,self.AvgErr))

		return self.Con.ProgBar.get()
		pass

	def CalcDist(self,x1,y1,x2,y2):
		 return ((x1-x2) **2 +(y1-y2)**2) **0.5

def main():
	
	# rootpath = '.\TFRecord\RawFiles\Test2'
	rootpath = r'E:\= Workspaces\Git\TraceReplay\LocateRecord\test.xml'
	# filename = '\Test2\Test2.xml'
	xml = XMLFile(rootpath)
	LTrace = LocTrace([xml.timestamplist_L,xml.Xlist_L,xml.Ylist_L],tag='L')
	RTrace = LocTrace([xml.timestamplist_R,xml.Xlist_R,xml.Ylist_R],tag='R')
	LTrace.LinearInterpolation()
	RTrace.LinearInterpolation()
	
	# Print the Raw Trace data
	# print '\n----===== Real  Path =====----\n'
	# print str(RTrace)
	# print '\n----===== Locate Path =====----\n'
	# print str(LTrace)
	# print LTrace.trace[LTrace.starttime].getTimeStamp()
	
	ParamFile = r'E:\MDBGenerate\= MDB_Modify_BJ\= ModifiedOK\TongFangD19\Binary\TongFangD19.binary.params'
	G = GUITop(LTrace,RTrace,ParamFile)
	

if __name__ == "__main__":
	
	main()
	# temptest()
	



	


