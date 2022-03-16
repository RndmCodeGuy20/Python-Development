from tkinter import *


app = Tk()
app.geometry("500x500")
app.title("Shantanu Mane - Currency Converter")


currDict = {
    "USD": 0.0132335,
    "Russ": 1.02349,
    "Yen": 1.5319,
    "CAD": 0.0169054,
}


welcomeLbl = Label(
    app, text="Currency Converter", width=20, font=("JetBrains Mono bold", 20)
)
welcomeLbl.place(x=90, y=60)


def convCurr():
    val = 0
    inpCurr = int(CurrEnt.get())

    USD = float(inpCurr * currDict["USD"])
    YEN = float(inpCurr * currDict["Yen"])
    RUS = float(inpCurr * currDict["Russ"])
    CAD = float(inpCurr * currDict["CAD"])

    USDOut.config(state="normal")
    USDOut.insert(0, USD)
    USDOut.config(state="disabled")
    RUSOut.config(state="normal")
    RUSOut.insert(0, RUS)
    RUSOut.config(state="disabled")
    YENOut.config(state="normal")
    YENOut.insert(0, YEN)
    YENOut.config(state="disabled")
    CADOut.config(state="normal")
    CADOut.insert(0, CAD)
    CADOut.config(state="disabled")


def resetBtn():
    var = IntVar(app)
    var.set(0)
    CurrEnt.config(textvariable=var)


var = IntVar(app)

CurrLbl = Label(app, text="Enter Currency", width=20, font=("JetBrains Mono", 10))
CurrLbl.place(x=80, y=130)


CurrEnt = Entry(app, textvariable=var)
CurrEnt.place(x=240, y=130)


Button(
    app,
    text="Convert",
    width=20,
    bg="green",
    fg="white",
    command=convCurr,
).place(x=90, y=180)

rstBtn = Button(app, text="Reset", width=20, bg="red", fg="white", command=resetBtn)
rstBtn.place(x=250, y=180)


USDLbl = Label(
    app,
    text="USD",
    width=20,
    font=("JetBrains Mono", 10),
)
USDLbl.place(x=80, y=230)


USDOut = Entry(
    app,
    state="disabled",
)
USDOut.place(x=240, y=230)


RUSLbl = Label(
    app,
    text="Russian Rubbles",
    width=20,
    font=("JetBrains Mono", 10),
)
RUSLbl.place(x=80, y=280)


RUSOut = Entry(
    app,
    state="disabled",
)
RUSOut.place(x=240, y=280)


YENLbl = Label(
    app,
    text="Japanese Yen",
    width=20,
    font=("JetBrains Mono", 10),
)
YENLbl.place(x=80, y=330)


YENOut = Entry(
    app,
    state="disabled",
)
YENOut.place(x=240, y=330)


CADLbl = Label(
    app,
    text="Canadian Dollars",
    width=20,
    font=("JetBrains Mono", 10),
)
CADLbl.place(x=80, y=380)


CADOut = Entry(
    app,
    state="disabled",
)
CADOut.place(x=240, y=380)


app.mainloop()
