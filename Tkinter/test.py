from tkinter import *
from tkinter.ttk import *

import datetime
vandaag = datetime.datetime.today()
s = vandaag.strftime("   %H:%M   ")

root = Tk()
root.configure(background='gold')
frame1 = Frame(master=root)
frame1.place(x = 206, y = 166)

def clicked():
    tekst = s
    label1["text"] = tekst

zero = 0
counter = 0
def laadtabel():
    global counter
    if counter == 1:
        frame1.destroy()
        counter = 0
    else:
        counter = 1
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
                tv.heading("#0", text='Soort trein', anchor='w')
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
                self.treeview.insert('', 'end', text="Sprinter", values=('10:00',
                                     'Uitgeest', '2'))

        def main():
            App(frame1)

        if __name__ == '__main__':
            main()



from tkinter import Button
labeltijd = Label(master=root,
              text=s, background="gold", foreground="white", font=("calibribold", 35))
labeltijd.place(x = 4, y = 96)

labelbovenaan = Label(master=root,
              text="Vertrektijden                                                                                                                                                                                                                                                                       ", background="white", foreground="navy", font=("calibribold", 30))
labelbovenaan.place(x=0, y=0)

labelbanner = Label(master = root, text = "Tijd                                   ", background = "navy", foreground = "white", font=("bold", 14))
labelbanner.place(x = 4, y = 64)

labelbanner2 = Label(master = root, text = "Plan uw reis                                                                                                                                                                                                                ", background = "navy", foreground = "white", font=("bold", 14))
labelbanner2.place(x = 206, y = 64)

button1 = Button(master=root, text='Veenendaal West', foreground="white", background='navy', width=25, height=2, font=("bold", 14), command = laadtabel)
button1.place(x = 206, y = 96)

button2 = Button(master=root, text='Veenendaal Centrum', background="navy", foreground="white", width=25, height=2, font = ("bold", 14), command = laadtabel)
button2.place(x = 494, y = 96)

root.geometry("1000x400")
root.mainloop()

