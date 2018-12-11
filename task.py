from tkinter import *
lineCount = 1

archivedTasks = []

def AddRowForTask(window, text, name,save):
    frame = Frame(window, name=name)
    frame.pack()
    label = Label(frame, text=text, height=2)
    label.config(font=("Comic Sans MS", 12))
    checkbox = Checkbutton(frame, name=name+"cbx", command=lambda: FinishTask(window, frame, label))
    checkbox.pack(side="left")
    label.pack(side="left")
    deletebtn = Button(frame, text="usuń", name=name + "deletebtn", command=lambda: DeleteTask(window, frame))
    editbtn = Button(frame, text="edytuj", name=name+"editbtn", command=lambda: EditTask(window,frame,label,deletebtn,editbtn))
    editbtn.pack(side="left")
    deletebtn.pack(side="left")

def PrepareTask(window, entry):
    global lineCount
    save = open("save.txt", "ab+")
    AddRowForTask(window, entry.get(), str(lineCount),save)
    lineCount += 1
    window.update()


def FinishTask(window, frame, label):
    global archivedTasks
    archivedTasks.append(label["text"])
    print(archivedTasks)
    frame.pack_forget()
    frame.destroy()
    window.update()




def DeleteTask(window,frame):
    frame.pack_forget()
    frame.destroy()
    window.update()

def EditTask(window,frame,label,deletebtn,editbtn):
    entry1 = Entry(frame)
    entry1.insert(END,label["text"])
    deletebtn.pack_forget()
    editbtn.pack_forget()
    entry1.pack(side="left")
    label.pack_forget()
    window.update()
    finbtn = Button(frame, text="Akceptuj", command=lambda: EntryToLabel(label,entry1,window,finbtn,deletebtn,editbtn))
    finbtn.pack(side="left")

def EntryToLabel(label, entry1, window, finbtn,deletebtn,editbtn):
    label.config(text=entry1.get())
    label.pack(side="left")
    editbtn.pack(side="left")
    deletebtn.pack(side="left")
    entry1.pack_forget()
    finbtn.pack_forget()
    window.update()

def Run(window):
    window.update()