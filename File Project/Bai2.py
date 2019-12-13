
from tkinter import *

class XuLy:
    def __init__(self):
        window = Tk()
        window.title("Ve Hinh")
        self.canvas = Canvas(window, width = 530, height = 300, bg = "whitesmoke")
        self.canvas.pack()
        frame = Frame(window)
        frame.pack()
        #Label
        labelframe1 = LabelFrame(window, text="Figure")
        labelframe1.place(x=410,y=0,height=150,width=120)
        labelframe2= LabelFrame(window, text="Color")
        labelframe2.place(x=410,y=150,height=150,width=120)
        #radio button
        self.figure = IntVar()
        #Set Checkbox = true Startup
        self.figure.set(1)
        Radiobutton(labelframe1, text = "Elip",variable = self.figure, value = "1", command = self.Change).place(x = 10, y = 10)  
        Radiobutton(labelframe1, text = "Chu Nhat",variable = self.figure, value = "2", command = self.Change).place(x = 10, y = 40)  
        Radiobutton(labelframe1, text = "Tam Giac",variable = self.figure, value = "3", command = self.Change).place(x = 10, y = 70)  
        #check button
        self.var1 = IntVar()
        self.var2 = IntVar()
        self.var3 = IntVar()
        #Set Checkbox = true Startup
        self.var1.set(1)
        Checkbutton(labelframe2, text = "Red", variable = self.var1, command = self.Change).place(x = 10, y = 10) 
        Checkbutton(labelframe2, text = "Green", variable = self.var2, command = self.Change).place(x = 10, y = 40)               
        Checkbutton(labelframe2, text = "Blue", variable = self.var3, command = self.Change).place(x = 10, y = 70) 
        
        window.mainloop()
    ## Value Get
    def Value(self):
        self.on = str(self.figure.get())
        self.red = str(self.var1.get())
        self.green = str(self.var2.get())
        self.blue = str(self.var3.get())
    ##Change
    def Change(self):
            self.clearCanvas()
            self.draw_Blackcolor()
    ##Delete Canvas Before Draw
    def clearCanvas(self):
        self.canvas.delete('elip','chunhat','tamgiac')
    ##Color RBG TransLates
    def colorRBG(self):
        def _from_rgb(rgb):
            return "#%02x%02x%02x" % rgb
        self.Value()
        if self.red == "1":
            self.x = 255
        else:
            self.x = 0
        if self.green == "1":
            self.y = 255
        else:
            self.y = 0
        if self.blue == "1":
            self.z = 255
        else:
            self.z = 0
        return _from_rgb((self.x, self.y, self.z))
    ##Color Change
    def draw_Blackcolor(self):     
        self.Value()
        abc = self.colorRBG()
        if self.on == "1":
            self.canvas.create_oval(20,300,280,30, fill = abc, tags="elip")
        elif self.on == "2":
            self.canvas.create_rectangle(20,200,280,30, fill = abc,tags="chunhat")
        elif self.on == "3":
            self.canvas.create_polygon(150,65,245,240,45,240,150,65, fill=abc, outline ="black",tags="tamgiac")  
XuLy()
