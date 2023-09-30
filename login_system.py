import tkinter as tk
from tkinter import *
import random as r
import hashlib

root = tk.Tk()
root.geometry('400x400')
root.config(bg='#c15430')
root.title('Login Page')
root.iconbitmap(r"")

def change():
    global num
    a = list(range(0,10))
    b = r.sample(a,6)
    num=''.join(str(i) for i in b)
change()

num_label = tk.Label(root,text=(f'Your password: {num}'),bg='#c15430',border=10,width=20,font=('Comic Sans',13))
num_label.pack(pady=20)

def remove(event):
    user_entry.configure(state=NORMAL)
    user_entry.delete(0,END)
    user_entry.unbind('<Button-1>',clicked)

user_entry = tk.Entry(root,width=25,borderwidth=3)
user_entry.pack(pady=10)
user_entry.insert(0,'Enter OTP')

clicked = user_entry.bind('<Button-1>',remove)

def click():
    global s
    global f
    inp = str(user_entry.get())
    if inp != '':
        if inp==num:
            s = tk.Label(root,text='Logged in',fg='green',bg='white',font=('comic sans',9))
            s.pack()
        else:
            f=tk.Label(root,text='Wrong password',fg='red',bg='#c15430')
            f.pack(pady=10)
        user_entry.delete(0,END)


def again():
    global s
    global f
    change()
    num_label.config(text=(f'Your password: {num}'),bg='#c15430',border=10,width=20,font=('Comic Sans',13))
    inp = str(user_entry.get())
    if inp != '':
        if inp==num:
            tk.Label(root,text='Logged in',fg='green',bg='white',font=('comic sans',9)).pack()
        else:
            tk.Label(root,text='Wrong password',fg='red',bg='#c15430').pack(pady=10)
        user_entry.delete(0,END)
    s.destroy()
    f.destroy()

tk.Button(root,text="Verify",bg='white',fg='black',width=12,command=click).pack(pady=30)
tk.Button(root,text="Retry",bg='white',fg='black',width=12,command=again).pack()

root.mainloop()
