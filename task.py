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
    editbtn = Button(frame, text="edytuj", name=name+"editbtn", command=lambda: EditTask(window,frame,label,deletebtn,editbtn,checkbox))
    editbtn.pack(side="left")
    deletebtn.pack(side="left")

def PrepareTask(window, entry):
    global lineCount
    save = open("save.txt", "ab+")
    AddRowForTask(window, entry.get(), str(lineCount),save)
    entry.delete(0,'end')
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

def EditTask(window,frame,label,deletebtn,editbtn,checkbox):
    entry1 = Entry(frame)
    entry1.insert(END,label["text"])
    editbtn.pack_forget()
    entry1.pack(side="left")
    label.pack_forget()
    window.update()
    checkbox.pack_forget()
    AcBtn = Button(frame,text="akceptuj ",command=lambda:  EntryToLabel(frame,label, entry1, window, deletebtn, editbtn,AcBtn,checkbox))
    AcBtn.pack()


def EntryToLabel(frame,label, entry1, window,deletebtn,editbtn,AcBtn,checkbox):
    AcBtn.pack_forget()
    deletebtn.pack_forget()
    window.update()
    if entry1.get() is "":
        DeleteTask(window,frame)
    else:
        checkbox.pack(side="left")
        label.config(text=entry1.get())
        label.pack(side="left")
        editbtn.pack(side="left")
        deletebtn.pack(side="left")
        entry1.pack_forget()
    window.update()

