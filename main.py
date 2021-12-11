'''
    Author: Usama Amjid
    Nickname: UsamaDarkweb
    Purpose: Learning or practice
    Date: December 11, 2021
    Youtube Channel: https://www.youtube.com/channel/UC6NrVQEqUXQq4tHdDrfMipw
    Facebook page: https://www.facebook.com/informationTechnology5256/
'''

from os import terminal_size
from random import choice, random
from tkinter import *
from tkinter import font
import tkinter.messagebox
import pyperclip

def g():
    '''
    this function generate random password 
    '''
    entry.delete(0,END) # this line remove or delete password text in the password feild when this function called
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
    password = ''
    l = pass_len.get() # get the password length
    if select.get() == 0: # mean by default
        for p in range(0, int(l)):
            password += choice(upper)
        return password
    elif select.get() == 1:
        for p in range(0,int(l)):
            password += choice(lower)
        return password
    elif select.get() == 3:
        for p in range(0, int(l)):
            password += choice(digits)
        return password


def generate():
    '''
    this function call the g function and display password when the generate button call
    '''
    password1 = g()
    entry.insert(0,password1) # this line display password in the password feild

def copy():
    '''
    this function will allow to copy the password when copy button call this function
    '''
    copy_password = entry.get()
    if copy_password:
        pyperclip.copy(copy_password)
        tkinter.messagebox.showinfo('Popup window','Copeid')





root = Tk()
pass_len = IntVar() # get the password length form the length input feild
select = IntVar() # get the choice password lower, meduim or strong
root.title("Password Generator by UsamaDarkweb")
root.geometry('550x65')
root.resizable(0,0)
root.iconbitmap('p.ico')
#start label password feild
label_password_generate = Label(root, text='Password',font='Times 17 bold')
label_password_generate.grid(row=0,column=0)
entry = Entry()
entry.grid(row=0,column=1)
# end 
#button generate
button1 = Button(root, text='Generate',font='Times 10 bold',padx=30,bg='sky blue',command=generate)
button1.grid(row=0,column=2)

#button copy
button2 = Button(root,text='Copy',font='Times 10 bold',width=6,padx=30,bg='sky blue',command=copy)
button2.grid(row=0,column=3)
# feild length password
label2 = Label(root, text='Length',font='Times 17 bold')
label2.grid(row=1,column=0)
entry_len = Entry(textvariable=pass_len)
entry_len.grid(row=1,column=1)

#make radio buttons
low = Radiobutton(root,text='Low',font='Times 15 bold',variable=select,value=1)
low.grid(row=1,column=2,sticky='E')
medium = Radiobutton(root,text='Medium',font='Times 15 bold',variable=select,value=0) # value 0 is given to make the default radio button
medium.grid(row=1,column=3,sticky='E')
strong = Radiobutton(root,text='Strong',font='Times 15 bold',variable=select,value=3)
strong.grid(row=1,column=4,sticky='E')



root.mainloop()