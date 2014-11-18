from Tkinter import *
import tkMessageBox
class App(object):
    def __init__(self):
        self.root = Tk()
        self.root.geometry("450x250+450+250")
        self.root.wm_title("My salary")
       # Label (self.root, text= "Enter your username. : ").place(relx=0.05, rely=0.2)
       # Label (self.root, text= "Enter your password. : ").place(relx=0.05, rely=0.4)
        

       # self.entryuser = StringVar()
       # Entry(self.root, textvariable=self.entryuser).place(relx=0.5, rely=0.2)


       # self.entrypass = StringVar()
       # Entry(self.root, show='*', textvariable=self.entrypass).place(relx=0.5, rely=0.4)
        Label(self.root, text = 'Please Choose form').place(relx=0.5, rely=0.25, anchor = CENTER)       



        
        Button(self.root, text = 'Week form', height = 2, width = 25).place(relx=0.5, rely=0.5,anchor = CENTER)
        Button(self.root, text = 'Month form', height = 2, width = 25).place(relx=0.5, rely=0.75,anchor = CENTER)


       # self.buttontext = StringVar()
       # self.buttontext.set("Login")
       # Button(self.root, textvariable=self.buttontext, command=self.open_new)\
        #                  .place(relx=0.5, rely=0.8, anchor=CENTER)

        self.root.mainloop()
    def open_new(self):
        self.root.destroy()
        Windows()


##    def clicked1(self):
##        input = self.entrytext.get()
##        result = int(input)*2
##        self.label.configure(text=result)
        
##    def button_click(self):
##        tkMessageBox.showwarning("Error", "Bad username and password")
        
class Windows(object):
    def __init__(self):
        self.win2 = Tk()
        self.win2.geometry("600x300+500+250")

        
if __name__ == '__main__':
    App()
