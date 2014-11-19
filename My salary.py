from Tkinter import *
import tkMessageBox
class App(object):
    def __init__(self):
        self.root = Tk()
        self.root.geometry("400x200+600+300")
        self.root.wm_title("My salary")
        

       # self.entryuser = StringVar()
       # Entry(self.root, textvariable=self.entryuser).place(relx=0.5, rely=0.2)


       # self.entrypass = StringVar()
       # Entry(self.root, show='*', textvariable=self.entrypass).place(relx=0.5, rely=0.4)
        Label(self.root, text = 'Please Choose form').place(relx=0.5, rely=0.25, anchor = CENTER)       

        
        Button(self.root, text = 'Week form', height = 2, width = 25, command = self.open_week)\
                          .place(relx=0.5, rely=0.5,anchor = CENTER)
        Button(self.root, text = 'Month form', height = 2, width = 25, command = self.open_month)\
                          .place(relx=0.5, rely=0.75,anchor = CENTER)


       # self.buttontext = StringVar()
       # self.buttontext.set("Login")
       # Button(self.root, textvariable=self.buttontext, command=self.open_new)\
        #                  .place(relx=0.5, rely=0.8, anchor=CENTER)

        self.root.mainloop()
        
    def open_week(self):
        self.root.destroy()
        Pattern_week()

    def open_month(self):
        self.root.destroy()
        Pattern_month()


##    def clicked1(self):
##        input = self.entrytext.get()
##        result = int(input)*2
##        self.label.configure(text=result)
        
##    def button_click(self):
##        tkMessageBox.showwarning("Error", "Bad username and password")
        
class Pattern_week(object):
    def __init__(self):
        self.week = Tk()
        self.week.geometry("600x300+500+250")
        self.week.wm_title("My salary")

class Pattern_month(object):
    def __init__(self):
        self.month = Tk()
        self.month.geometry("600x300+500+250")
        self.month.wm_title("My salary")   

        
if __name__ == '__main__':
    App()
