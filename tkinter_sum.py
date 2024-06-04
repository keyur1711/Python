import tkinter
from tkinter import font  as tkfont
root = tkinter.Tk()

def click1():
    print("but clicked...!")
    
    print(int(inp1.get()) + int(inp2.get()))
def click2():
    print("but clicked...!")
    
    print(int(inp1.get()) - int(inp2.get()))
def click3():
    print("but clicked...!")
    
    print(int(inp1.get()) * int(inp2.get()))
def click4():
    print("but clicked...!")
    
    print(int(inp1.get()) / int(inp2.get()))
            

inp1 = tkinter.Entry()
inp2 = tkinter.Entry()

btn1 = tkinter.Button(text="+" ,command=click1)
btn2 = tkinter.Button(text="-" ,command=click2)
btn3 = tkinter.Button(text="*" ,command=click3)
btn4 = tkinter.Button(text="/" ,command=click4)


inp1.grid(row=0,column=0,sticky='ew')
inp2.grid(row=1,column=0,sticky='ew')

btn1.grid(row=2,column=0,sticky='ew')
btn2.grid(row=3,column=0,sticky='ew')
btn3.grid(row=4,column=0,sticky='ew')
btn4.grid(row=5,column=0,sticky='ew')

root.geometry("400x400")
root.mainloop()