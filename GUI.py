from tkinter import *

window = Tk()
window.title("Niglo Bruteforce")
window.geometry("500x400")
img = PhotoImage(file='hedgehog-icon.png')
window.tk.call('wm', 'iconphoto', window._w, img)


window.mainloop()