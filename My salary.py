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
        week = Tk()
        week.geometry("600x300+500+250")
        week.wm_title("My salary")
        Label(week, text = 'earnings', )
        listtime = [0,1,2,3,4,5,6,7,8,9]
        
        def show(self, index, mode):
            num = week.globalgetvar(self)
            if num == 2:
                week.hourright = StringVar(week)
                week.hourright.set(listtime[0])
                OptionMenu(week,week.hourright, *listtime[0:4]).place(relx=0.19, rely=0.35)
            else:
                week.hourright = StringVar(week)
                week.hourright.set(listtime[0])
                OptionMenu(week,week.hourright, *listtime).place(relx=0.19, rely=0.35)
                
        
        week.geometry("600x300+500+250")
        week.wm_title("My salary")
        Label(week, text = 'Earnings Per Hours :', ).place(relx=0.25, rely=0.1)

        self.earn= StringVar(week)
        Entry(week, textvariable=self.earn).place(relx=0.45, rely=0.1)
        
        
        self.hourleft = StringVar(week)
        self.hourleft.trace('w', show)
        
        self.hourleft.set(listtime[0])
        OptionMenu(week,self.hourleft, *listtime[0:3]).place(relx=0.1, rely=0.35)

        self.hourright = StringVar(week)
        self.hourright.set(listtime[0])
        OptionMenu(week,self.hourright, *listtime).place(relx=0.19, rely=0.35)
        
        
        Label(week, text = ':', ).place(relx=0.29, rely=0.36)

        self.minuteleft = StringVar(week)
        self.minuteleft.set(listtime[0])
        OptionMenu(week,self.minuteleft, *listtime[:6]).place(relx=0.32, rely=0.35)

        self.minuteright = StringVar(week)
        self.minuteright.set(listtime[0])
        OptionMenu(week,self.minuteright, *listtime).place(relx=0.41, rely=0.35)
        
        week.mainloop()

class Pattern_month(object):
    def __init__(self):
        self.month = Tk()
        self.month.geometry("600x300+500+250")
        self.month.wm_title("My salary")   

        
if __name__ == '__main__':
    App()
