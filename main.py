import tkinter as TK
from tkinter import ttk
from tkinter import messagebox
from Connect import connection

root = TK.Tk()
root.geometry("450x400")
root.resizable(width=False, height=False)
root.title("Актерское агенство")

Name = TK.Label(text="Имя:")
Name.pack()

list = []

def create_data():
    with connection.cursor() as cursor:
        cursor.execute(""" SELECT `Name`, `Surname` FROM `Actor` WHERE 1 """)
        result = cursor.fetchall()
        for i in result:
            checkbox_var = TK.IntVar()
            name_surname = f"{i['Name']} {i['Surname']}"
            checkbox = ttk.Checkbutton(text=name_surname, variable=checkbox_var, command=lambda var=checkbox_var, name=name_surname: checking(var, name))
            checkbox.pack()

def checking(var, name):
    if var.get() == 1:
        list.append(name)
    else:
        list.remove(name)

    print(list)
    with connection.cursor() as cursor:
        for name in list:
            cursor.execute(f""" INSERT INTO `Vote`(`Name_Surname`, `Votes`) VALUES ('{name}', 1) """)
            connection.commit()
create_data()

Accept = TK.Button(text="Внести данные")
Accept.pack()
root.mainloop()