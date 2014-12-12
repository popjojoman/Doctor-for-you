from Tkinter import *
import tkMessageBox
days_w, days_m = 7, 30

class App(object):
    
    def __init__(self):
        
        self.root = Tk()
        self.root.geometry("400x200+550+300")
        self.root.wm_title("My salary")
        Label(self.root, text = 'Please Choose form').place(relx=0.5, rely=0.25, anchor = CENTER)       

        week = Button(self.root, text = 'Week form', height = 2, width = 25, command = self.destroyers)
        week.place(relx=0.5, rely=0.5,anchor = CENTER)
        month = Button(self.root, text = 'Month form', height = 2, width = 25, command = self.destroyers2)
        month.place(relx=0.5, rely=0.75,anchor = CENTER)   

        self.root.mainloop()

##    def clicked1(self):
##        input = self.entrytext.get()
##        result = int(input)*2
##        self.label.configure(text=result)

    def destroyers(self):
        self.root.destroy()
        Check_days(days_w)

    def destroyers2(self):
        self.root.destroy()
        Check_days(days_m)


class Check_days(object):
    
    def __init__(self, days):
        self.ask_work = Tk()
        self.ask_work.geometry("300x200+600+300")
        self.ask_work.wm_title("My salary")

        if days == 7:
            Label(self.ask_work, text='How many days do you work in 1 week ? ').place(relx=0.15, rely=0.2)
            Button(self.ask_work, text='OK', command= self.open_calculate).place(relx=0.4, rely=0.7)
            Button(self.ask_work, text='Back', command= self.destroyer).place(relx=0.5, rely=0.7)
        else:
            Label(self.ask_work, text='How many days do you work in 1 month ? ').place(relx=0.15, rely=0.2)
            Button(self.ask_work, text='OK', command= self.open_calculate2).place(relx=0.4, rely=0.7)
            Button(self.ask_work, text='Back', command= self.destroyer).place(relx=0.5, rely=0.7)

        self.workday = IntVar()
        Entry(self.ask_work, textvariable=self.workday, justify='center', bd = 5).place(relx=0.3, rely=0.45)
        

    def open_calculate(self):
        days = 7
        result = Check_moredays(days, self.workday.get())
        call_result = result.calculate_day()

        if call_result == True:
            self.ask_work.destroy()
            Pattern(self.workday.get())
        else:
            if self.workday == 0:
                tkMessageBox.showwarning("Error", "Error day out of range in 1 week")
            else:
                tkMessageBox.showwarning("Error", "Error input have more than one day")

    def open_calculate2(self):
        days = 30
        self.result = Check_moredays(days, self.workday.get())
        self.call_calculate = self.result.calculate_day()

        if self.call_calculate == True:
            self.ask_work.destroy()
            Pattern(self.workday.get())
        else:
            if self.workday == 0:
                tkMessageBox.showwarning("Error", "Error day out of range in 1 month")
            else:
                tkMessageBox.showwarning("Error", "Error input have more than one day")


    def destroyer(self):
        self.ask_work.destroy()
        App()

    def open_from(self):
        self.ask_work.destroy()
        Pattern()



class Check_moredays(object):
    def __init__(self, days, workday):
        self.workday = workday
        self.days = days

    def calculate_day(self):
        return False if self.workday > self.days or self.workday == 0 else True

##------------------------------------------------------- Pattern --------------------------------------------------------------------
class Pattern(object):

    def __init__(self, workday):
        week = Tk()
        week.geometry("600x300+500+250")
        week.wm_title("My salary")
        listtime = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        hour_in, hour_out = [0, 0], [0, 0]
        minute_in, minute_out = [0, 0], [0, 0]

        num_hour_in, num_hour_out = int(str(hour_in[0])+str(hour_in[1])), int(str(hour_out[0])+str(hour_out[1]))
        num_minute_in, num_minute_out = int(str(minute_in[0])+str(minute_in[1])), int(str(minute_out[0])+str(minute_out[1]))
        

        self.workday = workday

        week.geometry("600x300+500+250")
        week.wm_title("My salary")
        Label(week, text = 'Earnings Per Hours :', ).place(relx=0.30, rely=0.1)

        self.earn = IntVar()
        Entry(week, textvariable=self.earn, justify='center', bd = 5).place(relx=0.50, rely=0.1)
        
##------------------------------------------- TIME SUB IN -----------------------------------------------------------------------

    ##------------------------------------ SUB TIME IN HOURS ----------------------------------------------------

        def w_hrl(self, index, mode):
            hrl = week.globalgetvar(self)
            hour_in[0] = hrl
            print 'HOURS : ', hour_in, minute_in, 'MINUTE : ', hour_out, minute_out
            if hrl >= hour_out[0]:
                week.hourleft2 = StringVar(week)
                week.hourleft2.trace('w', w_hrl2)
                week.hourleft2.set(listtime[hrl])
                OptionMenu(week,week.hourleft2, *listtime[hrl:3]).place(relx=0.6, rely=0.35)
                if hrl == 2:
                    week.hourright = StringVar(week)
                    week.hourright.trace('w', w_hrr)
                    week.hourright.set(listtime[0])
                    OptionMenu(week,week.hourright, *listtime[hour_in[1]:5]).place(relx=0.1, rely=0.35)

                    week.hourright2 = StringVar(week)
                    week.hourright2.trace('w', w_hrr2)
                    week.hourright2.set(listtime[0])
                    OptionMenu(week,week.hourright2, *listtime[hour_out[1]:5]).place(relx=0.69, rely=0.35)
                else:
                    week.hourright = StringVar(week)
                    week.hourright.trace('w', w_hrr)
                    week.hourright.set(listtime[hour_in[1]])
                    OptionMenu(week,week.hourright, *listtime).place(relx=0.1, rely=0.35)
            else:
                week.hourleft2 = StringVar(week)
                week.hourleft2.trace('w', w_hrl2)
                week.hourleft2.set(listtime[hour_out[0]])
                OptionMenu(week,week.hourleft2, *listtime[hour_in[0]:3]).place(relx=0.6, rely=0.35)
                if hrl == 2:
                    week.hourright = StringVar(week)
                    week.hourright.trace('w', w_hrr)
                    week.hourright.set(listtime[0])
                    OptionMenu(week,week.hourright, *listtime).place(relx=0.1, rely=0.35)
                else:
                    week.hourright = StringVar(week)
                    week.hourright.trace('w', w_hrr)
                    week.hourright.set(listtime[hour_in[1]])
                    OptionMenu(week,week.hourright, *listtime).place(relx=0.1, rely=0.35)
                 
        def w_hrr(self, index, mode):
            hrr = week.globalgetvar(self)
            hour_in[1] = hrr
            print 'HOURS : ', hour_in, minute_in, 'MINUTE : ', hour_out, minute_out

            if hour_out[0] != 2 and hour_out[0] == hour_in[0]:

                if hour_in[1] >= hour_out[1]:
                    week.hourright2 = StringVar(week)
                    week.hourright2.trace('w', w_hrr2)
                    week.hourright2.set(listtime[hour_in[1]])
                    OptionMenu(week,week.hourright2, *listtime[hour_in[1]::]).place(relx=0.69, rely=0.35)
                else:
                    week.hourright2 = StringVar(week)
                    week.hourright2.trace('w', w_hrr2)
                    week.hourright2.set(listtime[hour_out[1]])
                    OptionMenu(week,week.hourright2, *listtime[hour_in[1]::]).place(relx=0.69, rely=0.35)

            elif hour_out[0] == 2 and hour_in[0] == 2:

                if hour_in[1] >= hour_out[1]:
                    week.hourright2 = StringVar(week)
                    week.hourright2.trace('w', w_hrr2)
                    week.hourright2.set(listtime[hour_in[1]])
                    OptionMenu(week,week.hourright2, *listtime[hour_in[1]:5]).place(relx=0.69, rely=0.35)
                else:
                    week.hourright2 = StringVar(week)
                    week.hourright2.trace('w', w_hrr2)
                    week.hourright2.set(listtime[hour_out[1]])
                    OptionMenu(week,week.hourright2, *listtime[hour_in[1]:5]).place(relx=0.69, rely=0.35)

            elif hour_out[0] == 2 and hour_in[0] != 2:

                if hour_in[1] >= hour_out[1]:
                    week.hourright2 = StringVar(week)
                    week.hourright2.trace('w', w_hrr2)
                    week.hourright2.set(listtime[hour_out[1]])
                    OptionMenu(week,week.hourright2, *listtime[hour_out[1]:5]).place(relx=0.69, rely=0.35)
                else:
                    week.hourright2 = StringVar(week)
                    week.hourright2.trace('w', w_hrr2)
                    week.hourright2.set(listtime[hour_out[1]])
                    OptionMenu(week,week.hourright2, *listtime[hour_in[1]:5]).place(relx=0.69, rely=0.35)
            else:
                week.hourright2 = StringVar(week)
                week.hourright2.trace('w', w_hrr2)
                week.hourright2.set(listtime[hour_out[1]])
                OptionMenu(week,week.hourright2, *listtime).place(relx=0.69, rely=0.35)

    ##----------------------------------- SUB TIME IN MINUTES-------------------------------------------------
        def w_mnl(self, index, mode):
            mnl = week.globalgetvar(self)
            minute_in[0] = mnl
            print 'HOURS : ', hour_in, minute_in, 'MINUTE : ', hour_out, minute_out

            if (hour_in[0] == hour_out[0]) and (hour_in[1] == hour_out[1]):
                if minute_in[0] >= minute_out[0]:
                    week.minuteleft2 = StringVar(week)
                    week.minuteleft2.trace('w', w_mnl2)
                    week.minuteleft2.set(listtime[minute_in[0]])
                    OptionMenu(week,week.minuteleft2, *listtime[minute_in[0]:6]).place(relx=0.82, rely=0.35)
                else:
                    week.minuteleft2 = StringVar(week)
                    week.minuteleft2.trace('w', w_mnl2)
                    week.minuteleft2.set(listtime[minute_out[0]])
                    OptionMenu(week,week.minuteleft2, *listtime[minute_in[0]:6]).place(relx=0.82, rely=0.35)

        def w_mnr(self, index, mode):
            mnr = week.globalgetvar(self)
            minute_in[1] = mnr
            print 'HOURS : ', hour_in, minute_in, 'MINUTE : ', hour_out, minute_out

            if (hour_in[0] == hour_out[0]) and (hour_in[1] == hour_out[1]):
                if minute_in[1] >= minute_out[1]:
                    week.minuteright2 = StringVar(week)
                    week.minuteright2.trace('w', w_mnr2)
                    week.minuteright2.set(listtime[minute_in[1]])
                    OptionMenu(week,week.minuteright2, *listtime[minute_in[1]::]).place(relx=0.91, rely=0.35)
                else:
                    week.minuteright2 = StringVar(week)
                    week.minuteright2.trace('w', w_mnr2)
                    week.minuteright2.set(listtime[minute_out[1]])
                    OptionMenu(week,week.minuteright2, *listtime[minute_in[1]::]).place(relx=0.91, rely=0.35)


##----------------------------------------- SUB TIME OUT ----------------------------------------------------------------------------
    
    ##---------------------------------- SUB TIME OUT HOURS---------------------------------------------------

        def w_hrl2(self, index, mode):
            hrl2 = week.globalgetvar(self)
            hour_out[0] = hrl2
            print 'HOURS : ', hour_in, minute_in, 'MINUTE : ', hour_out, minute_out
            if hrl2 == 2:
                week.hourright2 = StringVar(week)
                week.hourright2.trace('w', w_hrr2)
                week.hourright2.set(listtime[0])
                OptionMenu(week,week.hourright2, *listtime[hour_out[1]:5]).place(relx=0.69, rely=0.35)
            elif hrl2 == hour_in[0]:
                week.hourright2 = StringVar(week)
                week.hourright2.trace('w', w_hrr2)
                week.hourright2.set(listtime[hour_in[1]])
                OptionMenu(week,week.hourright2, *listtime[hour_in[1]::]).place(relx=0.69, rely=0.35)
            else:
                week.hourright2 = StringVar(week)
                week.hourright2.trace('w', w_hrr2)
                week.hourright2.set(listtime[hour_out[1]])
                OptionMenu(week,week.hourright2, *listtime).place(relx=0.69, rely=0.35)
            

        def w_hrr2(self, index, mode):
            hrr2 = week.globalgetvar(self)
            hour_out[1] = hrr2
            print 'HOURS : ', hour_in, minute_in, 'MINUTE : ', hour_out, minute_out


    ##-------------------------------- SUB TIME OUT MINUTE------------------------------------------
        def w_mnl2(self, index, mode):
            mnl2 = week.globalgetvar(self)
            minute_out[0] = mnl2
            print 'HOURS : ', hour_in, minute_in, 'MINUTE : ', hour_out, minute_out


        def w_mnr2(self, index, mode):
            mnr2 = week.globalgetvar(self)
            minute_out[1] = mnr2
            print 'HOURS : ', hour_in, minute_in, 'MINUTE : ', hour_out, minute_out
            

##------------------------------------------------------------------------------------------------------------------------
                
        

        

##------------------------------------------------------ TIME IN ---------------------------------------------------------------

      
        self.hourleft = StringVar(week)
        self.hourleft.trace('w', w_hrl)
        self.hourleft.set(listtime[0])
        OptionMenu(week,self.hourleft, *listtime[0:3]).place(relx=0.01, rely=0.35)
        
        self.hourright = StringVar(week)
        self.hourright.trace('w', w_hrr)
        self.hourright.set(listtime[0])
        OptionMenu(week,self.hourright, *listtime).place(relx=0.1, rely=0.35)
        
        
        Label(week, text = ':', ).place(relx=0.2, rely=0.36)
        Label(week, text = 'What time do you start your work?', ).place(relx=0.05, rely=0.26)
        

        self.minuteleft = StringVar(week)
        self.minuteleft.trace('w', w_mnl)
        self.minuteleft.set(listtime[0])
        OptionMenu(week,self.minuteleft, *listtime[:6]).place(relx=0.23, rely=0.35)

        self.minuteright = StringVar(week)
        self.minuteright.trace('w', w_mnr)
        self.minuteright.set(listtime[0])
        OptionMenu(week,self.minuteright, *listtime).place(relx=0.32, rely=0.35)



##------------------------------------------------------ TIME OUT ------------------------------------------------------------------
        
        self.hourleft2 = StringVar(week)
        self.hourleft2.trace('w', w_hrl2)
        self.hourleft2.set(listtime[0])
        OptionMenu(week,self.hourleft2, *listtime[0:3]).place(relx=0.6, rely=0.35)

        self.hourright2 = StringVar(week)
        self.hourright2.trace('w', w_hrr2)
        self.hourright2.set(listtime[0])
        OptionMenu(week,self.hourright2, *listtime).place(relx=0.69, rely=0.35)
        
        
        Label(week, text = ':', ).place(relx=0.79, rely=0.36)
        Label(week, text = 'What time do you knock off?', ).place(relx=0.65, rely=0.26)

        self.minuteleft2 = StringVar(week)
        self.minuteleft2.trace('w', w_mnl2)
        self.minuteleft2.set(listtime[0])
        OptionMenu(week,self.minuteleft2, *listtime[:6]).place(relx=0.82, rely=0.35)

        self.minuteright2 = StringVar(week)
        self.minuteright2.trace('w', w_mnr2)
        self.minuteright2.set(listtime[0])
        OptionMenu(week,self.minuteright2, *listtime).place(relx=0.91, rely=0.35)



##--------------------------------------------------------Break------------------------------------------------------

        label = Label(week, text= 'Do you take a break ?')
        label.place(relx=0.42, rely=0.52)

    ##----------------------------------------destroytext and replace textbox ---------------------------------

        def button_yes():

            label.place_forget()

            butt_back.place(relx=0.65, rely=0.52)
            textbreak.place(relx=0.455, rely=0.48)    
            breaks.place(relx=0.4, rely=0.57)

        def button_back():

            textbreak.place_forget()
            breaks.place_forget()
            butt_back.place_forget()

            self.breaks.set(0)

            label.place(relx=0.42, rely=0.52)


        def new_windows():
            def back_2_week():
                week.deiconify()
                new_win.withdraw()
                
            week.withdraw()

            new_win = Tk()
            new_win.geometry("250x200+650+300")
            new_win.wm_title("My salary")
            
            Label(new_win, text = 'Please select the number of working days').place(relx=0.038, rely=0.2)

            listweek = map(int, xrange(31))

            work_days = IntVar(new_win)
            work_days.set(1)
            OptionMenu(new_win, work_days, *listweek[1:self.workday+1]).place(relx=0.4, rely=0.4)

            Button(new_win,text='OK', command = back_2_week).place(relx=0.4, rely=0.7)

        
               

        def cancel():
            week.destroy()
            App()
            
        textbreak = Label(week, text = 'Break time', )
        

        self.breaks = IntVar()
        breaks = Entry(week, textvariable=self.breaks, justify='center', bd = 5)

        butt_yes = Button(week, text='Yes', command =button_yes)
        butt_yes.place(relx=0.65, rely=0.52)

        butt_back = Button(week, text='Back', command = button_back)
        butt_submit = Button(week, text = 'Submit', command = new_windows,  height = 1, width = 10)
        butt_cancel = Button(week, text = 'Cancel',command = cancel,  height = 1, width = 10)

        butt_submit.place(relx=0.35, rely=0.71)
        butt_cancel.place(relx=0.53, rely=0.71)
        
         
        
        week.mainloop()



        
if __name__ == '__main__':
    App()
