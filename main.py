from task import *
from scrollable import *

window = Tk()
window.geometry("400x400+0+0")
window.resizable(False, False)
tasksFrame = Frame(window)
tasksFrame.pack()
scrollable_body = Scrollable(tasksFrame, width=20)

entry = Entry(window, text="")
entry.pack(side="bottom", fill="x")

addTaskBtn = Button(window, text="dodaj zadanie", command=lambda:PrepareTask(scrollable_body, entry))
addTaskBtn.pack(side="bottom", fill="x")

# scrollbar.config(command=)
# AddRowForTask(window, "1", "buton")
# AddRowForTask(window, "2", "inna nazwa")
window.mainloop()

