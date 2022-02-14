from tkinter import *

app = Tk()
app.geometry("500x500")
app.title("Shantanu Mane - Registration Form")


welcomeLbl = Label(
    app, text="Registration Form", width=20, font=("JetBrains Mono bold", 20)
)
welcomeLbl.place(x=90, y=60)

resetVar = StringVar(app)

def okMsg():
    endLbl = Label(
        app,
        text="Form Submitted",
        width=20,
        font=("JetBrains Mono bold", 14),
        fg="green",
    )
    endLbl.place(x=150, y=220)


nameLbl = Label(app, text="Full Name", width=20, font=("JetBrains Mono", 10))
nameLbl.place(x=80, y=130)


nameEnt = Entry(app)
nameEnt.place(x=240, y=130)

Button(app, text="Convert", width=20, bg="green", fg="white", command=okMsg).place(
    x=90, y=180
)
Button(app, text="Reset", width=20, bg="red", fg="white").place(
    x=240, y=180
)



app.mainloop()
