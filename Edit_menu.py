from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import *
from tkinter.simpledialog import *

class File:
    def pop_up(self, event):
        #a popup menu is created in the same way, but is explicitly displayed, using the post method
        self.rightclick.post(event.x_root,event.y_root)
    def __init__(self,root,text):
        self.clipboard=None
        self.text=text
        self.rightclick=Menu(root)
          
    def cutFile(self,*args):
        #self.text.event_generate(("<<Cut>>"))
        sel=self.text.selection_get()
        self.clipboard=sel
        self.text.delete(SEL_FIRST,SEL_LAST)
    
    def copyFile(self,*args):
        #self.text.event_generate(("<<Copy>>"))
        try:
            sel=self.text.selection_get()
            self.clipboard=sel
        except :
            pass
    
    def pasteFile(self,*args):
        #self.text.event_generate(("<<Paste>>"))
        self.text.insert(INSERT,self.clipboard)
    
    def undoFile(self,*args):
        self.text.edit_undo()
    
    def redoFile(self,*args):
        self.text.edit_redo()
    
    def findFile(self,*args):
        self.text.tag_remove('found',1.0,END)
        target=askstring('Find','Search String :')
        if target:
            idx='1.0'
            while 1:
                idx=self.text.search(target,idx,nocase=1,stopindex=END)
                if not idx: break
                lastidx='%s+%dc' %(idx,len(target))
                self.text.tag_add('found',idx,lastidx)
                idx=lastidx
                self.text.tag_configure('found', foreground='white', background='blue')
    
    def select_all(self,*args):
        self.text.tag_add(SEL,1.0,END)
        self.text.mark_set(0.0,END)
        self.text.see(INSERT)
    
def main1(root,text,menubar):
    obj=File(root,text)
    EMenu=Menu(menubar,tearoff=0)
    EMenu.add_command(label="Cut", command=obj.cutFile, accelerator="Ctrl+X")
    EMenu.add_command(label="Copy",command=obj.copyFile,accelerator="Ctrl+C")
    EMenu.add_command(label="Paste", command=obj.pasteFile,accelerator="Ctrl+V")
    EMenu.add_command(label="Undo", command=obj.undoFile,accelerator="Ctrl+Z")
    EMenu.add_command(label="Redo", command=obj.redoFile,accelerator="Ctrl+Y")
    EMenu.add_command(label="Find", command=obj.findFile,accelerator="Ctrl+F")
    EMenu.add_separator()
    EMenu.add_command(label="Select all", command=obj.select_all,accelerator="Ctrl+A")
    menubar.add_cascade(label="Edit",menu=EMenu)
    root.config(menu=menubar)
    
    root.bind_all("<Control-f>",obj.findFile)
    root.bind_all("<Control-z>",obj.undoFile)
    root.bind_all("<Control-y>",obj.redoFile)
    root.bind_all("<Control-c>",obj.copyFile)
    root.bind_all("<Control-v>",obj.pasteFile)
    root.bind_all("<Control-x>",obj.cutFile)
    root.bind_all("<Control-a>",obj.select_all)
    
    obj.rightclick.add_command(label="Cut", command=obj.cutFile)
    obj.rightclick.add_command(label="Copy", command=obj.copyFile)
    obj.rightclick.add_command(label="Paste", command=obj.pasteFile)
    obj.rightclick.add_separator()
    obj.rightclick.add_command(label="Select All", command=obj.select_all)
   # obj.rightclick.bind("<Control-a>",obj.select_all)
    
    text.bind("<Button-3>",obj.pop_up)
    
    root.config(menu=menubar)
    
if __name__=='__main__':
    print("Welcome to edit menu")
      
#tag_add(self, tagName, index1, *args)
#Add tag TAGNAME to all characters between INDEX1 and index2 in ARGS.
#Additional pairs of indices may follow in ARGS.

#mark_set(self, markName, index)
#Set mark MARKNAME before the character at INDEX

#see(self, index)
#Scroll such that the character at INDEX is visible.

