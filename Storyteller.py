from random import *
from tkinter import ttk
from tkinter import *


wann = ["Vor einigen Jahren gab es ","Als ich noch klein war gab es ", "Zu meiner Zeit gab es ", "Vor einigen Monaten gab es ", "Am 20. Januar gab es ","Damals gab es "]
wer = ["einen alten Mann namens ", "ein Kind namens ", "einen Fuchs namens ","einen Kater namens "]
name = ["Abdelmalek \n", "Alex ", "Jan ", "Björn ", "Dennis ", "Phillip ","Timo ","Simon ","Moritz ","Fabian ","Andreas ","Michel ","Ashmaz "]
ort = ["in Barcelona ", "in Saarland ", "in Paris ","in Bangladesch ","auf einer einsamen Insel ","in den Bergen ","auf dem Land ","in Sibirien "]
went = ["und er ging ins Kino ","und er ging zur Uni ", "und er ging zur Schule ","und er ging ins Cafe ","und er besuchte ein Museum " 
        "und er hatte eine Besprechung in Teams ","und er spielte Fußball", "und er programmierte sehr gerne"]
geschehen = ["wo er auch neue Freunde gefunden hat :).","während er einen Burger aß...WAHNSINN!", "dann fand er plötzlich einen geheimen Schlüssel..."," worüber er auch ein Buch schrieb, es wurde ein Bestseller!!!."]


def tell():
    x = (choice(wann)+choice(wer)+choice(name)+choice(ort)+choice(went)+','+choice(geschehen))
    print(x)
    box.delete(1.0,"end")
    box.insert(1.0,x)

#Erstellen eines Hauptfensters
frmMain = Tk()
frmMain.wm_geometry("500x350")
frmMain.title("Storyteller")

#Hintergrund
canvas = Canvas(width = 500, height = 500, bg = 'white')
canvas.pack(expand = YES, fill = BOTH)
gif1 = PhotoImage(file = 'C:\\Users\\TN-35011\\VSP\\starfall-gif-46.gif')
canvas.create_image(0, 0, image = gif1, anchor = NW)


#Button erstellen
tellme = ttk.Button(frmMain, text="Tell me",command=tell)
tellme.place(x=210, y=40)


#Textbox erstellen
box = Text(frmMain, height=10, width=50, background="#0c1438",fg="white", borderwidth=0)
box.place(x=55, y=80)

#Endlosschleife
mainloop()
