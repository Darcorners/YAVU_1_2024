import tkinter
import tkinter as TK
from tkinter import messagebox
from Connect import connection
import pymysql


root = TK.Tk()
root.geometry("450x400")
root.resizable(width=False, height=False)
root.title("Актерское агенство")

Name = TK.Label(text="Имя:")
Name.pack()
Info1 = TK.Text(root, height = 1, width = 52)
Info1.pack()
SurName = TK.Label(text="Фамилия:")
SurName.pack()
Info2 = TK.Text(root, height = 1, width = 52)
Info2.pack()
Education = TK.Label(text="Образование:")
Education.pack()
Info3 = TK.Text(root, height = 1, width = 52)
Info3.pack()
Numbers = TK.Label(text="Кол-во ролей:")
Numbers.pack()
Info4 = TK.Text(root, height = 1, width = 52)
Info4.pack()

def DataInsert():
    try:
        with connection.cursor() as cursor:
            name = Info1.get("1.0", "end-1c")
            surname = Info2.get("1.0", "end-1c")
            education = Info3.get("1.0", "end-1c")
            numbers = Info4.get("1.0", "end-1c")
            InsertQuery = f"INSERT INTO `Actor`(`Name`, `Surname`, `Education`, `Number_of_roles`) VALUES ('{name}','{surname}','{education}','{numbers}') "
            cursor.execute(InsertQuery)
            connection.commit()
            messagebox.showinfo("Информация", "Данные успешно внесены в базу данных")
    except Exception as ex:
        print(ex)
        messagebox.showerror("Ошибка", "Ошибка в введённых данных")

Accept = TK.Button(text="Внести данные",command=DataInsert)
Accept.pack()
root.mainloop()