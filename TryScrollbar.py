from Tkinter import *
from PIL import Image, ImageTk

PNGPath = r'C:\Users\XiaoMing-OfficePC\Desktop\AEON Trace\ChaoYangDaYueCheng_Floor_AEON.png'


root = Toplevel()


image = Image.open(PNGPath) 
pngmap = ImageTk.PhotoImage(image) 



scrollbarY = Scrollbar(root)
scrollbarX = Scrollbar(root,orient = HORIZONTAL)

# mylist = Listbox(root, yscrollcommand = scrollbar.set )
# for line in range(30):
#    mylist.insert(END, "This is line number " + str(line))

# mylist.pack( side = LEFT, fill = BOTH )
# scrollbar.config( command = mylist.yview )

C = Canvas(root,
			width= 1500,
			height= 3000,
			scrollregion = (0,0,1500,2500),
			xscrollcommand = scrollbarX.set,
			yscrollcommand = scrollbarY.set,
			bg='white')
scrollbarX.config( command = C.xview )
scrollbarY.config( command = C.yview )
# C.grid(row=0, column=0)
scrollbarY.pack(side = RIGHT, fill=Y)
scrollbarX.pack(side = BOTTOM, fill=X)
C.pack(side = LEFT, fill = BOTH)
# scrollbar.grid(row=0, column=1, sticky='ns')


C.create_image(0,0,image=pngmap,anchor=NW,tags='map')

mainloop()
