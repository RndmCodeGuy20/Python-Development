from tkinter import *

app = Tk()
app.geometry("500x700")
app.title("Shantanu Mane - Registration Form")


welcomeLbl = Label(
    app, text="Registration Form", width=20, font=("JetBrains Mono bold", 20)
)
welcomeLbl.place(x=90, y=60)

resetVar = StringVar(app)


def reset():
    resetVar.set("")
    passEnt.config()


def okMsg():
    endLbl = Label(
        app,
        text="Form Submitted",
        width=20,
        font=("JetBrains Mono bold", 14),
        fg="green",
    )
    endLbl.place(x=150, y=580)


nameLbl = Label(app, text="Full Name", width=20, font=("JetBrains Mono", 10))
nameLbl.place(x=80, y=130)


nameEnt = Entry(app)
nameEnt.place(x=240, y=130)


emailLbl = Label(app, text="E-mail", width=20, font=("JetBrains Mono", 10))
emailLbl.place(x=68, y=180)


emailEnt = Entry(app)
emailEnt.place(x=240, y=180)


addLbl = Label(app, text="Address", width=20, font=("JetBrains Mono", 10))
addLbl.place(x=68, y=230)


addEnt = Entry(app)
addEnt.place(x=240, y=230)


cityLbl = Label(app, text="City", width=20, font=("JetBrains Mono", 10))
cityLbl.place(x=68, y=280)


cityEnt = Entry(app)
cityEnt.place(x=240, y=280)


pinLbl = Label(app, text="Pin Code", width=20, font=("JetBrains Mono", 10))
pinLbl.place(x=68, y=330)

pinEnt = Entry(app)
pinEnt.place(x=240, y=330)

passLbl = Label(app, text="Password", width=20, font=("JetBrains Mono", 10))
passLbl.place(x=68, y=380)

passEnt = Entry(app, show="*")
passEnt.place(x=240, y=380)


contLbl = Label(app, text="Contact", width=20, font=("JetBrains Mono", 10))
contLbl.place(x=68, y=430)

contEnt = Entry(app)
contEnt.place(x=240, y=430)

countryLbl = Label(app, text="Country", width=20, font=("JetBrains Mono", 10))
countryLbl.place(x=70, y=480)

countryList = ["India", "USA", "UK", "Canada"]
selCountry = StringVar()
droplist = OptionMenu(app, selCountry, *countryList)
droplist.config(width=15)
selCountry.set("Select your Country")
droplist.place(x=235, y=480)


Button(app, text="Submit", width=20, bg="green", fg="white", command=okMsg).place(
    x=180, y=530
)
Button(app, text="Reset", width=20, bg="red", fg="white", command=reset).place(
    x=180, y=580
)

app.mainloop()
