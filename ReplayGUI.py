from Tkinter import *
from Replay import *

class DisplayFrame(object):
	"""docstring for DisplayFrame"""
	def __init__(self,size,title=''):
		super(DisplayFrame, self).__init__()
		self.top = Tk()
		self.top.geometry(size)
		self.top.title(title)
		print 'DisplayFrame is loaded'



class Controler(DisplayFrame):
	"""docstring for Controler"""
	def __init__(self,size,title=''):
		super(Controler, self).__init__(size,title)
		# self.label = Label(self.top,text='This is Controler',font = 'Helvetica -12 bold')
		# self.label.pack(fill=Y, expand=0)
		self.Btn_quit = Button(self.top,text='QUIT',command=self.top.quit,activeforeground='white',
		activebackground='red')
		self.Btn_quit.pack(side=BOTTOM)

class ShowPath(DisplayFrame):
	"""docstring for ShowPath"""
	def __init__(self,size,title='',trace=None):
		super(ShowPath, self).__init__(size,title)
		# self.label = Label(self.top,text='This is ShowPath',font = 'Helvetica -12 bold')
		# self.label.pack(fill=Y, expand=1)
		self.C = Canvas(self.top,bg='white')
		self.coord = 10,50,240,210
		self.arc = self.C.create_arc(self.coord,start=0,extent=60,fill='green')
		self.rec = self.C.create_rectangle(50, 25, 55, 30, fill="red", outline='green')
		self.C.pack(expand=1)

		

class GUITop(object):
	"""docstring for GUITop"""
	def __init__(self,trace):
		super(GUITop, self).__init__()
		# self.arg = arg
		Con = Controler('800x600','Control Panel')		
		Show = ShowPath('400x300','Location Trace',trace)






		Con.top.mainloop()
		Show.top.mainloop()
		



def main():
	
	rootpath = 'E:\= Workspaces\Git\TraceReplay\LocateRecord'
	filename = '\\10100120_101001200004_20141017132945_1.xml'
	lp = LocPoint(['20141017132946','114.0','36.9'])
	xml = XMLFile(rootpath+filename)
	LTrace = LocTrace([xml.timestamplist_L,xml.Xlist_L,xml.Ylist_L])
	RTrace = LocTrace([xml.timestamplist_R,xml.Xlist_R,xml.Ylist_R])
	LTrace.LinearInterpolation()
	print str(LTrace)

	G = GUITop(LTrace)

	pass

if __name__ == "__main__":
	main()




	


