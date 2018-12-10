from tkinter import *
lineCount = 1

archivedTasks = []

def AddRowForTask(window, text, name):
    frame = Frame(window, name=name)
    frame.pack()
    checkbox = Checkbutton(frame, name=name+"cbx", command=lambda: FinishTask(window, frame, text))
    checkbox.pack(side="left")
    label = Label(frame, text=text, height=2)
    label.config(font=("Comic Sans MS", 12))
    label.pack(side="left")
    editbtn = Button(frame, text="edytuj", name=name+"editbtn", command=lambda: EditTask(window,frame,label))
    editbtn.pack(side="left")
    deletebtn = Button(frame, text="usuń", name=name+"deletebtn", command=lambda: DeleteTask(window,frame))
    deletebtn.pack(side="left")


def FinishTask(window, frame, text):
    global archivedTasks
    archivedTasks.append(text)
    print(archivedTasks)
    frame.pack_forget()
    frame.destroy()
    window.update()


def PrepareTask(window, entry):
    global lineCount
    AddRowForTask(window, entry.get(), str(lineCount))
    lineCount += 1
    window.update()

def DeleteTask(window,frame):
    frame.pack_forget()
    frame.destroy()
    window.update()

def EditTask(window,frame,label):
    entry1 = Entry(frame)
    entry1.insert(END,label["text"])
    entry1.pack(side="left")
    window.update()
    finbtn = Button(frame, text="Akceptuj", command=lambda: EntryToLabel(label,entry1,window,finbtn))
    finbtn.pack(side="left")

def EntryToLabel(label, entry1, window, finbtn):
    label.config(text=entry1.get())
    entry1.pack_forget()
    finbtn.pack_forget()
    window.update()

def Run(window):
    window.update()