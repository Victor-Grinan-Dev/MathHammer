from tkinter import *
from old_scripts.math_hammer_func import MathHammer as func

window = Tk()
window.iconbitmap('Cuba-Flag.ico')
window.title("MathHammer 1.3")
# window.geometry("1185x220")
window.resizable(width=FALSE, height=FALSE)

button_x = 2
button_y = 1

# dummy variables
calc = func(10, 3, 7, 3, 1, 3, 4, in_cover=True)

armies = [{'name': "Vctor's Wolves", 'faction': ["marines"]}, "tau", 'tyranids', 'necrons']

attacker_list = ['marines', "tau", 'tyranids', 'necrons']
target_list = ['marines', "tau", 'tyranids', 'necrons']

marine_units = ['centurions', 'land raider', 'tacticals']

sm_armoury = ['bolter', 'heavy bolter', 'bolt carbine', 'plasma gun']

tau_units = ['fire warrior', 'riptide', 'drones']

tau_armoury = ['plasma rifle', 'fusion blaster', 'pulse rifle', ]

fire_warrior = {"M": 6, "Ws": 5, "Ws": 4, "S": 3, "T": 3, "A": 1, 'W': 1, "Ld": 6, "save": 4, 'invul': None,
                'fnp': None, "key words": 'infantry', "abilities": None,
                'equipment': {'name': 'pulse rifle', "range": 30, "type": 'rapid fire', "initial_attacks": 1, "S": 5, "AP": 0,
                              "D": 1, "Abilities": None}}

riptide = {"M": 14, "Ws": 5, "Ws": 4, "S": 6, "T": 7, "A": 3, 'W': 14, "Ld": 6, "save": 3, 'invul': 5, 'fnp': None,
           "key words": 'monstrous', "abilities": 'nova reactor',
           'equipment': {'name': 'heavy burst cannon', "range": 36, "type": 'heavy', "initial_attacks": 12, "S": 6, "AP": 1,
                         "D": 2, "Abilities": 'nova reactor'}}

shield_drones = {"M": 12, "Ws": 5, "Ws": 5, "S": 4, "T": 4, "A": 1, 'W': 1, "Ld": 6, "save": 4, 'invul': 4, 'fnp': 5,
                 "key words": '?', "abilities": 'savior protocol',
                 'equipment': None}
# real database

# ...

# calc from raw_data_text
probability = calc.stat_result
average_run = calc.average
best_run = calc.rand_max
worst_run = calc.rand_min
weapon_amount = calc.shots

columns_width = 200
columns_height = 250


# functions

def add_list():
    create_database_level = Toplevel()


# menu widgets
menu_frame = Frame(window)
menu_frame.grid(row=0, column=0)

add_list_button = Button(text='Add List')
add_list_button.grid(row=0, column=0)

# top widgets
top_frame = Frame(window)
top_frame.grid(row=1, column=0)

list_frame = LabelFrame(top_frame, text="Army List", padx=5, pady=5)
list_frame.pack(side="left", fill=Y)

list_sbar = Scrollbar(list_frame)
list_sbar.pack(side="right", fill="y")

list_canvas = Canvas(list_frame, height=columns_height, width=columns_width, yscrollcommand=list_sbar.set)
list_canvas.pack(fill=Y, expand=True)

units_frame = LabelFrame(top_frame, text="Units", padx=5, pady=5)
units_frame.pack(side="left", fill=Y)

units_sbar = Scrollbar(units_frame)
units_sbar.pack(side="right", fill="y")

units_canvas = Canvas(units_frame, height=columns_height, width=columns_width, yscrollcommand=units_sbar.set)
units_canvas.pack(fill=Y, expand=True)

weapons_frame = LabelFrame(top_frame, text="Weapons", padx=5, pady=5)
weapons_frame.pack(side="left", fill=Y)

weapons_sbar = Scrollbar(weapons_frame)
weapons_sbar.pack(side="right", fill="y")

weapons_canvas = Canvas(weapons_frame, height=columns_height, width=columns_width, yscrollcommand=weapons_sbar.set)
weapons_canvas.pack(fill=Y, expand=True)

target_frame = LabelFrame(top_frame, text="Target Unit", padx=5, pady=5)
target_frame.pack(side="left", fill=Y)

target_sbar = Scrollbar(target_frame)
target_sbar.pack(side="right", fill="y")

target_canvas = Canvas(target_frame, height=columns_height, width=columns_width, yscrollcommand=target_sbar.set)
target_canvas.pack(fill=Y, expand=True)

modifiers_frame = LabelFrame(top_frame, text="Modifiers", padx=5, pady=5)
modifiers_frame.pack(side="left", fill=Y)

modifiers_sbar = Scrollbar(modifiers_frame)
modifiers_sbar.pack(side="right", fill="y")

modifiers_canvas = Canvas(modifiers_frame, height=columns_height, width=columns_width,
                          yscrollcommand=modifiers_sbar.set)
modifiers_canvas.pack(fill=Y, expand=True)

# Bottom widgets
bottom_frame = Frame(window)
bottom_frame.grid(row=2, column=0)

main_canvas = Canvas(bottom_frame)
main_canvas.pack(side=LEFT, anchor=W)

center_header = Label(main_canvas, text="ShootingPhase Inflicted Wounds")
center_header.grid(row=0, column=0, columnspan=3)
center_label = Label(main_canvas, text=f"{probability:.1f}", font="Ariel 160")
center_label.grid(row=1, column=0, rowspan=2)

random_display = Label(main_canvas, text="1000x simulation roll results:", font="Ariel 12")
random_display.grid(row=0, column=3, columnspan=3)

best_label = Label(main_canvas, text="Best:", fg="green")
best_label.grid(row=1, column=3, sticky="N")
best_value = Label(main_canvas, text=f"{best_run}", font="Ariel 20", fg="green")
best_value.grid(row=2, column=3, sticky="N")

average_label = Label(main_canvas, text="average:")
average_label.grid(row=1, column=4)
average_value = Label(main_canvas, text=f"{average_run:.1f}", font="Ariel 20")
average_value.grid(row=2, column=4)

worst_label = Label(main_canvas, text="worst:", fg="red")
worst_label.grid(row=1, column=5, sticky="N", )
worst_value = Label(main_canvas, text=f"{worst_run}", font="Ariel 20", fg="red")
worst_value.grid(row=2, column=5, sticky="N")

image_canvas = Canvas(bottom_frame)
image_canvas.pack(side=RIGHT)

window.mainloop()
