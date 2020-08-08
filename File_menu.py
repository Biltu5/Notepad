from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter.simpledialog import *
from fpdf import FPDF
import sys

class File:
    def __init__(self,text,root):
        self.root=root
        self.text=text
        self.filename=None
    
    def add_NewFile(self):
       self.filename='Untitled'
       self.root.title("Untitled - Notepad")
       self.text.delete(0.0,END)
        
    def add_OpenFile(self):
        f=askopenfile(mode='r')
        try:
            self.filename=f.name
            self.root.title(self.filename + " - Notepad")
            t=f.read()
            self.text.delete(0.0,END)
            self.text.insert(0.0,t)
        except:
            pass
            
    def add_Save(self):
        try:
            t = self.text.get(0.0, END)
            f = open(self.filename, 'w')
            f.write(t)
            f.close()
        except:
            self.add_Save_as()
    
    def add_Save_as(self):
        t=asksaveasfile(mode="w",defaultextension=".txt")
        f=self.text.get(0.0,END)
        try:
            t.write(f.rstrip())
            #Python rstrip() method removes all the trailing characters from the string.It removes all white spaces from right side.
        except:
            showerror("Oops!","Unable to save file")
        
    def generatePDF(self):
        t=askstring("PDF","Enter your file Name :")
        data=self.text.get(1.0,END)
        try:
            f=open("file.txt","w")
            f.write(data.rstrip())
            f.close()
            
            pdf = FPDF() 
            pdf.add_page() 
            pdf.set_font("Arial", size = 15) 
            f = open("file.txt", "r") 
            for x in f:
                pdf.multi_cell(200, 10, txt = x,align = 'C')
#This method allows printing text with line breaks. They can be automatic (as soon as the text reaches the right border of the cell) or explicit (via the \n character). As many cells as necessary are output, one below the other. Text can be aligned, centered or justified. The cell block can be framed and the background painted.
            pdf.output(t)   
        except:
            pass
    
    def add_Quite(self):
        ans=askyesno("Quite","Are you sure you want to quite ?")
        if ans:
            self.root.destroy()
    
def main1(root,text,menubar):
    FMenu=Menu(root,tearoff=0)
    obj=File(text,root)
    FMenu.add_command(label="New", command=obj.add_NewFile, accelerator="Ctrl+N")
    FMenu.add_command(label="Open", command=obj.add_OpenFile, accelerator="Ctrl+O")
    FMenu.add_command(label="save", command=obj.add_Save, accelerator="Ctrl+S")
    FMenu.add_command(label="Save as...",command=obj.add_Save_as)
    FMenu.add_command(label="Save as PDF", command=obj.generatePDF)
    FMenu.add_separator()
    FMenu.add_command(label="Quite", command=obj.add_Quite, accelerator="Ctrl+Q")
    menubar.add_cascade(label="File",menu=FMenu)
    root.configure(menu=menubar)
    
    root.bind_all("<Control-n>",obj.add_NewFile)
    root.bind_all("<Control-o>",obj.add_OpenFile)
    root.bind_all("<Control-s>",obj.add_Save)
    root.bind_all("<Control-q>",obj.add_Quite)
    
if __name__=='__main__':
    print("welcome Nayak")
    
    
