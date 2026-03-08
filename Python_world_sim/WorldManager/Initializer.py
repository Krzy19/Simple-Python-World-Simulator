from tkinter import Tk, Label, Entry, Button

class Initializer:
    def __init__(self):
        self.values = {}

    def submit(self):
        self.values['width'] = int(self.entry_width.get())
        self.values['height'] = int(self.entry_height.get())
        self.values['ileczlowiek'] = int(self.entry_ileczlowiek.get())
        self.values['ileowca'] = int(self.entry_ileowca.get())
        self.values['ilewilk'] = int(self.entry_ilewilk.get())
        self.values['ilelis'] = int(self.entry_ilelis.get())
        self.values['ileantylopa'] = int(self.entry_ileantylopa.get())
        self.values['ilezolw'] = int(self.entry_ilezolw.get())
        self.values['iletrawa'] = int(self.entry_iletrawa.get())
        self.values['ilemlecz'] = int(self.entry_ilemlecz.get())
        self.values['ilewilcze'] = int(self.entry_ilewilcze.get())
        self.values['ileguarana'] = int(self.entry_ileguarana.get())
        self.values['ilebarszcz'] = int(self.entry_ilebarszcz.get())
        self.values['ilecyberowca'] = int(self.entry_ilecyberowca.get())
        self.initwindow.quit()  # Exit the Tkinter main loop

    def get_initial_values(self):
        root = Tk()
        root.withdraw()

        self.initwindow = Tk()
        self.initwindow.title("Initial Values")

        Label(self.initwindow, text="Enter width:").grid(row=0, column=0)
        self.entry_width = Entry(self.initwindow)
        self.entry_width.insert(0,"20")
        self.entry_width.grid(row=0, column=1)

        Label(self.initwindow, text="Enter height:").grid(row=1, column=0)
        self.entry_height = Entry(self.initwindow)
        self.entry_height.insert(0, "20")
        self.entry_height.grid(row=1, column=1)

        Label(self.initwindow, text="Czy dodac gracza:").grid(row=2, column=0)
        self.entry_ileczlowiek = Entry(self.initwindow)
        self.entry_ileczlowiek.insert(0, "1")
        self.entry_ileczlowiek.grid(row=2, column=1)

        Label(self.initwindow, text="Ile owiec:").grid(row=3, column=0)
        self.entry_ileowca = Entry(self.initwindow)
        self.entry_ileowca.insert(0, "0")
        self.entry_ileowca.grid(row=3, column=1)

        Label(self.initwindow, text="Ile wilkow:").grid(row=4, column=0)
        self.entry_ilewilk = Entry(self.initwindow)
        self.entry_ilewilk.insert(0, "0")
        self.entry_ilewilk.grid(row=4, column=1)

        Label(self.initwindow, text="Ile lisow:").grid(row=5, column=0)
        self.entry_ilelis = Entry(self.initwindow)
        self.entry_ilelis.insert(0, "0")
        self.entry_ilelis.grid(row=5, column=1)

        Label(self.initwindow, text="Ile antylop:").grid(row=6, column=0)
        self.entry_ileantylopa = Entry(self.initwindow)
        self.entry_ileantylopa.insert(0, "0")
        self.entry_ileantylopa.grid(row=6, column=1)

        Label(self.initwindow, text="Ile zolwi:").grid(row=7, column=0)
        self.entry_ilezolw = Entry(self.initwindow)
        self.entry_ilezolw.insert(0, "0")
        self.entry_ilezolw.grid(row=7, column=1)

        Label(self.initwindow, text="Ile traw:").grid(row=8, column=0)
        self.entry_iletrawa = Entry(self.initwindow)
        self.entry_iletrawa.insert(0, "0")
        self.entry_iletrawa.grid(row=8, column=1)

        Label(self.initwindow, text="Ile mleczy:").grid(row=9, column=0)
        self.entry_ilemlecz = Entry(self.initwindow)
        self.entry_ilemlecz.insert(0, "0")
        self.entry_ilemlecz.grid(row=9, column=1)

        Label(self.initwindow, text="Ile wilczych jagod:").grid(row=10, column=0)
        self.entry_ilewilcze = Entry(self.initwindow)
        self.entry_ilewilcze.insert(0, "0")
        self.entry_ilewilcze.grid(row=10, column=1)

        Label(self.initwindow, text="Ile guaran:").grid(row=11, column=0)
        self.entry_ileguarana = Entry(self.initwindow)
        self.entry_ileguarana.insert(0, "0")
        self.entry_ileguarana.grid(row=11, column=1)

        Label(self.initwindow, text="Ile barszczow sosnowskiego:").grid(row=12, column=0)
        self.entry_ilebarszcz = Entry(self.initwindow)
        self.entry_ilebarszcz.insert(0, "0")
        self.entry_ilebarszcz.grid(row=12, column=1)

        Label(self.initwindow, text="Ile cyberowiec:").grid(row=13, column=0)
        self.entry_ilecyberowca = Entry(self.initwindow)
        self.entry_ilecyberowca.insert(0, "0")
        self.entry_ilecyberowca.grid(row=13, column=1)

        Button(self.initwindow, text="Submit", command=self.submit).grid(row=14, columnspan=2)

        self.initwindow.mainloop()  # Start the Tkinter main loop
        self.initwindow.destroy()   # Destroy the Tkinter window
        return self.values