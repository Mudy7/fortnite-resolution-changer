from tkinter import *
from getpass import getuser
from time import sleep



class app:

    def __init__(self, master):
        self.master = master
        master.title("Fortnite stretcher")
        self.list = []
        self.main()



    def main(self):
        fm = Frame(root,width=500, height=150, bg="#f54242")
        fm.pack()

        label1=Label(root,bg="#f54242",text="Resolution?",font=("helvetica", 12))
        label1.place(x=200,y=5)
        self.list.append(label1)

        self.resolution = StringVar()
        entry1 = Entry(root,textvariable=self.resolution)
        entry1.place(x=175,y=50)
        self.list.append(entry1)

        button1 = Button(root,text="change res",height=1,width=20,font=("helvetica", 10),command=self.change)
        button1.place(x=155,y=90)
        self.list.append(button1)



    def change(self):
        path = "C:\\Users\\{}\\AppData\\Local\\FortniteGame\\Saved\Config\\WindowsClient\\GameUserSettings.ini".format(getuser())
        res = self.resolution.get()
        u = 0
        for i in res:
            if i == "x":
                x = res[0:u]
                y = res[u+1:]
            u += 1
        lines = open(path).read().splitlines()
        lines[71]= "ResolutionSizeX={}".format(x)
        lines[72]="ResolutionSizeY={}".format(y)
        lines[73]="LastUserConfirmedResolutionSizeX={}".format(x)
        lines[74]="LastUserConfirmedResolutionSizeY={}".format(y)
        lines[82]="DesiredScreenWidth={}".format(x)
        lines[83]="DesiredScreenHeight={}".format(y)
        lines[84]="LastUserConfirmedDesiredScreenWidth={}".format(x)
        lines[85]="LastUserConfirmedDesiredScreenHeight={}".format(y)
        open(path, 'w').write('\n'.join(lines))
        self.done()
    def done(self):
        for i in self.list:
            i.destroy()
        label2 = Label(root,text="Done!",bg="#f54242",font=("helvetica",12))
        label2.place(x=210,y=50)
        root.update()
        sleep(2)
        root.destroy()
        



root = Tk()
root.geometry("500x150")
apps = app(root)
root.mainloop()


