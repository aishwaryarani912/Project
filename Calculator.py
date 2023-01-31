from tkinter import *
import tkinter.messagebox
class cal_1():
    def __init__(self):
        cal.geometry("500x500")
        title=Label(cal,text="Calculator",font="bold",pady=10)
        title.pack()
        frame=Frame(cal,bg="black")
        frame.pack()
        entry=Entry(frame,font=("cambria",20,"bold"),borderwidth=20,relief="groove",highlightbackground="black")
        entry.grid(row=0,column=0,columnspan=50,padx=5,pady=5)
    
        def bt_click(number):
            entry.insert(END,number)
        
        def bt_equal():
            try:
                x=str(eval(entry.get()))
                entry.delete(0,END)
                entry.insert(0,x)
            except:
                tkinter.messagebox.showinfo("Error","syntaxerror")
        def btn_clear():
            entry.delete(0,END)
        
        clear = Button(frame, text = "C",fg = "blue",width = 10, height = 3,command =btn_clear,borderwidth=5,relief="groove").grid(row = 1, column = 0, padx = 1, pady = 1)
        leftbracket = Button(frame, text = "(",fg = "blue",width = 10, height = 3,command = lambda: bt_click(("(")),borderwidth=5,relief="groove").grid(row = 1, column = 1, padx = 1, pady = 1)
        rightbracket = Button(frame, text = ")",fg = "blue", width = 10, height = 3,command = lambda: bt_click(")"),borderwidth=5,relief="groove").grid(row = 1, column = 2, padx = 1, pady = 1)
        divide = Button(frame, text = "/",fg = "blue", width = 10, height = 3,command = lambda: bt_click("/"),borderwidth=5,relief="groove").grid(row = 1, column = 3, padx = 1, pady = 1)

        seven = Button(frame, text = "7",fg = "blue",width = 10, height = 3, command = lambda: bt_click(7),borderwidth=5,relief="groove").grid(row = 2, column = 0, padx = 1, pady = 1)
        eight = Button(frame, text = "8",fg = "blue",width = 10, height = 3, command = lambda: bt_click(8),borderwidth=5,relief="groove").grid(row = 2, column = 1, padx = 1, pady = 1)
        nine = Button(frame, text = "9",fg = "blue", width = 10, height = 3, command = lambda: bt_click(9),borderwidth=5,relief="groove").grid(row = 2, column = 2, padx = 1, pady = 1)
        multiply = Button(frame, text = "*",fg = "blue",width = 10, height = 3,command = lambda: bt_click("*"),borderwidth=5,relief="groove").grid(row = 2, column = 3, padx = 1, pady = 1)

        four = Button(frame, text = "4", fg = "blue",width = 10, height = 3, command = lambda: bt_click(4),borderwidth=5,relief="groove").grid(row = 3, column = 0, padx = 1, pady = 1)
        five = Button(frame, text = "5", fg = "blue",width = 10, height = 3, command = lambda: bt_click(5),borderwidth=5,relief="groove").grid(row = 3, column = 1, padx = 1, pady = 1)
        six = Button(frame, text = "6", fg = "blue",width = 10, height = 3, command = lambda: bt_click(6),borderwidth=5,relief="groove").grid(row = 3, column = 2, padx = 1, pady = 1)
        minus = Button(frame, text = "-", fg = "blue",width = 10, height = 3, command = lambda: bt_click("-"),borderwidth=5,relief="groove").grid(row = 3, column = 3, padx = 1, pady = 1)

        one = Button(frame, text = "1", fg = "blue",width = 10, height = 3,command = lambda: bt_click(1),borderwidth=5,relief="groove").grid(row = 4, column = 0, padx = 1, pady = 1)
        two = Button(frame, text = "2", fg = "blue", width = 10, height = 3,command = lambda: bt_click(2),borderwidth=5,relief="groove").grid(row = 4, column = 1, padx = 1, pady = 1)
        three = Button(frame, text = "3", fg = "blue",width = 10, height = 3, command = lambda: bt_click(3),borderwidth=5,relief="groove").grid(row = 4, column = 2, padx = 1, pady = 1)
        plus = Button(frame, text = "+", fg = "blue", width = 10, height = 3,command = lambda: bt_click("+"),borderwidth=5,relief="groove").grid(row = 4, column = 3, padx = 1, pady = 1)

        modulus = Button(frame, text = "%", fg = "blue",width = 10, height = 3,command = lambda: bt_click("%"),borderwidth=5,relief="groove").grid(row = 5, column = 0, padx = 1, pady = 1) 
        zero = Button(frame, text = "0", fg = "blue",width = 10, height = 3,command = lambda: bt_click(0),borderwidth=5,relief="groove").grid(row = 5, column = 1, padx = 1, pady = 1)
        point = Button(frame, text = ".", fg = "blue",width = 10, height = 3, command = lambda: bt_click("."),borderwidth=5,relief="groove").grid(row = 5, column = 2, padx = 1, pady = 1)
        equals = Button(frame, text = "=", fg = "blue",width = 10, height = 3, command =bt_equal,borderwidth=5,relief="groove").grid(row = 5, column =3, padx = 1, pady = 1)


cal=Tk()
obj=cal_1()
cal.mainloop()
