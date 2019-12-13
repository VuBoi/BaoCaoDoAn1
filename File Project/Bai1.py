from functools import partial
import tkinter as tk

class FieldUI(tk.Canvas):
    def __init__(self, parent, sizew, sizeh, variable):
        tk.Canvas.__init__(self, parent, width=sizew, height=sizeh)
        self.sizew = sizew
        self.sizeh = sizeh
        self.variable = variable
        self.variable.trace('w', self.update_display)
        self.update_display()
    def update_display(self, *_args):
        self.delete(tk.ALL)
        value = self.variable.get()
        if value == 'x':
            self.create_line(0, 0, self.sizew, self.sizeh, width=1)
            self.create_line(self.sizew, 0, 0, self.sizeh, width=1)
        elif value == 'y':
            self.delete()
class Board(tk.Frame):
    def __init__(self, parent = None):
        tk.Frame.__init__(self, parent, background='black') ## call board
        self.field_vars = [tk.StringVar() for _ in range(25)] ## size board
        for i, field_var in enumerate(self.field_vars):
            field_ui = FieldUI(self, 238, 138, field_var) ##size board mini
            field_ui.bind('<Button-1>', partial(self.on_click1, i))
            field_ui.bind('<Button-3>', partial(self.on_click2, i))
            column, row = divmod(i, 5) ## number row
            field_ui.grid(row=row, column=column, padx=0, pady=0) ##line bettwen row and column
            field_ui.configure(highlightthickness=1, highlightbackground="black") 
    def on_click1(self, field_index, _event=None):
        field_var = self.field_vars[field_index]
        field_var.set('x')
    def on_click2(self, field_index, _event=None):
        field_var = self.field_vars[field_index]
        field_var.set('y')
    def deleteline(self,field_ui, event): 
        field_ui.delete()
if __name__ == '__main__':
    root = tk.Tk()
    root.wm_title("Demo Checker Beta")
    root.resizable(width= False, height= False)
    root.geometry("1200x700+350+150")
    board = Board(root)
    board.pack()
    root.mainloop()


