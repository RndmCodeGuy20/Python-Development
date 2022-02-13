from datetime import date
import tkinter as tk


colors = ["#3874ef", "#cc5cd5", "#ff4c99", "#ff7055", "#ffa600"]
today = date.today()


def exit():
    ageApp.destroy()


def calcAge():
    inpM = int(entryM.get())
    inpY = int(entryY.get())
    age = today.year - inpY - (today.month < inpM)
    rezLbl.config(state="normal")
    rezLbl.delete("1.0", tk.END)
    rezLbl.insert(tk.END, age)
    rezLbl.config(state="disabled")


ageApp = tk.Tk()
ageApp.geometry("400x300")
ageApp.config(bg=colors[0])
ageApp.resizable(width=False, height=False)
ageApp.title("Shantanu Mane - Age Calculator")

welcomeLabel1 = tk.Label(
    ageApp,
    text="Age Calculator!",
    font=("JetBrains Mono Bold", 20),
    fg=colors[4],
    bg=colors[0],
)

welcomeLabel2 = tk.Label(
    ageApp,
    font=("JetBrains Mono Bold", 12),
    text="Enter your birth month and year : ",
    fg=colors[4],
    bg=colors[0],
)

month = tk.Label(
    ageApp,
    text="Month : ",
    font=("JetBrains Mono Bold", 12, "bold"),
    fg=colors[2],
    bg=colors[0],
)

year = tk.Label(
    ageApp,
    text="Year : ",
    font=("JetBrains Mono Bold", 12, "bold"),
    fg=colors[2],
    bg=colors[0],
)

entryM = tk.Entry(ageApp, width=5)
entryY = tk.Entry(ageApp, width=5)

calcBtn = tk.Button(
    ageApp,
    text="Calculate Age!",
    font=("JetBrains Mono", 13),
    fg=colors[4],
    bg=colors[3],
    command=calcAge,
)

rezLabel = tk.Label(
    ageApp,
    text="The Calculated Age is : ",
    font=("JetBrains Mono", 12, "bold"),
    fg=colors[4],
    bg=colors[0],
)

rezLbl = tk.Text(ageApp, width=5, height=0, state="disabled")
exitBtn = tk.Button(
    ageApp,
    text="Exit Application!",
    font=("JetBrains Mono", 13),
    fg=colors[4],
    bg=colors[3],
    command=exit,
)

welcomeLabel1.place(x=70, y=5)
welcomeLabel2.place(x=10, y=40)
month.place(x=100, y=95)
year.place(x=100, y=120)
entryM.place(x=180, y=95)
entryY.place(x=180, y=120)
calcBtn.place(x=100, y=150)
rezLabel.place(x=50, y=200)
rezLbl.place(x=240, y=203)
exitBtn.place(x=100, y=230)
ageApp.mainloop()
