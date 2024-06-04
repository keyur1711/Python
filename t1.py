import tkinter



root = tkinter.Tk()

def click():
    print("but clicked...!")
    root.config(background="red")
    print(inp.get())
    
btn = tkinter.Button(text="click" ,command=click)
inp = tkinter.Entry()

btn.grid(row=0,column=0)
inp.grid(row=1,column=0)
root.geometry("400x500")
root.mainloop()
#print(dir(tkinter))