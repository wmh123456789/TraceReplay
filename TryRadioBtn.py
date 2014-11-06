# -*- coding:utf-8 -*-
'''1.创建一个简单的Radiobutton'''
from Tkinter import *
root = Tk()
Radiobutton(root,indicatoron = 0,text = 'python').pack()
Radiobutton(root,indicatoron = 0,text = 'tkinter').pack()
Radiobutton(root,indicatoron = 0,text = 'widget').pack()
root.mainloop()
#不指定绑定变量，每个Radiobutton自成一组

# '''2.创建一个Radiobutton组，使用绑定变量来设置选中哦的按钮'''
# from Tkinter import *
# root = Tk()
# #创建一个Radiobutton组，创建三个Radiobutton，并绑定到整型变量v
# #选中value=1的按钮
# v = IntVar()
# v.set(1)
# for i in range(3):
#     Radiobutton(root,variable = v,text = 'python'+str(i),value = i).pack()

# root.mainloop()

# '''3.创建两个不同的组'''
# from Tkinter import *
# root = Tk()
# vLang = IntVar()
# vOS = IntVar()
# vLang.set(1)
# vOS.set(2)

# for v in [vLang,vOS]:    #创建两个组
#     for i in range(3):    #每个组含有3个按钮
#         Radiobutton(root,
#                     variable = v,
#                     value = i,
#                     text = 'python' + str(i)
#                     ).pack()
# root.mainloop()
# #不同的组，各个按钮互不影响。

# '''4.如果同一个组中的按钮使用相同的alue，则这两个按钮的工作方式完全相同'''
# # -*- coding: cp936 -*-
# from Tkinter import *
# root = Tk()
# v = IntVar()
# v.set(1)
# for i in range(3):
#     Radiobutton(root,
#                 variable = v,
#                 value = 1,
#                 text = 'python' + str(i)
#                 ).pack()
# for i in range(3):
#     Radiobutton(root,
#                     variable = v,
#                     value = i,
#                     text = 'python' + str(2 + i)
#                     ).pack()
# root.mainloop()
#上述的例子中共有4个alue为1的值，当选中其中的一个时，其他三个也会被选中；选中除了这四个只外的按钮时，四个按钮全部取消

# '''5.与Checkbutton类似，每个Radiobutton可以有自己的处理函数，每当点击按钮时，系统会调用相应的处理函数'''
# # -*- coding: cp936 -*-
# from Tkinter import *
# root = Tk()
# v = IntVar()
# v.set(0)
# def r1():
#     print 'call r1'
# def r2():
#     print 'call r2'
# def r3():
#     print 'call r3'
# def r4():
#     print 'call r4'
# i = 0
# #创建8个按钮，其中两个两个的value值相同
# for r in [r1,r2,r3,r4]:
#     Radiobutton(root,
#                     variable = v,
#                     text = 'radio button',
#                     value = i,
#                     command = r
#                     ).pack()
#     Radiobutton(root,
#                     variable = v,
#                     text = 'radio button',
#                     value = i,
#                     command = r
#                     ).pack()
#     i += 1
    
# root.mainloop()
# 注意虽然同时可以选中两个按钮，但每次点击按钮，执行的代码只有一次

# '''6.Radiobutton另一个比较实用的属性是indicatoron,缺省情况下为1，如果将这个属性改为0，则其外观是Sunken'''
# from Tkinter import *
# root = Tk()
# v = IntVar()
# v.set(1)
# for i in range(3):
#     Radiobutton(root,
#                     variable = v,
#                     indicatoron = 0,
#                     text = 'python & tkinter',
#                     value = i
#                     ).pack()
# root.mainloop()
# #Radiobutton表示按钮的弹起或按下两种状态