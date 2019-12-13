import tkinter as tk
from time import strftime
root = tk.Tk()
root.wm_title("Clock Time")
root.geometry("1200x300+200+150")
root.resizable(width= False, height= False)
screen = tk.Canvas(root)
screen.config(width = 1200, height = 300)
screen.grid()
##setting
offsets =(
    (7,  6,  11,  2,  31,  2,  35,  6,  31, 10,  11, 10),
    (6,  7,  10, 11,  10, 31,   6, 35,   2, 31,   2, 11),
    (36,  7,  40, 11,  40, 31,  36, 35,  32, 31,  32, 11),
    (7, 36,  11, 32,  31, 32,  35, 36,  31, 40,  11, 40 ),
    (6, 37,  10, 41,  10, 61,   6, 65,   2, 61,   2, 41),
    (36, 37,  40, 41,  40, 61,  36, 65,  32, 61,  32, 41),
    (7, 66,  11, 62,  31, 62,  35, 66,  31, 70,  11, 70)
    )
# Segments used for each digit; 0, 1 = off, on.
digits = (
    (1, 1, 1, 0, 1, 1, 1),  # 0
    (0, 0, 1, 0, 0, 1, 0),  # 1
    (1, 0, 1, 1, 1, 0, 1),  # 2
    (1, 0, 1, 1, 0, 1, 1),  # 3
    (0, 1, 1, 1, 0, 1, 0),  # 4
    (1, 1, 0, 1, 0, 1, 1),  # 5
    (1, 1, 0, 1, 1, 1, 1),  # 6
    (1, 0, 1, 0, 0, 1, 0),  # 7
    (1, 1, 1, 1, 1, 1, 1),  # 8
    (1, 1, 1, 1, 0, 1, 1),  # 9
)
#Position X, Y
ptColon1 = (462,85, 477, 100, 462, 115, 447, 100)
ptColon2 = (462,175,477,190,462,205,447,190)
ptColon3 = (812,85,827,100,812,115,797,100)
ptColon4 = (812,175,827,190,812,205,797,190)
class Digit:
    def __init__(self, canvas, x=10, y=40, length=3):
        self.canvas = canvas
        l = length
        self.segs = []
        for x0, y0, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5 in offsets:
            self.segs.append(canvas.create_polygon(x + x0*l, y + y0*l, x + x1*l, y + y1*l,x + x2*l, y + y2*l, x + x3*l, y + y3*l, x + x4*l, y + y4*l, x + x5*l, y + y5*l, state='hidden', fill ="red"))
            screen.create_polygon(ptColon1, fill = "red")
            screen.create_polygon(ptColon2, fill = "red")
            screen.create_polygon(ptColon3, fill = "red")
            screen.create_polygon(ptColon4, fill = "red")
    def show(self, num):
        for iid, on in zip(self.segs, digits[num]):
            self.canvas.itemconfigure(iid, state = 'normal' if on else 'hidden')

digh1 = Digit(screen, 150, 35) ##
digh2 = Digit(screen, 300, 35) ##
digm1 = Digit(screen, 500, 35) ##
digm2 = Digit(screen, 650, 35) ##
digs1 = Digit(screen, 850, 35) ##
digs2 = Digit(screen, 1000, 35) ##
def update():
    global s
    X = int(strftime("%I%M%S"))
    s2 = X%10
    s1 = int(X/10) %10
    m2 = int(X/100)%10
    m1 = int(X/1000)%10
    h2 = int(X/10000)%10
    h1 = int(X/100000)%10
    digs1.show(s1)
    digs2.show(s2)
    digm1.show(m1)
    digm2.show(m2)
    if h1 > 0:
        digh1.show(h1)
    digh2.show(h2)  
    root.after(1000, update)
root.after(1000, update)
root.mainloop()
