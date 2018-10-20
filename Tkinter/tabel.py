from tkinter import *
from tkinter.ttk import *


class App(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.CreateUI()
        self.LoadTable()
        self.grid(sticky = (N,S,W,E))
        parent.grid_rowconfigure(0, weight = 1)
        parent.grid_columnconfigure(0, weight = 1)

    def CreateUI(self):
        tv = Treeview(self)
        tv['columns'] = ('vertrek', 'bestemming', 'spoor')
        tv.heading("#0", text='Huidig station', anchor='w')
        tv.column("#0", anchor="w")
        tv.heading('vertrek', text='Vertrek')
        tv.column('vertrek', anchor='center', width=100)
        tv.heading('bestemming', text='Bestemming')
        tv.column('bestemming', anchor='center', width=100)
        tv.heading('spoor', text='Spoor')
        tv.column('spoor', anchor='center', width=100)
        tv.grid(sticky = (N,S,W,E))
        self.treeview = tv
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)

    def LoadTable(self):
        self.treeview.insert('', 'end', text="Veenendaal West", values=('10:00',
                             'Uitgeest', '2'))

def main():
    root = Tk()
    App(root)
    root.mainloop()

if __name__ == '__main__':
    main()