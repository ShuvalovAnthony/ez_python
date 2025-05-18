from tkinter import *
from tkinter import ttk

root = Tk()
root.attributes("-topmost", True)
root.geometry("1024x768")
frame = ttk.Frame(root, padding=10)
frame.pack(expand=True, fill="both")  # Растягиваем на все окно

HEADERS_LABELS = ["Add task", 'To do', 'In progress', 'Completed']

class Task:
    toDo = {}
    inProgress = {}
    completed = {}
    labels = []
    id_counter = 1

    def __init__(self, task: str, status: str, frame):
        self.task = task
        self.status = status
        self.frame = frame
        self.id_ = Task.id_counter
        Task.id_counter += 1
        Task.toDo[self.id_] = self

        print("New task added", task, "with id", self.id_)

        self.refreshFrame()

    
    def refreshFrame(self):
        for label in Task.labels:
            label.destroy()
        Task.labels.clear()
        self.refreshTodo()
        self.refreshCompleted()
        self.refreshInprogress()


    def refreshTodo(self):
        self.drawBtns(Task.toDo, 2)


    def refreshInprogress(self):
        self.drawBtns(Task.inProgress, 3)


    def refreshCompleted(self):
        self.drawBtns(Task.completed, 4, False)

    
    def drawBtns(self, btnsPack: dict, col_: int, isEnabled: bool=True):
        row_ = 2
        for id_, task in btnsPack.items():
            tempTaskBtn = ttk.Button(self.frame, text=task.task, command=task.changeStatus)
            tempTaskBtn.grid(row=row_, column=col_, sticky="nsew")
            if not isEnabled: tempTaskBtn.state(["disabled"])
            Task.labels.append(tempTaskBtn)
            row_ += 1

    
    def changeStatus(self):
        if self.status == "t":
            self.status = 'i'
            Task.inProgress[self.id_] = Task.toDo.pop(self.id_)
        elif self.status == "i":
            self.status = 'c'
            Task.completed[self.id_] = Task.inProgress.pop(self.id_)
        elif self.status == "c":
            ...

        self.refreshFrame()


def createTask():
    newTask = Task(taskTextBox.get(), "t", frame)
    taskTextBox.delete(0, END)


def changeAddTaskBtnStatus(*args):
    if task_text.get().strip():
        addTaskButton.state(["!disabled"])
    else:
        addTaskButton.state(["disabled"])


task_text = StringVar()



for i in range(1, 5):
    frame.grid_columnconfigure(i, weight=1, minsize=256, pad=10)

for col_ in range(1, 5):
    initialLabel = ttk.Label(frame, text=HEADERS_LABELS[col_ - 1])
    initialLabel.grid(row=1, column=col_, sticky="nsew")

taskTextBox = ttk.Entry(frame, textvariable=task_text)
taskTextBox.grid(row=2, column=1, sticky="nsew")

addTaskButton = ttk.Button(frame, text="Добавить", command=createTask)
addTaskButton.state(["disabled"])
addTaskButton.grid(row=3, column=1, sticky="nsew")


task_text.trace_add("write", changeAddTaskBtnStatus)

root.mainloop()