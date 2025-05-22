from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from file_manager import *
from validator import *

house_list = read_from_file("house.dat")


def load_data(house_list):
    house_list = read_from_file("house.dat")
    for row in table.get_children():
        table.delete(row)

    for house in house_list:
        table.insert("", END, values=(house .id , house .metrazh ,house.area , house.address, house.elvator ,house.parking))


def reset_form():
    id.set(len(house_list) + 1)
    metrazh.set(0)
    area.set(0)
    address.set(0)
    elvator.set(0)
    parking.set(0)
    load_data(house_list)


def save_btn_click():
    house= (id.get(), metrazh.get(), area.get(), address.get(), elvator() , parking())
    errors = house_validator(house)
    if errors:
        msg.showerror("Errors", "\n".join(errors))
    else:
        msg.showinfo("Saved", "house saved")
        house_list.append(house)
        write_to_file("houses.dat", house_list)
        reset_form()


def table_select(x):
    selected_house = table.item(table.focus())["values"]
    if selected_house:
        id.set(selected_house[0])
        metrazh.set(selected_house[1])
        area.set(selected_house[2])
        address.set(selected_house[3])
        elvator.set(selected_house[4])
        parking.set(selected_house[5])


def edit_btn_click():
    pass


def remove_btn_click():
    pass


window = Tk()
window.title("house Info")
window.geometry("8000x8000")

# Id
Label(window, text="Id").place(x=20, y=20)
id = IntVar(value=1)
Entry(window, textvariable=id, state="readonly").place(x=80, y=20)

# Metrazh
Label(window, text="Metrazh").place(x=20, y=60)
metrazh = IntVar()
Entry(window, textvariable=metrazh).place(x=80, y=60)

# area
Label(window, text="area").place(x=20, y=100)
area = IntVar()
Entry(window, textvariable=area).place(x=80, y=100)

# address
Label(window, text="address").place(x=20, y=140)
address = IntVar()
Entry(window, textvariable=address).place(x=80, y=140)

#elvator
Label(window, text="elvator").place(x=20, y=180)
elvator = IntVar()
Entry(window, textvariable=elvator).place(x=80, y=180)

#parking
Label(window, text="parking").place(x=20, y=220)
parking = IntVar()
Entry(window, textvariable=parking).place(x=80, y=220)

table = ttk.Treeview(window, columns=[1, 2, 3, 4 , 5, 6], show="headings")
table.heading(1, text="Id")
table.heading(2, text="Metrazh")
table.heading(3, text="area")
table.heading(4, text="address")
table.heading(5, text="elvator")
table.heading(6, text="parking")

table.column(1, width=60)
table.column(2, width=100)
table.column(3, width=100)
table.column(4, width=100)
table.column(5, width=100)
table.column(6, width=100)

table.bind("<<TreeviewSelect>>", table_select)

table.place(x=20, y=20)

Button(window, text="Save", width=6, command=save_btn_click).place(x=90, y=220)
Button(window, text="Edit", width=6, command=edit_btn_click).place(x=180, y=220)
Button(window, text="Remove", width=6, command=remove_btn_click).place(x=270, y=220)
Button(window, text="Clear", width=6, command=reset_form).place(x=360, y=180, width=300)

reset_form()

window.mainloop()