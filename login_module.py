import tkinter

root = tkinter.Tk()
lst=[]
def reg():
    dic={}
    
    dic['email']=inp1.get()
    dic['password']=inp2.get()
    a="Register..."
    lst.append(dic)
    print(lst)
    lab.config(text=a)

def log():
    
    for i in lst:
        if i['email']==inp1.get():
            a="Login Successfuly"
            lab.config(text=a)
            break
    else: 
        lab.config(text="Invalid Email And Password")
inp1 = tkinter.Entry()
inp2 = tkinter.Entry()
btn1 = tkinter.Button(text="Register",command=reg)
btn2 = tkinter.Button(text="Login",command=log)
lab = tkinter.Label()

inp1.grid(row=0,column=0,sticky='ew')
inp2.grid(row=1,column=0,sticky='ew')
btn1.grid(row=2,column=0,sticky='ew')
btn2.grid(row=3,column=0,sticky='ew')
lab.grid(row=4,column=0,sticky='ew')

root.geometry("400x400")
root.mainloop()