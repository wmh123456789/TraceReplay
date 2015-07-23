# -*- coding:utf-8 -*-
# from Tkinter import *
# root = Tk()
# def hello():
# 	print 'hello menu'
# menubar = Menu(root)

# filemenu = Menu(menubar,tearoff = 0)
# for item in ['Python','PHP','CPP','C','Java','JavaScript','VBScript']:
# 	filemenu.add_command(label = item,command = hello)
# #将menubar的menu属性指定为filemenu，即filemenu为menubar的下拉菜单
# menubar.add_cascade(label = 'Language',menu = filemenu)
# root['menu'] = menubar
# root.mainloop()


# from Tkinter import *
# from FileDialog import *
# class App:
# 	def __init__(self,master):
# 		frame=Frame(master)
# 		frame.pack()
		
# 		self.button1=Button(frame,text="open",fg="red",command=self.inputnumber).grid(row=0,column=0)

# 	def inputnumber(self):
# 		fd = LoadFileDialog(root) 
# 		filename = fd.go() 
# 		print filename
        
# root=Tk()
# app=App(root)
# root.mainloop()

# import tkFileDialog
# import os
 
# filename = tkFileDialog.askopenfilename(initialdir = 'E:/Python')
# if filename == '':
# 	print 'Canceled'
# else:
# 	print filename

# path = 'D:\\Path0.txt '
# def LoadPathLog(logpath):
# 	if os.path.isfile(logpath):
# 		return open(logpath).read().strip()
# 	else:
# 		print 'Error:Cannot find the log file:',logpath

# print LoadPathLog(path)


a = 1
b = 2

c = max(a,b)
print c 