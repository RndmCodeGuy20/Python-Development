import tkinter as tk

simpleApp = tk.Tk()

def showText():
    inpText = str(inpText.get())
    rezLbl.config(state="normal")
    rezLbl.delete("1.0", tk.END)
    rezLbl.insert(tk.END, age)
    rezLbl.config(state="disabled")


simpleApp.geometry("400x300")
simpleApp.config(bg = 'blue')

simpleApp.resizable(width=False, height=False)

simpleApp.title("Simple App")


simpleAppLabel = tk.Label(
    simpleApp,
    text= "Enter the text : ",
    bg = 'blue'
).place(x=70, y=5)

inpText = tk.Entry(simpleApp, width=10).place(x=200, y=5)

rezLabel = tk.Label(
    simpleApp, 
    text="Your input was : "
).place(x=200,y=50)

rezLabel = tk.Text(
    simpleApp,
    width=5,
    height=0,
    state="disabled",
)

simpleApp.mainloop()