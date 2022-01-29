from tkinter import *
import csv
import os

root = Tk()

root.iconbitmap('Cuba-Flag.ico')
root.title("MathHammer 1.3")

NUMER_ENTRY_WIDTH = 3
ALFAB_ENTRY_WIDTH = 15

back_button = Button(root, text='Back')
back_button.pack()

author_label = Label(root, text='Author')
author_label.pack()
author_entry = Entry(root, width=ALFAB_ENTRY_WIDTH)

author_entry.pack()
author_entry.insert(0, "UNKNOWN", )  # TASK get the user name from the log-inas author
author_entry.configure(takefocus=True)  # TASK indicate that the user can use the Tab key to move to this widget.

list_name_label = Label(root, text='List name')
list_name_label.pack()
list_name_entry = Entry(root, width=ALFAB_ENTRY_WIDTH)
list_name_entry.pack()
list_name_entry.insert(0, "NEW LIST", )
list_name_entry.configure(takefocus=True)

faction_label = Label(root, text='Faction')
faction_label.pack()
faction_entry = Entry(root, width=ALFAB_ENTRY_WIDTH)
faction_entry.pack()
faction_entry.insert(0, "UNDEFINED")
faction_entry.configure(takefocus=True)

# dummy raw_data_text base
argumentsPerModelList = ['M', 'Ws', 'Ws', 'other_equipments']


def create_txt_file():
    name = list_name_entry.get()
    faction = faction_entry.get()
    author = author_entry.get()

    # TASK make a 'safe saving' os system for this documents if doesnt exist or replace doc question

    with open(f"{author}'s {name} ({faction}).txt", 'w') as f:
        f.write('list name:' + name + '\n')
        f.write('faction:' + faction + '\n')
        f.write('author:' + author + '\n')


def read_txt_file(file):
    with open(file, 'r') as f:
        f_contents = f.read()
        for line in f_contents:
            print(line, end='')


def create_csv_file(file):
    pass


def read_csv_file(file):
    pass


def modify_csv_file(file):
    pass


def del_csV_file(file):
    pass


def close():
    pass


unit_composition_list = []


def new_unit():
    top_page = Toplevel()

    top_page.iconbitmap('Cuba-Flag.ico')
    top_page.title("MathHammer 1.3")

    unit_name_label = Label(top_page, text='unit_name')
    unit_name_label.grid(row=0, column=0)

    unit_name_entry = Entry(top_page, width=ALFAB_ENTRY_WIDTH)
    unit_name_entry.grid(row=0, column=1)

    unit_fieldroll_label = Label(top_page, text='unit_fieldroll')
    unit_fieldroll_label.grid(row=1, column=0)

    unit_fieldroll_entry = Entry(top_page, width=ALFAB_ENTRY_WIDTH)
    unit_fieldroll_entry.grid(row=1, column=1)

    unit_composition_label = Label(top_page, text='unit_composition')
    unit_composition_label.grid(row=2, column=0)

    unit_composition_entry = Entry(top_page, width=ALFAB_ENTRY_WIDTH)
    unit_composition_entry.grid(row=2, column=1)
    unit_composition_entry.insert(0, 'Sgt')
    unit_composition_label1 = Label(top_page, text='+')
    unit_composition_label1.grid(row=2, column=2)
    unit_composition_entry1 = Entry(top_page, width=NUMER_ENTRY_WIDTH)
    unit_composition_entry1.grid(row=2, column=3)
    unit_composition_entry1.insert(0, 4)
    unit_composition_entry2 = Entry(top_page, width=ALFAB_ENTRY_WIDTH)
    unit_composition_label2 = Label(top_page, text='x')
    unit_composition_label2.grid(row=2, column=4)
    unit_composition_entry2.grid(row=2, column=5)
    unit_composition_entry2.insert(0, 'marine')

    unit_composition_number = int(unit_composition_entry1.get()) + 1
    print('unit_composition_number', unit_composition_number)

    unit_composition_members = []
    for _ in range(int(unit_composition_entry1.get())):
        unit_composition_members.append(unit_composition_entry2.get())

    print('unit_composition_members', unit_composition_members)

    unit_composition_list = [unit_composition_entry.get()] + unit_composition_members

    print('unit_composition_list', unit_composition_list)

    unit_equipment_label = Label(top_page, text='unit_equipment')
    unit_equipment_label.grid(row=3, column=0)

    unit_equipment_entry = Entry(top_page)
    unit_equipment_entry.grid(row=3, column=1)

    unit_arguments_label = Label(top_page, text='Models/arguments')
    unit_arguments_label.grid(row=4, column=0)

    global column_num
    global row_num

    column_num = 1
    row_num = 5

    def creae_table():

        column_num = 1

        for argument in argumentsPerModelList:  # CREATES THE ARGUMENTS LINE ON TOP

            if argument is not argumentsPerModelList[-1]:
                unit_arguments_label = Label(top_page, text=f'{argument}')
                unit_arguments_label.grid(row=4, column=column_num)

                column_num += 1

            else:
                unit_arguments_label = Label(top_page, text=f'{argument}')
                unit_arguments_label.grid(row=4, column=column_num)

        row_num = 5

        for model in unit_composition_list:  # TABLE

            column_num = 0

            model_name_label = Label(top_page, text=f'{model}')
            model_name_label.grid(row=row_num, column=column_num)

            column_num += 1

            for argument in argumentsPerModelList:
                if len(argument) <= 4:
                    unit_arguments_entry = Entry(top_page, width=NUMER_ENTRY_WIDTH)
                    unit_arguments_entry.grid(row=row_num, column=column_num)
                else:
                    unit_arguments_entry = Entry(top_page, width=ALFAB_ENTRY_WIDTH)
                    unit_arguments_entry.grid(row=row_num, column=column_num)

                if argument is not argumentsPerModelList[-1]:  # trying to fix desnivel, not working
                    column_num += 1

            row_num += 1

    creae_table()

    def add_unit():
        unit_name_entry.get()
        unit_fieldroll_entry.get()
        unit_composition_entry.get()
        unit_equipment_entry.get()

    add_to_list_button = Button(top_page, text='add to the list', command=add_unit)
    add_to_list_button.grid(row=100, column=0)

    update_arg_button = Button(top_page, text='update', command=creae_table)
    update_arg_button.grid(row=4, column=column_num + 1)

add_unit_button = Button(root, text='Continue', command=new_unit)
add_unit_button.pack(side=LEFT, anchor='sw')

back_button.config(command=close)
back_button.focus_set()

create_list_button = Button(root, text='Create', command=create_txt_file)
create_list_button.pack()
root.mainloop()
