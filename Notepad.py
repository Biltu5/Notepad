from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.scrolledtext import *
import File_menu
import Edit_menu
import Format_menu
import Help_menu

root = Tk()

root.title("Text Editor-Untiltled")
root.geometry("300x250+300+300")
root.wm_iconbitmap("Notepad_icon.ico")
root.minsize(width=400, height=400)

text = ScrolledText(root, state='normal', height=400, width=400, wrap='word', pady=2, padx=3, undo=True)
text.pack(fill=Y, expand=1)
text.focus_set()

menubar=Menu(root)
File_menu.main1(root,text,menubar)
Edit_menu.main1(root,text,menubar)
Format_menu.main1(root,text,menubar)
Help_menu.main1(root,text,menubar)
root.mainloop()
