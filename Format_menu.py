from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.scrolledtext import *
from tkinter.colorchooser import askcolor
from tkinter.font import *

class Format:
    def __init__(self,text):
        self.text=text
    
    def changebg(self):
        (triple, color)=askcolor()
        if color:
            self.text.config(bg=color)
            
 #If the user clicks the OK button on the pop-up, the returned value will be a tuple (triple, color), where triple is a tuple (R, G, B) containing red, green, and blue values in the range [0,255] respectively, and color is the selected color as a regular Tkinter color object.
# If the users clicks Cancel, this function will return (None, None).
    
    def changefg(self):
        (triple, color)=askcolor()
        if color:
            self.text.config(fg=color)
    
    def italicText(self):
        #works only if text is selected
        try:
            current_tags = self.text.tag_names("sel.first")
            if "italic" in current_tags:
                self.text.tag_remove("italic", "sel.first", "sel.last")
            else:
                self.text.tag_add("italic", "sel.first", "sel.last")
                italic_font = Font(self.text, self.text.cget("font"))
                italic_font.configure(slant="italic")
                self.text.tag_configure("italic", font=italic_font)
        except:
            pass
    
    def overstrickText(self):
        #works only if text is selected
        try:
            current_tags = self.text.tag_names("sel.first")
            if "overstrike" in current_tags:
                self.text.tag_remove("overstrike", "sel.first", "sel.last")
            else:
                self.text.tag_add("overstrike", "sel.first", "sel.last")
                overstrike_font = Font(self.text, self.text.cget("font"))
                overstrike_font.configure(overstrike=1)
                self.text.tag_configure("overstrike", font=overstrike_font)
        except:
            pass
    
    def underlineText(self):
        #works only if text is selected
        try:
            current_tags = self.text.tag_names("sel.first")
            if "underline" in current_tags:
                self.text.tag_remove("underline", "sel.first", "sel.last")
            else:
                self.text.tag_add("underline", "sel.first", "sel.last")
                underline_font = Font(self.text, self.text.cget("font"))
                underline_font.configure(underline=1)
                self.text.tag_configure("underline", font=underline_font)
        except:
            pass
       
    def boldText(self,*args):
        #works only if text is selected
        try:
            current_tag=self.text.tag_names("sel.first")
            if "bold" in current_tag:
                self.text.tag_remove("bold","sel.first","sel.last")
            else:
                self.text.tag_add("bold","sel.first","sel.last")
                bold_font=Font(self.text,self.text.cget("font"))
#cget(self, key)
#Return the resource value for a KEY given as string.
                bold_font.configure(weight="bold")
                self.text.tag_configure("bold",font=bold_font)
        except :
            pass
        
def main1(root,text,menubar):
    obj=Format(text)
    fontOptions=families(root)
    font1=Font(family="Arial",size=11)  
    text.configure(font=font1)
    
    FMenu=Menu(menubar)
    fsubmenu=Menu(FMenu,tearoff=0)
    ssubmenu=Menu(FMenu,tearoff=0)
    
    for option in fontOptions:
        fsubmenu.add_command(label=option, command=lambda option=option: font1.config(family=option))
        
    for I in range(1,31):
       ssubmenu.add_command(label=str(I), command=lambda I=I:font1.configure(size=I))     
       
    FMenu.add_command(label="Change Background", command=obj.changebg)
    FMenu.add_command(label="Change Font Color", command=obj.changefg)
    FMenu.add_cascade(label="Font", underline=0,menu=fsubmenu)
    FMenu.add_cascade(label="Size", underline=0,menu=ssubmenu)
    FMenu.add_command(label="Bold", command=obj.boldText, accelerator="Ctrl+B")
    FMenu.add_command(label="Italic", command=obj.italicText, accelerator="Ctrl+I")
    FMenu.add_command(label="Underline", command=obj.underlineText, accelerator="Ctrl+U")
    FMenu.add_command(label="Overstrick", command=obj.overstrickText,accelerator="Ctrl+O")
    menubar.add_cascade(label="Format",menu=FMenu)
    root.configure(menu=menubar)
    
    root.bind_all("<Control-b>",obj.boldText)
    root.bind_all("<Control-i>",obj.italicText)
    root.bind_all("<Control-u>",obj.underlineText)
    root.bind_all("<Control-o>",obj.overstrickText)
    
if __name__=='__main__':
    root=Tk()
    text = ScrolledText(root, state='normal', height=400, width=400, wrap='word', pady=2, padx=3, undo=True)
    text.pack(fill=Y, expand=1)
    text.focus_set()
    menubar=Menu(root)
    main1(root,text,menubar)
    root.mainloop()