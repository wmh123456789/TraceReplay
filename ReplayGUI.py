from Tkinter import *
import tkFileDialog
from Replay import *
from PIL import Image, ImageTk

class DisplayFrame(object):
	"""docstring for DisplayFrame"""
	def __init__(self,size,title=''):
		super(DisplayFrame, self).__init__()
		self.top = Toplevel()
		self.top.geometry(size)
		self.top.title(title)
		self.TraceList = []
		print 'DisplayFrame is loaded'

	def AddTrace(self,trace):
		self.TraceList.append(trace)
		print 'Trace',trace.tag,'is added'


	def ClearAllTrace(self):
		#ToDo: Renew all traces 
		self.TraceList = []
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


	def initMenu(self,Caller):
		pass

	def initFrame(self,Caller):
		# Create Frames
		self.f_CanOpt = Frame(self.top)
		self.f_TrcOpt = Frame(self.top)
		self.f_bar = Frame(self.top)
		self.f_bottom = Frame(self.top)
		self.f_param = Frame(self.top)
		self.f_map = Frame(self.top)
		# Pack Frames
		self.f_CanOpt.pack(side=TOP,expand=1,fill=X)
		self.f_param.pack(side=TOP,expand=1,fill=X)
		self.f_map.pack(side=TOP,expand=1,fill=X)
		self.f_TrcOpt.pack(side=TOP,expand=1,fill=X)
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
		self.btn_Confirm = Button(self.f_CanOpt,text='Confirm',command = Caller.OnConfirm)
		self.btn_Confirm.pack(side=LEFT)
		self.var_Interpolate = IntVar()
		self.cb_Interpolate = Checkbutton(self.f_CanOpt,text='Interpolate',
										variable=self.var_Interpolate)
		self.cb_Interpolate.pack(side=RIGHT)
		self.var_FromAPP = IntVar()
		self.cb_FromAPP = Checkbutton(self.f_CanOpt,text='FromAPP',
										variable=self.var_FromAPP)
		self.cb_FromAPP.pack(side=RIGHT)

	def initTraceOpt(self,Caller):
		self.lb_tracepath = Label(self.f_TrcOpt,text='TracePath',font = 'Helvetica -12 bold')
		self.lb_tracepath.pack(side=LEFT)
		self.tx_tracepath = Text(self.f_TrcOpt,height=1,width=32)
		self.tx_tracepath.pack(side=LEFT)
		self.btn_loadtrace = Button(self.f_TrcOpt,text='Dir',command = Caller.OnLoadTrace)
		self.btn_loadtrace.pack(side=LEFT)
		self.btn_loadtraceF = Button(self.f_TrcOpt,text='File',command = Caller.OnLoadTraceFile)
		self.btn_loadtraceF.pack(side=LEFT)
		self.lb_opt = Label(self.f_TrcOpt,text='    DrawMode',font = 'Helvetica -12 bold')
		self.lb_opt.pack(side=LEFT)
		# self.tx_opt = Text(self.f_TrcOpt,height=1,width=3)
		# self.tx_opt.pack(side=LEFT)
		self.var_modePtTrace = IntVar()
		self.cb_modePtTrace = Checkbutton(self.f_TrcOpt,text='Trace',
										variable=self.var_modePtTrace,
										indicatoron = 0)
		self.cb_modePtTrace.pack(side=LEFT)
		self.var_modeLine = IntVar()
		self.cb_modeLine = Checkbutton(self.f_TrcOpt,text='Line',
										variable=self.var_modeLine,
										indicatoron = 0)
		self.cb_modeLine.pack(side=LEFT)
		self.btn_clear = Button(self.f_TrcOpt,text='Clear',command = Caller.OnClearTrace)
		self.btn_clear.pack(side=RIGHT)

	def initMap(self,Caller):
		self.lb_parampath = Label(self.f_param,text='Param',font = 'Helvetica -12 bold')
		self.lb_parampath.pack(side=LEFT)
		self.tx_parampath = Text(self.f_param,height=1)
		self.tx_parampath.pack(side=LEFT,fill=X)
		self.btn_openmpr = Button(self.f_param,text='Open',command = Caller.OnOpenMapParamPath)
		self.btn_openmpr.pack(side=RIGHT)

		self.lb_mappath = Label(self.f_map,text='FloorMap',font = 'Helvetica -12 bold')
		self.lb_mappath.pack(side=LEFT)
		self.tx_mappath = Text(self.f_map,height=1)
		self.tx_mappath.pack(side=LEFT,fill=X)
		self.btn_loadmap = Button(self.f_map,text='Load',command = Caller.OnLoadMap)
		self.btn_loadmap.pack(side=RIGHT)

	def initPrograssBar(self,Caller):
		self.ProgBar = Scale(self.f_bar,from_=0,to=100,orient=HORIZONTAL,command=Caller.OnProgBarMove)
		self.ProgBar.pack(fill=X,side=TOP)
		self.ProgBarScale = []    # Scale to real time point
		self.btn_showall = Button(self.f_bar,text='ShowAll',command = Caller.OnShowAll)
		self.btn_showall.pack(side=RIGHT)


	def initStatus(self,Caller):
		self.CoordLbl = Label(self.f_bottom,text='xl=0, yl=0; xr=0, yr=0;',font = 'Helvetica -12 bold')
		self.CoordLbl.pack(side=LEFT)
		self.TimeLbl = Label(self.f_bottom,text='Start= ; End= ',font = 'Helvetica -12 bold')
		self.TimeLbl.pack(side=LEFT)

	def initButtons(self,Caller):
		self.btn_quit = Button(self.f_bottom,text='QUIT',command=self.top.quit,activeforeground='white',
								activebackground='red')
		self.btn_quit.pack(side=RIGHT)


	def AddTrace(self,trace):
		if not trace==None:
			super(Controler,self).AddTrace(trace)
			# TraceLen = self.TraceList[0].endtime - self.TraceList[0].starttime
			TraceLen = len(self.TraceList[0].trace.keys())
			self.ProgBar.config(to=TraceLen-1)
			self.ProgBarScale = self.TraceList[0].trace.keys()
			self.ProgBarScale.sort()
			# print self.ProgBarScale
		pass
		

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

		self.scrollbarY = Scrollbar(self.top, orient=VERTICAL)
		self.scrollbarX = Scrollbar(self.top, orient = HORIZONTAL)

		self.C = Canvas(self.top,
						width= min(1000,self.width),
						height= min(800,self.height),
						xscrollcommand = self.scrollbarX.set,
						yscrollcommand = self.scrollbarY.set,
						scrollregion = (0,0,self.width,self.height),
						bg='white')
		# self.Loadmap(Caller.MapPath)
		self.scrollbarY.config( command = self.C.yview )
		self.scrollbarX.config( command = self.C.xview )
		
		self.scrollbarY.pack( side = RIGHT, fill=Y)
		self.scrollbarX.pack( side = BOTTOM, fill=X )
		
		self.C.pack(expand=1)
		
		self.recW = 7
		self.recH = 7
		self.recDict = {}
		self.recStyle = {'L':['red','green'],'R':['blue','white']}




	#reload
	def AddTrace(self,trace):
		# self.TraceList.append(trace)
		super(ShowPath,self).AddTrace(trace)
		rec = self.C.create_rectangle(0, 0, self.recW, self.recH, 
						fill=self.recStyle[trace.tag][0], 
						outline=self.recStyle[trace.tag][1],
						tags=(trace.tag,'rec'))
		self.recDict.update({trace:rec})


	def Loadmap(self,mappath):
		image = Image.open(mappath) 
		self.map = ImageTk.PhotoImage(image) 
		print self.map
		# self.C.create_image(self.width/2,self.height/2,image=self.map,tags='map')
		self.C.create_image(0,0,anchor=NW,image=self.map,tags='map')

class GUITop(object):
	"""docstring for GUITop"""
	def __init__(self,LTrace=None,RTrace=None,MapParamPath = '',TracePath=''):
		super(GUITop, self).__init__()
		self.LTrace = LTrace
		self.RTrace = RTrace
		self.TracePath = TracePath
		self.TraceMode = '0'  # 0=Default, 1=PointTrace, 2=Line, 3=TagOn
		self.recH = 10
		self.recW = 10
		self.MapParamPath = MapParamPath
		self.MapParam = self.ParseMapParam(self.MapParamPath)
		# if not (LTrace == None or RTrace == None): 
		# 	self.FitTwoTraces(self.LTrace,self.RTrace)
		self.MapPath = ''
		self.CurrFlr = ''
		# self.MapPath = 'TongFangD19_Floor_F19.png'
		# self.CurrFlr = self.MapPath.split('.')[-2].split('_')[-1]

		self.Con = Controler('750x280+0+0','Control Panel',Caller=self)
		# self.Show = ShowPath(self.MapParam[self.CurrFlr]['sizeTxt'],'Location Trace',Caller=self)
		# self.Show.Loadmap(self.MapPath)
		
		# Add traces
		self.Con.AddTrace(self.LTrace)
		self.Con.AddTrace(self.RTrace)
		# self.Show.AddTrace(self.LTrace)
		# self.Show.AddTrace(self.RTrace)
	
		# Data analysis
		self.TotalErr = 0.0
		self.TotalPts = 0
		self.AvgErr = 0.0

		# Start windows
		# self.Show.top.mainloop()
		self.Con.top.mainloop()

	'''
	Parse the mpa params from .params file:
	Each line of .params file: BldName FlrName W H X Y K
	In the ShowPath class, coordinates of each locat point(lx,ly) is (px,py):
		px =  lx*K+X
		py = -ly*K+(H-Y)
	'''
	def ParseMapParam(self,ParamFile):
		params = {}
		if not ParamFile == '':
			lines = open(ParamFile).readlines()
			for line in lines:
				text = line.split('\t')
				param = {'BldName':text[0],
							'FlrName':text[1],
							'W':int(text[2]),
							'H':int(text[3]),
							'X':int(text[4]),
							'Y':int(text[5]),
							'K':float(text[6]),
							'sizeTxt':text[2]+'x'+text[3]
							# 'sizeTxt':str(text[2]*2)+'x'+str(text[3]*2)
							}
				params.update({param['FlrName']:param})
				print param['FlrName']
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
		print 'FitTwoTraces'
		if not (TA == None or TA == None):
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
		
		if self.Con.var_Interpolate.get() == 1 :
			self.LTrace.LinearInterpolation()
			self.RTrace.LinearInterpolation()
			self.FitTwoTraces(self.LTrace,self.RTrace)
		
		self.Con.ClearAllTrace()
		self.Show.ClearAllTrace()
		self.Show.C.delete('rec')
		self.Con.AddTrace(self.LTrace)
		self.Con.AddTrace(self.RTrace)
		self.Show.AddTrace(self.LTrace)
		self.Show.AddTrace(self.RTrace)
		self.TotalErr = 0.0
		self.TotalPts = 0
		self.AvgErr = 0.0

		pass

	def LoadPathLog(self,logpath):
		if os.path.isfile(logpath):
			fp = open(logpath)
			log = fp.read()
			fp.close()
			if os.path.isfile(log):
				return os.path.split(log)[0]
			else:
				return log
		else:
			print 'Error:Cannot find the log file:',logpath
			return 'C:/'

	def OnClearTrace(self,ev=None):
		self.Show.C.delete('trace')
		pass
	
	def SavePathLog(self,log,logpath):
		fp=open(logpath,'w')
		fp.write(log)
		fp.close()

	def OnLoadTrace(self,ev=None):
		initdir = self.LoadPathLog('TracePath.log')
		path = tkFileDialog.askdirectory(initialdir = initdir)
		if path != '':
			self.TracePath = path
			self.Con.tx_tracepath.delete(1.0, END)
			self.Con.tx_tracepath.insert(1.0, self.TracePath.split('/')[-1])
			self.SavePathLog(self.TracePath,'TracePath.log')
			self.OnReloadTrace()

	def OnLoadTraceFile(self,ev=None):
		initdir = self.LoadPathLog('TracePath.log')
		path = tkFileDialog.askopenfilename(initialdir = initdir)
		if path != '':
			self.TracePath = path
			self.Con.tx_tracepath.delete(1.0, END)
			self.Con.tx_tracepath.insert(1.0, self.TracePath.split('/')[-1])
			self.SavePathLog(self.TracePath,'TracePath.log')
			self.OnReloadTrace()

	def OnOpenMapParamPath(self,ev=None):
		initdir = self.LoadPathLog('MapParamPath.log')
		path = tkFileDialog.askopenfilename(initialdir = initdir)
		if path != '':
			self.MapParamPath = path
			self.Con.tx_parampath.delete(1.0, END)
			self.Con.tx_parampath.insert(1.0, self.MapParamPath.split('/')[-1])
			self.SavePathLog(self.MapParamPath,'MapParamPath.log')
			self.MapParam = self.ParseMapParam(self.MapParamPath)

	def OnLoadMap(self,ev=None):
		# Load map
		initdir = self.LoadPathLog('MapPath.log')
		path = tkFileDialog.askopenfilename(initialdir = initdir)
		if path != '':
			self.MapPath = path
			self.Con.tx_mappath.delete(1.0, END)
			self.Con.tx_mappath.insert(1.0, self.MapPath.split('/')[-1])
			self.SavePathLog(self.MapPath,'MapPath.log')
			self.CurrFlr = self.MapPath.split('.')[-2].split('_')[-1]
			# self.CurrFlr = self.MapPath.split('.')[1][5:]
			print self.MapPath

			self.Show = ShowPath('1000x800+800+100','Location Trace',Caller=self)
			# self.Show = ShowPath(self.MapParam[self.CurrFlr]['sizeTxt']+'+800+100','Location Trace',Caller=self)
			# self.Show = ShowPath('1920x1080',Caller=self)
			self.Show.AddTrace(self.LTrace)
			self.Show.AddTrace(self.RTrace)
			self.Show.Loadmap(self.MapPath)
			self.Show.C.pack(fill=BOTH)
			self.Show.top.mainloop()
		pass

	def OnConfirm(self,ev=None):
		self.Show.SftX = float(self.Con.text1.get(1.0,END))
		self.Show.SftY = float(self.Con.text2.get(1.0,END))
		self.Show.Scale = float(self.Con.text3.get(1.0,END))
		pass

	def DrawTrace(self,trace,time):
		W = self.recW
		H = self.recH
		
		#for debug
		# print trace.trace.keys() 
		# print time,len(trace.trace.keys())

		# The Result From Trace Record APP  FromAPP
		if self.Con.var_FromAPP.get() == 1:
			PosX = lambda t:(trace.trace[t].getX()* self.Show.Scale + self.Show.SftX)  
			PosY = lambda t:(-1*trace.trace[t].getY()* self.Show.Scale + self.Show.SftY) 
		
		# The result from location server
		else:
			if trace.tag == 'L':
				PosX = lambda t:(trace.trace[t].getX()* self.Show.Scale)  
				PosY = lambda t:(trace.trace[t].getY()* self.Show.Scale)
			else:
				PosX = lambda t:0
				PosY = lambda t:0
		
		rec = self.Show.recDict[trace]
		self.Show.C.coords(rec,(PosX(time), PosY(time), W+PosX(time), H+PosY(time)))

		# for debug
		# print "X:"+str(PosX(time))+"; Y:"+str(PosY(time))
		

		# Keep a trace on map 
		# if '1' in self.TraceMode:     # Points-Trace mode
		if self.Con.var_modePtTrace.get() == 1:
			self.Show.C.create_rectangle(PosX(time), PosY(time), W+PosX(time), H+PosY(time), 
						fill=self.Show.recStyle[trace.tag][0], 
						outline=self.Show.recStyle[trace.tag][1],
						tags='trace')
		# if '2' in self.TraceMode:    # Lines mode
		if self.Con.var_modeLine.get() == 1:
			if time > trace.starttime:
				#ToDo: Draw a line 
				time0 = self.Con.ProgBarScale[self.Con.ProgBar.get()-1]
				self.Show.C.create_line(PosX(time0),PosY(time0),PosX(time),PosY(time),
						fill=self.Show.recStyle[trace.tag][0],
						width = 1.5,tags='trace')
				pass
		if '3' in  self.TraceMode:    # Tag on trace
			#TODO: add a tag on the current point
			pass

	def OnProgBarMove(self,ev=None):
		# print self.Con.ProgBar.get()
		# W = self.recW
		# H = self.recH

		for trace in self.Show.TraceList:
			# time = trace.starttime + self.Con.ProgBar.get()    # Fit the real time list

			time = self.Con.ProgBarScale[self.Con.ProgBar.get()]
			# print 'Find the Scale:',self.Con.ProgBar.get(),time
			self.DrawTrace(trace,time)
			

		# Error Calculation in APP record
		if self.Con.var_FromAPP.get() == 1:
			ErrorDist = self.CalcDist(float(self.Show.TraceList[0].trace[time].x),
									float(self.Show.TraceList[0].trace[time].y),
									float(self.Show.TraceList[1].trace[time].x),
									float(self.Show.TraceList[1].trace[time].y))
		else:
			ErrorDist = 0.0

		self.TotalErr += ErrorDist
		self.TotalPts += 1
		self.AvgErr = float(self.TotalErr/self.TotalPts)
		self.Con.CoordLbl.config(text = 'ErrorDst=%.2f; AvgErr=%.3f'%(ErrorDist,self.AvgErr))

		return self.Con.ProgBar.get()
		pass


	def OnShowAll(self,ev=None):
		for trace in self.Show.TraceList:
			print 'From:',self.Sec2Time(trace.starttime),' To:',self.Sec2Time(trace.endtime)
			print 'Total Points:',len(trace.trace)
			if trace.tag == 'L':     # For the locating trace
				self.CalcRegion(trace)

			for time in trace.trace.keys():
				self.DrawTrace(trace,time)
				pass
		pass

	def RegionCount(self,alist,rules):
		# rules: {keyA:ruleA,keyB:ruleB,...}
		count = dict(zip(rules.keys(),[0 for i in xrange(0,len(rules))]))
		for e in alist:
			for key in rules.keys():
				if rules[key](e) == True:
					count[key] += 1
					#debug
					if e >158:
						print e 

					pass
			pass
		return count
		pass

	# For AEON case, analyse the region distribution
	def CalcRegion(self,trace):
		if self.Con.var_FromAPP.get() == 1:
			bottom = lambda t: t<90
			lower = lambda t: t>=90 and t<130
			upper = lambda t: t>=130 and t<158
			top = lambda t: t>=158
		else:
			bottom = lambda t: t>135
			lower = lambda t: t>=95 and t<135
			upper = lambda t: t>=66 and t<95
			top = lambda t: t<66

		# rules = {'Top':top,'Upper':upper,'Lower':lower, 'Bottom':bottom}	
		rules = {'I':top,'II':upper,'III':lower, 'IV':bottom}		
		TraceY = [trace.trace[t].getY() for t in trace.trace.keys()]
		count = self.RegionCount(TraceY,rules)
		print count

	# Retrun DDHHMMSS
	def Sec2Time(self,sec):
		day = int(sec)/86400
		sec -= day*86400
		hour = int(sec)/3600
		sec -= hour*3600
		minute = int(sec)/60
		sec -= minute*60
		# print day,hour,minute,sec
		# return str(day)+str(hour)+str(minute)+str(sec)
		return "%2s%2s%2s%2s"%(day,hour,minute,sec)

	def CalcDist(self,x1,y1,x2,y2):
		 return ((x1-x2) **2 +(y1-y2)**2) **0.5

def main():
	
	# rootpath = '.\TFRecord\RawFiles\Test2'
	rootpath = r'.\LocateRecord\test.xml'
	MallName = 'TongFangD19'
	ParamFile = r'E:\MDBGenerate\= MDB_Modify_BJ\= ModifiedOK\\'+MallName+r'\Binary\\'+MallName+r'.binary.params'

	xml = XMLFile(rootpath)
	LTrace = LocTrace([xml.timestamplist_L,xml.Xlist_L,xml.Ylist_L],tag='L')
	RTrace = LocTrace([xml.timestamplist_R,xml.Xlist_R,xml.Ylist_R],tag='R')
	# Interplate polate

	# LTrace.LinearInterpolation()
	# RTrace.LinearInterpolation()
	
	# Print the Raw Trace data
	# print '\n----===== Real  Path =====----\n'
	# print str(RTrace)
	# print '\n----===== Locate Path =====----\n'
	# print str(LTrace)
	# print LTrace.trace[LTrace.starttime].getTimeStamp()
	print LTrace
	print RTrace
	
	G = GUITop(LTrace,RTrace)
	# G = GUITop()
	

if __name__ == "__main__":
	
	main()
	# temptest()
	



	


