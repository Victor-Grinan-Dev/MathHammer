from tkinter import *
from tkinter import ttk
from old_scripts.math_hammer_func import MathHammer as func

# from math_hammer_DB import armies

window = Tk()
# window.iconbitmap(r'C:\Users\victo\Downloads\Cuba-Flag.ico')
window.title("MathHammer 1.2")
# window.geometry("1185x220")
window.resizable(width=FALSE, height=FALSE)

# dimensions of button
button_x = 2
button_y = 1

# dummy variables
try1 = func(10, 3, 7, 3, 1, 3, 4, in_cover=True)

armies = ['marines', "tau", 'tyranids', 'necrons']

attacker_list = ['marines', "tau", 'tyranids', 'necrons']
target_list = ['marines', "tau", 'tyranids', 'necrons']

marine_units = ['centurions', 'land raider', 'tacticals']
tau_units = ['cara de pescao', 'cara de pescao grande', 'drones']

sm_armoury = ['bolter', 'heavy bolter', 'bolt carbine', 'plasma gun']
tau_armoury = ['plasma rifle', 'fusion blaster', 'pulse rifle', ]
# real database

# ...

probability = try1.stat_result
average_run = try1.average
best_run = try1.rand_max
worst_run = try1.rand_min
weapon_amount = try1.shots

attacker = StringVar()
attacker.set(None)
defender = StringVar()
defender.set(None)

global weapon


def add_shot(current_w, amount):
    print(current_w, amount)


def sub_shot(current_w, amount):
    print(current_w, amount)


def show_units(army):
    pass


attacking_frame = LabelFrame(window, text="Attacking Army", padx=5, pady=5)
army_sbar = Scrollbar(attacking_frame)
army_canvas = Canvas(attacking_frame, height=220, yscrollcommand=army_sbar.set)
army_scrollable_frame = ttk.Frame(army_canvas)

army_scrollable_frame.bind("<Configure>", lambda e: army_canvas.configure(scrollregion=army_canvas.bbox("all")))

army_list_row = 1


class MathHammerWidges:

    def __init__(self):
        self.attacking_frame = LabelFrame(window, text="Attacking Army", padx=5, pady=5)
        self.attacking_frame.pack(side="left", fill=Y)

        self.army_sbar = Scrollbar(attacking_frame)
        self.army_sbar.pack(side="right", fill="y")

        self.army_canvas = Canvas(attacking_frame, height=220, yscrollcommand=army_sbar.set)
        self.army_canvas.pack(fill=Y, expand=True)

        self.army_scrollable_frame = ttk.Frame(army_canvas)

        self.army_scrollable_frame.bind("<Configure>", lambda e: self.army_canvas.configure(
            scrollregion=self.army_canvas.bbox("all")))

        self.army_list_row = 1
        self.line_value = 0

        for army in armies:
            # eval(f"rb{name}=")

            rb = Radiobutton(army_canvas, text=f'{army}', variable=attacker, value=f'{army}', command=show_units(army))

            # variable=r, value=1, command=lambda: update_label(r.get())).pack()

            rb.grid(row=self.army_list_row, column=0, sticky="w")

            self.army_list_row += 1

        self.army_sbar.config(command=army_canvas.yview)

        self.armory_frame = LabelFrame(window, text="Armory", padx=5, pady=5)
        self.armory_frame.pack(side="left", fill=Y)  # .grid(row=0, column=1, padx=5, pady=5, sticky="n")

        self.armoury_sbar = Scrollbar(self.armory_frame)
        self.armoury_sbar.pack(side="right", fill=Y)

        self.armoury_canvas = Canvas(self.armory_frame, height=220)
        self.armoury_canvas.config(yscrollcommand=self.armoury_sbar.set)
        self.armoury_canvas.pack(fill=Y)

        self.armoury_sbar.config(command=self.armoury_canvas.yview)

    def show_army(self, army):

        armoury_row = 1

        for weapon_ in sm_armoury:  # armoury[name.get()]

            cb = Checkbutton(self.armoury_canvas,
                             text=f"{weapon_}")  # variable=var, onvalue="On", offvalue="off", command=show)
            cb.grid(row=armoury_row, sticky="nw")

            weapon_sub_button = Button(self.armoury_canvas, text="-", width=button_x, state=DISABLED)
            weapon_sub_button.config(command=lambda: sub_shot(f"{weapon_}", 1))
            weapon_sub_button.grid(row=armoury_row, column=1, sticky="wN")

            weapon_amount_label = Label(self.armoury_canvas, text=f'{weapon_amount:02d}', state=DISABLED)
            weapon_amount_label.grid(row=armoury_row, column=2, sticky="w")

            weapon_add_button = Button(self.armoury_canvas, text="+", width=button_x, state=DISABLED,
                                       command=lambda: add_shot(f"{weapon_}", 1))
            weapon_add_button.grid(row=armoury_row, column=3, sticky="wN")

            weapon_sub10_button = Button(self.armoury_canvas, text="-10", width=button_x, state=DISABLED,
                                         command=lambda: sub_shot(f"{weapon_}", 10))
            weapon_sub10_button.grid(row=armoury_row, column=4, padx=5, sticky="wN")

            weapon_add10_button = Button(self.armoury_canvas, text="+10", width=button_x, state=DISABLED,
                                         command=lambda: add_shot(f"{weapon_}", 10))
            weapon_add10_button.grid(row=armoury_row, column=5, sticky="wN")

            armoury_row += 1

    main_frame = LabelFrame(window, text="Main", padx=5, pady=5)
    main_frame.pack(side="left", fill=Y)  # .grid(row=0, column=2, padx=5, pady=5, sticky="n")

    main_canvas = Canvas(main_frame)
    main_canvas.pack(fill=Y)

    center_header = Label(main_canvas, text="ShootingPhase Inflicted Wounds")
    center_header.grid(row=0, columnspan=3)
    center_label = Label(main_canvas, text=f"{probability:.1f}", font="Ariel 48")
    center_label.grid(row=1, columnspan=3)

    random_display = Label(main_canvas, text="1000x simulation roll results:", font="Ariel 12")
    random_display.grid(row=2, columnspan=3)

    best_label = Label(main_canvas, text="best:", fg="green")
    best_label.grid(row=3, column=0, sticky="N")
    best_value = Label(main_canvas, text=f"{best_run}", font="Ariel 20", fg="green")
    best_value.grid(row=4, column=0, sticky="N")

    average_label = Label(main_canvas, text="average:")
    average_label.grid(row=3, column=1)
    average_value = Label(main_canvas, text=f"{average_run:.1f}", font="Ariel 20")
    average_value.grid(row=4, column=1)

    worst_label = Label(main_canvas, text="worst:", fg="red")
    worst_label.grid(row=3, column=2, sticky="N", )
    worst_value = Label(main_canvas, text=f"{worst_run}", font="Ariel 20", fg="red")
    worst_value.grid(row=4, column=2, sticky="N")

    target_frame = LabelFrame(window, text="Target Unit", padx=5, pady=5)
    target_frame.pack(side="left", fill=Y)  # .grid(row=0, column=3, padx=5, pady=5, sticky="n")

    target_sbar = Scrollbar(target_frame)
    target_sbar.pack(side="right", fill=Y)

    target_canvas = Canvas(target_frame, yscrollcommand=target_sbar.set)
    target_canvas.pack(side="left", fill=Y)

    target_sbar.config(command=target_canvas.yview)

    target_row = 1

    for target in target_list:
        tb = Radiobutton(target_canvas, text=f"{target}")
        tb.grid(row=target_row, sticky="w")
        target_row += 1

    defending_frame = LabelFrame(window, text="Defending Army", padx=5, pady=5)
    defending_frame.pack(side="left", fill=Y)  # .grid(row=0, column=4, padx=5, pady=5, sticky="n")

    defending_sbar = Scrollbar(defending_frame)
    defending_sbar.pack(side="right", fill=Y)

    defending_canvas = Canvas(defending_frame, yscrollcommand=defending_sbar.set)
    defending_canvas.pack(side=LEFT, fill=Y)

    defending_sbar.config(command=defending_canvas.yview)

    defending_row = 1

    for army in armies:
        drb = Radiobutton(defending_canvas, text=f'{army}', variable=defender, value=f'{army}')
        drb.deselect()
        # variable=r, value=1, command=lambda: update_label( r.get())).pack()
        drb.grid(row=defending_row, sticky="w")
        defending_row += 1


window.mainloop()
