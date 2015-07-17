# import Tkinter as Tk
from Tkinter import *
class TryClass(object):
	"""docstring for TryClass"""
	
	def __init__(self):
		super(TryClass, self).__init__()
		self.arc = 0
		top = Tk()
		top2 = Tk()
		# for top
		top.geometry('800x600')
		self.label = Label(top,text='hello ming',font = 'Helvetica -12 bold')
		self.label.pack(fill=Y, expand=1)
		self.scale = Scale(top,from_=0,to=18000,orient=HORIZONTAL,command=self.resize)
		self.scale.set(12) 
		self.scale.pack(fill=X,expand=1)
		quit = Button(top,text='QUIT',command=top.quit,activeforeground='white',
		activebackground='red')
		quit.pack()

		# for top2
		top2.geometry('1000x1000')
		label2 = Label(top2,text='Window 2!',font = 'Helvetica -20 bold')
		label2.pack()

		self.C = Canvas(top2,bg='white',height=1000,width=1200)
		# self.C = Canvas(top2,bg='white',height=250,width=300)
		self.coord = 10,50,240,210
		self.arc = self.C.create_arc(self.coord,start=0,extent=60,fill='green')

		self.rec = self.C.create_rectangle(50, 25, 55, 30, fill="red", outline='green')
		
		# for f in dir(self.C): 
		# 	print f 
		self.C.pack()

		top.mainloop()
		top2.mainloop()


	def resize(self,ev=None):
		self.label.config(font ='Helvetica -%d bold' % int(self.scale.get()/100))
		extent = self.scale.get()*2/100
		# self.C.delete(self.arc)
		# self.arc = self.C.create_arc(self.coord,start=0,extent=extent,fill='green')
		self.C.itemconfig(self.arc,extent=extent)
		self.C.coords(self.rec,(50+extent, 25, 55+extent, 30))

print dir(Canvas)
mytry = TryClass()


