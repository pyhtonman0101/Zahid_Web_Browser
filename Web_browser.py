import webbrowser              #webbrowser module
from tkinter import *          # Module for GUI programming(this line means from tkinter import everything)


def google():
    webbrowser.open_new_tab('www.google.com')

def facebook():
    webbrowser.open_new_tab("www.facebook.com/?ref=tn_tnmn")

def Instagram():
    webbrowser.open_new_tab("www.instagram.com")

def youtube():
    webbrowser.open_new_tab('www.youtube.com')

def amazon():
    webbrowser.open_new_tab('www.amazon.in')

def stackovrflow():
    webbrowser.open_new_tab('stackoverflow.com')

def github():
    webbrowser.open_new_tab('github.com')

def gfg():
    webbrowser.open_new_tab('geeksforgeeks.com')

def search(url):
    webbrowser.open('https://www.google.com/search?q=%s' % url)

#----------------------x-------------------------x---------------------
#Programming for GUI using tkinter

win=Tk()
win.config(bg='black')
win.title('Zahid Web Browser')
label=Label(win,bg='gray14')
label.pack()
frame=Frame(label,bg='gray14')
frame.pack()

ZAhid=Label(frame,bg='gray14',text="ZAHID BROWSER",font=('times new roman',65,'bold'),fg='green2')
ZAhid.grid(row=0,columnspan=3,padx=10,pady=10,)

imagegoogle = PhotoImage(file="google.png")
gbtn=Button(frame,image=imagegoogle,command=lambda:google())
gbtn.grid(row=1,column=0,padx=10,pady=10)

imageface = PhotoImage(file="facebook.png")
fbtn=Button(frame,image=imageface,command=lambda:facebook())
fbtn.grid(row=1,column=1,padx=10,pady=10)

imageIG = PhotoImage(file="instagram.png")
igbtn=Button(frame,image=imageIG,command=lambda:Instagram())
igbtn.grid(row=1,column=2,padx=10,pady=10)

imageamazon = PhotoImage(file="amazon.png")
abtn=Button(frame,image=imageamazon,command=lambda:amazon())
abtn.grid(row=2,column=0,padx=10,pady=10)

imagestack = PhotoImage(file="stackover.png")
sbtn=Button(frame,image=imagestack,command=lambda:stackovrflow())
sbtn.grid(row=2,column=1,padx=10,pady=10)

imagegfg = PhotoImage(file="gfg1.png")
gfgbtn=Button(frame,image=imagegfg,command=lambda:gfg())
gfgbtn.grid(row=3,column=1,padx=10,pady=10,columnspan=2)

imagegit = PhotoImage(file="github.png")
gitbtn=Button(frame,image=imagegit,bg='white',command=lambda:github())
gitbtn.grid(row=3,column=0,padx=10,pady=10)

imageyoutube = PhotoImage(file="youtube.png")
ytbtn=Button(frame,image=imageyoutube,bg='white',command=lambda:youtube())
ytbtn.grid(row=2,column=2,padx=10,pady=10)

searchEntry=Entry(frame,bg='gray14',fg='cyan',text='Enter your Query',relief=SUNKEN,bd=10,font=('Ubuntu', 30))
searchEntry.grid(row=4,column=0,columnspan=2,sticky='W')
searchEntry.config(insertbackground='green2')

searchbtn=Button(frame,text='Search',bg='green2',command=lambda:search(searchEntry.get()),font=('Ubuntu', 20,'bold'),bd=10,fg='black')
searchbtn.grid(row=4,column=2,padx=10,pady=10)

win.mainloop()