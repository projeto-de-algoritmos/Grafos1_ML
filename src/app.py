from tkinter import *
from PIL import ImageTk, Image

app = Tk()

app.title('Mapa Brasil')
app.geometry('500x500')
app.config(bg='#242323')

mapa = '../assets/mapaBR.jpg'

img_mapa = ImageTk.PhotoImage(Image.open(mapa))

label = Label(app, image=img_mapa)
label.pack()


app.mainloop()

