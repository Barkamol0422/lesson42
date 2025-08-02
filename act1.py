from tkinter import *
window=Tk()
window.title("Event Handler")
window.geometry("100x100")

def e(event):
    print(event.char)
window.bind("<Key>", e)


button=Button(window,text="Click me")
button.pack()

def click_me(event):
    print("\n button is clicked")
button.bind("<Button-1>", click_me)
window.mainloop()
