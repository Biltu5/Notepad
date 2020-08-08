from tkinter import *
import time
import tkinter.messagebox as tmsg

class Help:
    def about(self):     
        tmsg.showinfo("About","Simple Notepad create\n      by B Nayak")
    
    def get_time(self):
        self.hours=time.strftime("%I")
        self.minute=time.strftime("%M")
        self.second=time.strftime("%S")
        self.am_pm=time.strftime("%p")
        self.day=time.strftime("%A")
        self.mounth=time.strftime("%B")
        self.year=time.strftime("%Y")
        
    def showTime(self):
        self.get_time()
        tmsg.showinfo("Time","      "+self.hours+" : "+self.minute+" : "+self.second+" "+self.am_pm+"\n"+self.day+","+self.mounth+","+self.year)
    
def main1(root,text,menubar):
    obj=Help()
    HMenu=Menu(menubar)
    HMenu.add_command(label="Time",command=obj.showTime)
    HMenu.add_command(label="About", command=obj.about)
    menubar.add_cascade(label="Help",menu=HMenu)
    root.config(menu=menubar)
    
    