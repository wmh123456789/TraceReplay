# -*- coding:utf-8 -*-
# import time 
# import Tkinter 
# from PIL import Image, ImageTk

# print time.time()
# print time.localtime(1414051329393/100.0)


# D = {1:'a',2:'b',3:'c'}
# D.pop(2)

# A = lambda x,y:x+y
# print A(1,2)


# image = Image.open("pikachou.jpg")
# print image
# photo = ImageTk.PhotoImage(file="pikachou.jpg")



# root = Tkinter.Tk()
# root2 = Tkinter.Tk()
# image = Image.open("pikachou.jpg")
# im = ImageTk.PhotoImage(image)
# canvas = Tkinter.Canvas(root,
#     # width = 500,      # 指定Canvas组件的宽度
#     # height = 600,      # 指定Canvas组件的高度
#     bg = 'white')      # 指定Canvas组件的背景色
# #im = Tkinter.PhotoImage(file='img.gif')     # 使用PhotoImage打开图片


# canvas.create_image(150,150,image = im)      # 使用create_image将图片添加到Canvas组件中
# canvas.create_text(302,77,       # 使用create_text方法在坐标（302，77）处绘制文字
#    text = 'Use Canvas'      # 所绘制文字的内容
#    ,fill = 'gray')       # 所绘制文字的颜色为灰色
# canvas.create_text(300,75,
#    text = 'Use Canvas',
#    fill = 'blue')
# canvas.pack()         # 将Canvas添加到主窗口
# root.mainloop()
# root2.mainloop()


# from Tkinter import Tk, Frame, Text, BOTH, X, Y, RIGHT, LEFT, Listbox, N,E,W,S
# from Tkinter.Ttk import Notebook, Button

# root = Tk()
# root.geometry('{}x{}+{}+{}'.format(300, 200, 100, 50))
# root.title('test the ttk.Notebook')

# nb = Notebook(root)
# nb.pack(fill='both', expand='yes')

# # create a child frame for each page
# f1 = Frame(bg = 'red')
# f2 = Frame(bg='blue')
# f3 = Frame(bg='green')
# f1.pack(fill = BOTH, expand = 1)
# claimtext = Text(f1)
# claimtext.insert(1.0, 'Please insert text here...')
# claimtext.grid(sticky = E+W+S+N)
# listbox = Listbox(f1)
# listbox.grid(row = 0, column = 1, sticky = E+W+S+N)

# nb.add(f1, text = 'page1')
# nb.add(f2, text = 'page2')
# nb.add(f3, text = 'page3')

# # put a button widget on child frame f1 on page1
# #btn1 = Button(f1, text='button1')
# #btn1.pack(side='left', anchor='nw', padx=3, pady=5)

# root.mainloop()

from Tkinter import *
root = Tk()
def hello():
    print 'hello menu'
menubar = Menu(root)

filemenu = Menu(menubar,tearoff = 0)
for item in ['Python','PHP','CPP','C','Java','JavaScript','VBScript']:
    filemenu.add_command(label = item,command = hello)
#将menubar的menu属性指定为filemenu，即filemenu为menubar的下拉菜单
menubar.add_cascade(label = 'Language',menu = filemenu)
root['menu'] = menubar
root.mainloop()