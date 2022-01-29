from tkinter import *
from tkinter import ttk

# from math_hammer.version_storage import math_hammer_functions_00 as my_func

# CREATE OBJECT
window = Tk()

# window size
x = 525
y = 400
window.geometry(f'{x}x{y}')

# title
window.title('Math-Hammer 1.1')

# img_icon
window.iconbitmap(r'C:\Users\victo\Downloads\Cuba-Flag.ico')

# fixed size
# window.resizable(width=FALSE, height=FALSE)

# CREATING TABS

# ATTACKER PART
attacker_page = ttk.Notebook(window)
attacker_page.grid(row=0, column=0, sticky='W')
# marines tab_
marines_a = ttk.Frame(attacker_page)
attacker_page.add(marines_a, text='Marines')
# tau tab_
tau_a = ttk.Frame(attacker_page)
attacker_page.add(tau_a, text='Tau')
# tiranids tab_
tyranids = ttk.Frame(attacker_page)
attacker_page.add(tyranids, text='Tyranids')

center_page = ttk.Notebook(window)
center_page.grid(row=0, column=1, sticky='NESW')
main_frame = ttk.Frame(center_page)
center_page.add(main_frame, text="main page")

# DEFENDER PART
defender = ttk.Notebook(window)
defender.grid(row=0, column=2, sticky='E')

marines_d = ttk.Frame(window)
defender.add(marines_d, text='Marines')

tau_d = ttk.Frame(window)
defender.add(tau_d, text='Tau')

tyranids_d = ttk.Frame(window)
defender.add(tyranids_d, text='Tyranids')

# background image
# bg_path = r"C:\Users\victo\PycharmProjects\math_hammer\math-hammer.png"
# background_image = PhotoImage(file=bg_path)
# background_label = Label(main_frame, image=background_image)
# background_label.place(x=0, y=0, relwidth=1, relheight=1)

# database
# TEMP DATABASE :)
marines_armory = ['bolter', 'plasma', 'melta', 'flamer', 'grav_cannon' 'plasma_cannon']
marines_units = ['tactical', "intercessor", "centurions", "predator", "landraider"]

tau_armory = ['plasma rifle', 'pulse rifle', 'fusion blaster', 'missile pod',
              'smart missiles', 'burst cannon', 'Heavy burst cannon']
tau_units = ["fire warriors", "riptide", "broadside"]

tyranid_armory = ['deathspiters', 'bio plasma', 'bioplasma cannon', 'spinefist']
tyranids_units = ["termagaunts", "genestealers", "carnifex"]

# declare type of varible

button_x = 2
button_y = 1

probability = 0
test_run = 0

target = StringVar()
target.set("tactical")  # whats the initial value

shooting_weapon = StringVar()
# variables marines all_equipments:['bolter', 'plasma', 'melta', 'flamer', 'grav cannon' 'lasscannon']
bolter_shooting = StringVar()
plasma_shooting = StringVar()
melta_shooting = StringVar()
flamer_shooting = StringVar()
grav_cannon_shooting = StringVar()
lasscannon_shooting = StringVar()

bolter_amount = 0
plasma_amount = 0
melta_amount = 0
flamer_amount = 0
grav_cannon_amount = 0
lasscannon_amount = 0

# variable tau all_equipments: plasma rifle', 'pulse rifle', 'fusion blaster', 'missile pod','smart missiles', 'Heavy burst
# cannon'
plasma_rifle_shooting = StringVar()
pulse_rifle_shooting = StringVar()
fusion_blaster_shooting = StringVar()
missile_pod_shooting = StringVar()
smart_missiles_shooting = StringVar()
heavy_burst_cannon_shooting = StringVar()

plasma_rifle_amount = 0
pulse_rifle_amount = 0
fusion_blaster_amount = 0
missile_pod_amount = 0
smart_missiles_amount = 0
heavy_burst_cannon_amount = 0

# variables tiranids all_equipments: spinefists, deathspitter, impaler cannon, shock cannon, brainleech devourer,
# heavy venom cannon
spinefists_shooting = StringVar()
deathspitter_shooting = StringVar()
impaler_cannon_shooting = StringVar()
shock_cannon_shooting = StringVar()
brainleech_devourer_shooting = StringVar()
heavy_venom_cannon_shooting = StringVar()

spinefists_amount = 0
deathspitter_amount = 0
impaler_cannon_amount = 0
shock_cannon_amount = 0
brainleech_devourer_amount = 0
heavy_venom_cannon_amount = 0

# GLOBALS:


center_header = Label(main_frame, text="amount of wounds")
center_header.grid(row=0, column=0)
center_label = Label(main_frame, text=f"{probability}", font="Ariel 48", fg="red")
center_label.grid(row=1, column=0, sticky="N")

random_display = Label(main_frame, text="runned test:")
random_display.grid(row=2, column=0, sticky="N", )
lower_labael = Label(main_frame, text=f"{test_run}", font="Ariel 20", fg="green")
lower_labael.grid(row=3, column=0, sticky="N")


def marines_enable_buttons():
    global bolter_amount
    global plasma_amount
    global melta_amount
    global flamer_amount
    global grav_cannon_amount
    global lasscannon_amount

    global bolter_amount_label
    global plasma_amount_label
    global melta_amount_label
    global flamer_amount_label
    global grav_cannon_amount_label
    global lasscannon_amount_label

    if bolter_shooting.get() == "True":
        bolter_sub_button = Button(marines_a, text="-", width=button_x,
                                   command=lambda: sub_shot("marines", marines_armory[0], 1))
        bolter_sub_button.grid(row=1, column=1, sticky="w")
        bolter_amount_label = Label(marines_a, text=f'{bolter_amount:02d}')
        bolter_amount_label.grid(row=1, column=2, sticky="w")
        bolter_add_button = Button(marines_a, text="+", width=button_x,
                                   command=lambda: add_shot("marines", marines_armory[0], 1))
        bolter_add_button.grid(row=1, column=3, sticky="w")
        bolter_sub10_button = Button(marines_a, text="-10", width=button_x,
                                     command=lambda: sub_shot("marines", marines_armory[0], 10))
        bolter_sub10_button.grid(row=1, column=4, padx=5, sticky="w")
        bolter_add10_button = Button(marines_a, text="+10", width=button_x,
                                     command=lambda: add_shot("marines", marines_armory[0], 10))
        bolter_add10_button.grid(row=1, column=5, sticky="w")

        # display_shooting_weapons(bolter_amount, marines_armory[0], True)

    if bolter_shooting.get() == "False":
        bolter_sub_button = Button(marines_a, text="-", width=button_x, state=DISABLED)
        bolter_sub_button.grid(row=1, column=1, sticky="w")
        bolter_amount_label = Label(marines_a, text=f'{bolter_amount:02d}', state=DISABLED)
        bolter_amount_label.grid(row=1, column=2, sticky="w")
        bolter_add_button = Button(marines_a, text="+", width=button_x, state=DISABLED)
        bolter_add_button.grid(row=1, column=3, sticky="w")
        bolter_sub10_button = Button(marines_a, text="-10", width=button_x, state=DISABLED)
        bolter_sub10_button.grid(row=1, column=4, padx=5, sticky="w")
        bolter_add10_button = Button(marines_a, text="+10", width=button_x, state=DISABLED)
        bolter_add10_button.grid(row=1, column=5, sticky="w")

        # display_shooting_weapons(bolter_amount, marines_armory[0], False)

    if plasma_shooting.get() == "True":
        plasma_sub_button = Button(marines_a, text="-", width=button_x,
                                   command=lambda: sub_shot("marines", marines_armory[1], 1))
        plasma_sub_button.grid(row=2, column=1, sticky="w")
        plasma_amount_label = Label(marines_a, text=f'{plasma_amount:02d}')
        plasma_amount_label.grid(row=2, column=2, sticky="w")
        plasma_add_button = Button(marines_a, text="+", width=button_x,
                                   command=lambda: add_shot("marines", marines_armory[1], 1))
        plasma_add_button.grid(row=2, column=3, sticky="w")
        plasma_sub10_button = Button(marines_a, text="-10", width=button_x,
                                     command=lambda: sub_shot("marines", marines_armory[1], 10))
        plasma_sub10_button.grid(row=2, column=4, padx=5, sticky="w")
        plasma_add10_button = Button(marines_a, text="+10", width=button_x,
                                     command=lambda: add_shot("marines", marines_armory[1], 10))
        plasma_add10_button.grid(row=2, column=5, sticky="w")

    if plasma_shooting.get() == "False":
        plasma_sub_button = Button(marines_a, text="+", width=button_x, state=DISABLED)
        plasma_sub_button.grid(row=2, column=3, sticky="w")
        plasma_amount_label = Label(marines_a, text=f'{plasma_amount:02d}', state=DISABLED)
        plasma_amount_label.grid(row=2, column=2, sticky="w")
        plasma_add_button = Button(marines_a, text="-", width=button_x, state=DISABLED)
        plasma_add_button.grid(row=2, column=1, sticky="w")
        plasma_sub10_button = Button(marines_a, text="-10", width=button_x, state=DISABLED)
        plasma_sub10_button.grid(row=2, column=4, padx=5, sticky="w")
        plasma_add10_button = Button(marines_a, text="+10", width=button_x, state=DISABLED)
        plasma_add10_button.grid(row=2, column=5, sticky="w")

    if melta_shooting.get() == "True":
        melta_sub_button = Button(marines_a, text="-", width=button_x, command=lambda: sub_shot("marines", "melta", 1))
        melta_sub_button.grid(row=3, column=1, sticky="w")
        melta_amount_label = Label(marines_a, text=f'{melta_amount:02d}')
        melta_amount_label.grid(row=3, column=2, sticky="w")
        melta_add_button = Button(marines_a, text="+", width=button_x, command=lambda: add_shot("marines", "melta", 1))
        melta_add_button.grid(row=3, column=3, sticky="w")
        melta_sub10_button = Button(marines_a, text="-10", width=button_x,
                                    command=lambda: sub_shot("marines", "melta", 10))
        melta_sub10_button.grid(row=3, column=4, padx=5, sticky="w")
        melta_add10_button = Button(marines_a, text="+10", width=button_x,
                                    command=lambda: add_shot("marines", "melta", 10))
        melta_add10_button.grid(row=3, column=5, sticky="w")

    if melta_shooting.get() == "False":
        melta_sub_button = Button(marines_a, text="+", width=button_x, state=DISABLED)
        melta_sub_button.grid(row=3, column=3, sticky="w")
        melta_amount_label = Label(marines_a, text=f'{melta_amount:02d}', state=DISABLED)
        melta_amount_label.grid(row=3, column=2, sticky="w")
        melta_add_button = Button(marines_a, text="-", width=button_x, state=DISABLED)
        melta_add_button.grid(row=3, column=1, sticky="w")
        melta_sub10_button = Button(marines_a, text="-10", width=button_x, state=DISABLED)
        melta_sub10_button.grid(row=3, column=4, padx=5, sticky="w")
        melta_add10_button = Button(marines_a, text="+10", width=button_x, state=DISABLED)
        melta_add10_button.grid(row=3, column=5, sticky="w")

    if flamer_shooting.get() == "True":
        flamer_sub_button = Button(marines_a, text="-", width=button_x,
                                   command=lambda: sub_shot("marines", "flamer", 1))
        flamer_sub_button.grid(row=4, column=1, sticky="w")
        flamer_amount_label = Label(marines_a, text=f'{flamer_amount:02d}')
        flamer_amount_label.grid(row=4, column=2, sticky="w")
        flamer_add_button = Button(marines_a, text="+", width=button_x,
                                   command=lambda: add_shot("marines", "flamer", 1))
        flamer_add_button.grid(row=4, column=3, sticky="w")
        flamer_sub10_button = Button(marines_a, text="-10", width=button_x,
                                     command=lambda: sub_shot("marines", "flamer", 10))
        flamer_sub10_button.grid(row=4, column=4, padx=5, sticky="w")
        flamer_add10_button = Button(marines_a, text="+10", width=button_x,
                                     command=lambda: add_shot("marines", "flamer", 10))
        flamer_add10_button.grid(row=4, column=5, sticky="w")

    if flamer_shooting.get() == "False":
        flamer_sub_button = Button(marines_a, text="-", width=button_x, state=DISABLED)
        flamer_sub_button.grid(row=4, column=1, sticky="w")
        flamer_amount_label = Label(marines_a, text=f'{flamer_amount:02d}', state=DISABLED)
        flamer_amount_label.grid(row=4, column=2, sticky="w")
        flamer_add_button = Button(marines_a, text="+", width=button_x, state=DISABLED)
        flamer_add_button.grid(row=4, column=3, sticky="w")
        flamer_sub10_button = Button(marines_a, text="-10", width=button_x, state=DISABLED)
        flamer_sub10_button.grid(row=4, column=4, padx=5, sticky="w")
        flamer_add10_button = Button(marines_a, text="+10", width=button_x, state=DISABLED)
        flamer_add10_button.grid(row=4, column=5, sticky="w")

    if grav_cannon_shooting.get() == "True":
        grav_cannon_sub_button = Button(marines_a, text="-", width=button_x,
                                        command=lambda: sub_shot("marines", "grav_cannon", 1))
        grav_cannon_sub_button.grid(row=5, column=1, sticky="w")
        grav_cannon_amount_label = Label(marines_a, text=f'{grav_cannon_amount:02d}')
        grav_cannon_amount_label.grid(row=5, column=2, sticky="w")
        grav_cannon_add_button = Button(marines_a, text="+", width=button_x,
                                        command=lambda: add_shot("marines", "grav_cannon", 1))
        grav_cannon_add_button.grid(row=5, column=3, sticky="w")
        grav_cannon_sub10_button = Button(marines_a, text="-10", width=button_x,
                                          command=lambda: sub_shot("marines", "grav_cannon", 10))
        grav_cannon_sub10_button.grid(row=5, column=4, padx=5, sticky="w")
        grav_cannon_add10_button = Button(marines_a, text="+10", width=button_x,
                                          command=lambda: add_shot("marines", "grav_cannon", 10))
        grav_cannon_add10_button.grid(row=5, column=5, sticky="W")

    if grav_cannon_shooting.get() == "False":
        grav_cannon_sub_button = Button(marines_a, text="-", width=button_x, state=DISABLED)
        grav_cannon_sub_button.grid(row=5, column=1, sticky="w")
        grav_cannon_amount_label = Label(marines_a, text=f'{grav_cannon_amount:02d}', state=DISABLED)
        grav_cannon_amount_label.grid(row=5, column=2, sticky="w")
        grav_cannon_add_button = Button(marines_a, text="+", width=button_x, state=DISABLED)
        grav_cannon_add_button.grid(row=5, column=3, sticky="w")
        grav_cannon_sub10_button = Button(marines_a, text="-10", width=button_x, state=DISABLED)
        grav_cannon_sub10_button.grid(row=5, column=4, padx=5, sticky="w")
        grav_cannon_add10_button = Button(marines_a, text="+10", width=button_x, state=DISABLED)
        grav_cannon_add10_button.grid(row=5, column=5, sticky="W")

    if lasscannon_shooting.get() == "True":
        lasscannon_sub_button = Button(marines_a, text="-", width=button_x,
                                       command=lambda: sub_shot("marines", "lasscannon", 1))
        lasscannon_sub_button.grid(row=6, column=1, sticky="W")
        lasscannon_amount_label = Label(marines_a, text=f'{lasscannon_amount:02d}')
        lasscannon_amount_label.grid(row=6, column=2, sticky="W")
        lasscannon_add_button = Button(marines_a, text="+", width=button_x,
                                       command=lambda: add_shot("marines", "lasscannon", 1))
        lasscannon_add_button.grid(row=6, column=3, sticky="W")
        lasscannon_sub10_button = Button(marines_a, text="-10", width=button_x,
                                         command=lambda: sub_shot("marines", "lasscannon", 10))
        lasscannon_sub10_button.grid(row=6, column=4, padx=5, sticky="W")
        lasscannon_add10_button = Button(marines_a, text="+10", width=button_x,
                                         command=lambda: add_shot("marines", "lasscannon", 10))
        lasscannon_add10_button.grid(row=6, column=5, sticky="W")

    if lasscannon_shooting.get() == "False":
        lasscannon_sub_button = Button(marines_a, text="-", width=button_x, state=DISABLED)
        lasscannon_sub_button.grid(row=6, column=1, sticky="W")
        lasscannon_amount_label = Label(marines_a, text=f'{lasscannon_amount:02d}', state=DISABLED)
        lasscannon_amount_label.grid(row=6, column=2, sticky="W")
        lasscannon_add_button = Button(marines_a, text="+", width=button_x, state=DISABLED)
        lasscannon_add_button.grid(row=6, column=3, sticky="W")
        lasscannon_sub10_button = Button(marines_a, text="-10", width=button_x, state=DISABLED)
        lasscannon_sub10_button.grid(row=6, column=4, padx=5, sticky="EW")
        lasscannon_add10_button = Button(marines_a, text="+10", width=button_x, state=DISABLED)
        lasscannon_add10_button.grid(row=6, column=5, sticky="W")


def tau_enable_buttons():
    if pulse_rifle_shooting.get() == "True":
        pulse_rifle_sub_button = Button(tau_a, text="-", width=button_x)
        pulse_rifle_sub_button.grid(row=1, column=1, sticky="w")
        pulse_rifle_amount_label = Label(tau_a, text=f'{bolter_amount:02d}')
        pulse_rifle_amount_label.grid(row=1, column=2, sticky="w")
        pulse_rifle_add_button = Button(tau_a, text="+", width=button_x)
        pulse_rifle_add_button.grid(row=1, column=3, sticky="w")
        pulse_rifle_sub10_button = Button(tau_a, text="-10", width=button_x)
        pulse_rifle_sub10_button.grid(row=1, column=4, padx=5, sticky="w")
        pulse_rifle_add10_button = Button(tau_a, text="+10", width=button_x)
        pulse_rifle_add10_button.grid(row=1, column=5, sticky="w")

    if pulse_rifle_shooting.get() == "False":
        pulse_rifle_sub_button = Button(tau_a, text="-", width=button_x, state=DISABLED)
        pulse_rifle_sub_button.grid(row=1, column=1, sticky="w")
        pulse_rifle_amount_label = Label(tau_a, text=f'{bolter_amount:02d}', state=DISABLED)
        pulse_rifle_amount_label.grid(row=1, column=2, sticky="w")
        pulse_rifle_add_button = Button(tau_a, text="+", width=button_x, state=DISABLED)
        pulse_rifle_add_button.grid(row=1, column=3, sticky="w")
        pulse_rifle_sub10_button = Button(tau_a, text="-10", width=button_x, state=DISABLED)
        pulse_rifle_sub10_button.grid(row=1, column=4, padx=5, sticky="w")
        pulse_rifle_add10_button = Button(tau_a, text="+10", width=button_x, state=DISABLED)
        pulse_rifle_add10_button.grid(row=1, column=5, sticky="w")

    if plasma_rifle_shooting.get() == "True":
        plasma_rifle_sub_button = Button(tau_a, text="+", width=button_x)
        plasma_rifle_sub_button.grid(row=2, column=3, sticky="w")
        plasma_rifle_amount_label = Label(tau_a, text=f'{plasma_amount:02d}')
        plasma_rifle_amount_label.grid(row=2, column=2, sticky="w")
        plasma_rifle_add_button = Button(tau_a, text="-", width=button_x)
        plasma_rifle_add_button.grid(row=2, column=1, sticky="w")
        plasma_rifle_sub10_button = Button(tau_a, text="-10", width=button_x)
        plasma_rifle_sub10_button.grid(row=2, column=4, padx=5, sticky="w")
        plasma_rifle_add10_button = Button(tau_a, text="+10", width=button_x)
        plasma_rifle_add10_button.grid(row=2, column=5, sticky="w")

    if plasma_rifle_shooting.get() == "False":
        plasma_rifle_sub_button = Button(tau_a, text="-", width=button_x, state=DISABLED)
        plasma_rifle_sub_button.grid(row=2, column=1, sticky="w")
        plasma_rifle_amount_label = Label(tau_a, text=f'{bolter_amount:02d}', state=DISABLED)
        plasma_rifle_amount_label.grid(row=2, column=2, sticky="w")
        plasma_rifle_add_button = Button(tau_a, text="+", width=button_x, state=DISABLED)
        plasma_rifle_add_button.grid(row=2, column=3, sticky="w")
        plasma_rifle_sub10_button = Button(tau_a, text="-10", width=button_x, state=DISABLED)
        plasma_rifle_sub10_button.grid(row=2, column=4, padx=5, sticky="w")
        plasma_rifle_add10_button = Button(tau_a, text="+10", width=button_x, state=DISABLED)
        plasma_rifle_add10_button.grid(row=2, column=5, sticky="w")

    if fusion_blaster_shooting.get() == "True":
        fusion_blaster_sub_button = Button(tau_a, text="+", width=button_x)
        fusion_blaster_sub_button.grid(row=3, column=3, sticky="w")
        fusion_blaster_amount_label = Label(tau_a, text=f'{melta_amount:02d}')
        fusion_blaster_amount_label.grid(row=3, column=2, sticky="w")
        fusion_blaster_add_button = Button(tau_a, text="-", width=button_x)
        fusion_blaster_add_button.grid(row=3, column=1, sticky="w")
        fusion_blaster_sub10_button = Button(tau_a, text="-10", width=button_x)
        fusion_blaster_sub10_button.grid(row=3, column=4, padx=5, sticky="w")
        fusion_blaster_add10_button = Button(tau_a, text="+10", width=button_x)
        fusion_blaster_add10_button.grid(row=3, column=5, sticky="w")

    if fusion_blaster_shooting.get() == "False":
        fusion_blaster_sub_button = Button(tau_a, text="-", width=button_x, state=DISABLED)
        fusion_blaster_sub_button.grid(row=3, column=1, sticky="w")
        fusion_blaster_amount_label = Label(tau_a, text=f'{bolter_amount:02d}', state=DISABLED)
        fusion_blaster_amount_label.grid(row=3, column=2, sticky="w")
        fusion_blaster_add_button = Button(tau_a, text="+", width=button_x, state=DISABLED)
        fusion_blaster_add_button.grid(row=3, column=3, sticky="w")
        fusion_blaster_sub10_button = Button(tau_a, text="-10", width=button_x, state=DISABLED)
        fusion_blaster_sub10_button.grid(row=3, column=4, padx=5, sticky="w")
        fusion_blaster_add10_button = Button(tau_a, text="+10", width=button_x, state=DISABLED)
        fusion_blaster_add10_button.grid(row=3, column=5, sticky="w")

    if missile_pod_shooting.get() == "True":
        missile_pod_sub_button = Button(tau_a, text="+", width=button_x)
        missile_pod_sub_button.grid(row=4, column=3, sticky="w")
        missile_pod_amount_label = Label(tau_a, text=f'{flamer_amount:02d}')
        missile_pod_amount_label.grid(row=4, column=2, sticky="w")
        missile_pod_add_button = Button(tau_a, text="-", width=button_x)
        missile_pod_add_button.grid(row=4, column=1, sticky="w")
        missile_pod_sub10_button = Button(tau_a, text="-10", width=button_x)
        missile_pod_sub10_button.grid(row=4, column=4, padx=5, sticky="w")
        missile_pod_add10_button = Button(tau_a, text="+10", width=button_x)
        missile_pod_add10_button.grid(row=4, column=5, sticky="w")

    if missile_pod_shooting.get() == "False":
        missile_pod_sub_button = Button(tau_a, text="-", width=button_x, state=DISABLED)
        missile_pod_sub_button.grid(row=4, column=1, sticky="w")
        missile_pod_amount_label = Label(tau_a, text=f'{bolter_amount:02d}', state=DISABLED)
        missile_pod_amount_label.grid(row=4, column=2, sticky="w")
        missile_pod_add_button = Button(tau_a, text="+", width=button_x, state=DISABLED)
        missile_pod_add_button.grid(row=4, column=3, sticky="w")
        missile_pod_sub10_button = Button(tau_a, text="-10", width=button_x, state=DISABLED)
        missile_pod_sub10_button.grid(row=4, column=4, padx=5, sticky="w")
        missile_pod_add10_button = Button(tau_a, text="+10", width=button_x, state=DISABLED)
        missile_pod_add10_button.grid(row=4, column=5, sticky="w")

    if smart_missiles_shooting.get() == "True":
        smart_missiles_sub_button = Button(tau_a, text="+", width=button_x)
        smart_missiles_sub_button.grid(row=5, column=3, sticky="w")
        smart_missiles_amount_label = Label(tau_a, text=f'{grav_cannon_amount:02d}')
        smart_missiles_amount_label.grid(row=5, column=2, sticky="w")
        smart_missiles_add_button = Button(tau_a, text="-", width=button_x)
        smart_missiles_add_button.grid(row=5, column=1, sticky="w")
        smart_missiles_sub10_button = Button(tau_a, text="-10", width=button_x)
        smart_missiles_sub10_button.grid(row=5, column=4, padx=5, sticky="w")
        smart_missiles_add10_button = Button(tau_a, text="+10", width=button_x)
        smart_missiles_add10_button.grid(row=5, column=5, sticky="W")

    if smart_missiles_shooting.get() == "False":
        smart_missiles_sub_button = Button(tau_a, text="-", width=button_x, state=DISABLED)
        smart_missiles_sub_button.grid(row=5, column=1, sticky="w")
        smart_missiles_amount_label = Label(tau_a, text=f'{bolter_amount:02d}', state=DISABLED)
        smart_missiles_amount_label.grid(row=5, column=2, sticky="w")
        smart_missiles_add_button = Button(tau_a, text="+", width=button_x, state=DISABLED)
        smart_missiles_add_button.grid(row=5, column=3, sticky="w")
        smart_missiles_sub10_button = Button(tau_a, text="-10", width=button_x, state=DISABLED)
        smart_missiles_sub10_button.grid(row=5, column=4, padx=5, sticky="w")
        smart_missiles_add10_button = Button(tau_a, text="+10", width=button_x, state=DISABLED)
        smart_missiles_add10_button.grid(row=5, column=5, sticky="w")

    if heavy_burst_cannon_shooting.get() == "True":
        heavy_burst_cannon_sub_button = Button(tau_a, text="+", width=button_x)
        heavy_burst_cannon_sub_button.grid(row=6, column=3, sticky="W")
        heavy_burst_cannon_amount_label = Label(tau_a, text=f'{lasscannon_amount:02d}')
        heavy_burst_cannon_amount_label.grid(row=6, column=2, sticky="W")
        heavy_burst_cannon_add_button = Button(tau_a, text="-", width=button_x)
        heavy_burst_cannon_add_button.grid(row=6, column=1, sticky="W")
        heavy_burst_cannon_sub10_button = Button(tau_a, text="-10", width=button_x)
        heavy_burst_cannon_sub10_button.grid(row=6, column=4, padx=5, sticky="EW")
        heavy_burst_cannon_add10_button = Button(tau_a, text="+10", width=button_x)
        heavy_burst_cannon_add10_button.grid(row=6, column=5, sticky="W")

    if heavy_burst_cannon_shooting.get() == "False":
        heavy_burst_cannon_sub_button = Button(tau_a, text="-", width=button_x, state=DISABLED)
        heavy_burst_cannon_sub_button.grid(row=6, column=1, sticky="w")
        heavy_burst_cannon_amount_label = Label(tau_a, text=f'{bolter_amount:02d}', state=DISABLED)
        heavy_burst_cannon_amount_label.grid(row=6, column=2, sticky="w")
        heavy_burst_cannon_add_button = Button(tau_a, text="+", width=button_x, state=DISABLED)
        heavy_burst_cannon_add_button.grid(row=6, column=3, sticky="w")
        heavy_burst_cannon_sub10_button = Button(tau_a, text="-10", width=button_x, state=DISABLED)
        heavy_burst_cannon_sub10_button.grid(row=6, column=4, padx=5, sticky="w")
        heavy_burst_cannon_add10_button = Button(tau_a, text="+10", width=button_x, state=DISABLED)
        heavy_burst_cannon_add10_button.grid(row=6, column=5, sticky="w")


def tyranids_enable_button():
    pass


def set_marines_weapons():
    global bolter_amount
    global plasma_amount
    global melta_amount
    global flamer_amount
    global grav_cannon_amount
    global lasscannon_amount

    global bolter_sub_button
    global bolter_amount_label
    global plasma_amount_label
    global melta_amount_label
    global flamer_amount_label
    global grav_cannon_amount_label
    global lasscannon_amount_label

    # print(f"""
    # bolter      shooting  {is_shooting.get()},
    # plasma      shooting  {plasma_shooting.get()},
    # melta       shooting  {melta_shooting.get()},
    # flamer      shooting  {flamer_shooting.get()},
    # grav cannon shooting  {grav_cannon_shooting.get()},
    # lasscannon  shooting  {lasscannon_shooting.get()}""")

    if bolter_shooting.get() == "True":
        bolter_sub_button["command"] = lambda: sub_shot("marines", "bolter")
        # bolter_sub_button.grid(row=1, column=1, sticky="w")
        bolter_amount_label["cajlito_army"] = f'{bolter_amount:02d}'
        bolter_amount_label.grid(row=1, column=2, sticky="w")
        bolter_add_button = Button(marines_a, text="+", width=button_x, command=lambda: add_shot("marines", "bolter"))
        bolter_add_button.grid(row=1, column=3, sticky="w")
    if bolter_shooting.get() == "False":
        bolter_amount = 0
        bolter_sub_button = Button(marines_a, text="-", width=button_x, state=DISABLED)
        bolter_sub_button.grid(row=1, column=1, sticky="w")
        bolter_amount_label["cajlito_army"] = f'{bolter_amount:02d}'
        bolter_amount_label["state"] = DISABLED
        bolter_amount_label.grid(row=1, column=2, sticky="w")
        bolter_add_button = Button(marines_a, text="+", width=button_x, state=DISABLED)
        bolter_add_button.grid(row=1, column=3, sticky="w")

    if plasma_shooting.get() == "True":
        plasma_sub_button = Button(marines_a, text="-", width=button_x, command=lambda: sub_shot("marines", "plasma"))
        plasma_sub_button.grid(row=2, column=1, sticky="w")
        plasma_amount_label = Label(marines_a, text=f'{plasma_amount:02d}')
        plasma_amount_label.grid(row=2, column=2, sticky="w")
        plasma_add_button = Button(marines_a, text="+", width=button_x, command=lambda: add_shot("marines", "plasma"))
        plasma_add_button.grid(row=2, column=3, sticky="w")
    if plasma_shooting.get() == "False":
        plasma_amount = 0
        plasma_sub_button = Button(marines_a, text="-", width=button_x, state=DISABLED)
        plasma_sub_button.grid(row=2, column=1, sticky="w")
        plasma_amount_label = Label(marines_a, text=f'{plasma_amount:02d}', state=DISABLED)
        plasma_amount_label.grid(row=2, column=2, sticky="w")
        plasma_add_button = Button(marines_a, text="+", width=button_x, state=DISABLED)
        plasma_add_button.grid(row=2, column=3, sticky="w")

    if melta_shooting.get() == "True":
        melta_sub_button = Button(marines_a, text="-", width=button_x, command=lambda: sub_shot("marines", "melta"))
        melta_sub_button.grid(row=3, column=1, sticky="w")
        melta_amount_label = Label(marines_a, text=f'{melta_amount:02d}')
        melta_amount_label.grid(row=3, column=2, sticky="w")
        melta_add_button = Button(marines_a, text="+", width=button_x, command=lambda: add_shot("marines", "melta"))
        melta_add_button.grid(row=3, column=3, sticky="w")
    if melta_shooting.get() == "False":
        melta_amount = 0
        melta_sub_button = Button(marines_a, text="-", width=button_x, state=DISABLED)
        melta_sub_button.grid(row=3, column=1, sticky="w")
        melta_amount_label = Label(marines_a, text=f'{melta_amount:02d}', state=DISABLED)
        melta_amount_label.grid(row=3, column=2, sticky="w")
        melta_add_button = Button(marines_a, text="+", width=button_x, state=DISABLED)
        melta_add_button.grid(row=3, column=3, sticky="w")

    if flamer_shooting.get() == "True":
        flamer_sub_button = Button(marines_a, text="-", width=button_x, command=lambda: sub_shot("marines", "flamer"))
        flamer_sub_button.grid(row=4, column=1, sticky="w")
        flamer_amount_label = Label(marines_a, text=f'{flamer_amount:02d}')
        flamer_amount_label.grid(row=4, column=2, sticky="w")
        flamer_add_button = Button(marines_a, text="+", width=button_x, command=lambda: add_shot("marines", "flamer"))
        flamer_add_button.grid(row=4, column=3, sticky="w")
    if flamer_shooting.get() == "False":
        flamer_amount = 0
        flamer_sub_button = Button(marines_a, text="-", width=button_x, state=DISABLED)
        flamer_sub_button.grid(row=4, column=1, sticky="w")
        flamer_amount_label = Label(marines_a, text=f'{flamer_amount:02d}', state=DISABLED)
        flamer_amount_label.grid(row=4, column=2, sticky="w")
        flamer_add_button = Button(marines_a, text="+", width=button_x, state=DISABLED)
        flamer_add_button.grid(row=4, column=3, sticky="w")

    if grav_cannon_shooting.get() == "True":
        grav_cannon_sub_button = Button(marines_a, text="-", width=button_x,
                                        command=lambda: sub_shot("marines", "grav_cannon"))
        grav_cannon_sub_button.grid(row=5, column=1, sticky="w")
        grav_cannon_amount_label = Label(marines_a, text=f'{grav_cannon_amount:02d}')
        grav_cannon_amount_label.grid(row=5, column=2, sticky="w")
        grav_cannon_add_button = Button(marines_a, text="+", width=button_x,
                                        command=lambda: add_shot("marines", "grav_cannon"))
        grav_cannon_add_button.grid(row=5, column=3, sticky="w")
    if grav_cannon_shooting.get() == "False":
        grav_cannon_amount = 0
        grav_cannon_sub_button = Button(marines_a, text="+", width=button_x, state=DISABLED)
        grav_cannon_sub_button.grid(row=5, column=3, sticky="w")
        grav_cannon_amount_label = Label(marines_a, text=f"{grav_cannon_amount:02d}", state=DISABLED)
        grav_cannon_amount_label.grid(row=5, column=2, sticky="w")
        grav_cannon_add_button = Button(marines_a, text="-", width=button_x, state=DISABLED)
        grav_cannon_add_button.grid(row=5, column=1, sticky="w")

    if lasscannon_shooting.get() == "True":
        lasscannon_sub_button = Button(marines_a, text="-", width=button_x,
                                       command=lambda: sub_shot("marines", "lasscannon"))
        lasscannon_sub_button.grid(row=6, column=1, sticky="w")
        lasscannon_amount_label = Label(marines_a, text=f'{lasscannon_amount:02d}')
        lasscannon_amount_label.grid(row=6, column=2, sticky="w")
        lasscannon_add_button = Button(marines_a, text="+", command=lambda: add_shot("marines", "lasscannon"))
        lasscannon_add_button.grid(row=6, column=3, sticky="w")
    if lasscannon_shooting.get() == "False":
        lasscannon_amount = 0
        lasscannon_sub_button = Button(marines_a, text="-", width=button_x, state=DISABLED)
        lasscannon_sub_button.grid(row=6, column=1, sticky="w")
        lasscannon_amount_label = Label(marines_a, text=f'{lasscannon_amount:02d}', state=DISABLED)
        lasscannon_amount_label.grid(row=6, column=2, sticky="w")
        lasscannon_add_button = Button(marines_a, text="-", width=button_x, state=DISABLED)
        lasscannon_add_button.grid(row=6, column=3, sticky="w")


def set_Tau_weapons():
    global plasma_rifle_amount
    global pulse_rifle_amount
    global fusion_blaster_amount
    global missile_pod_amount
    global smart_missiles_amount
    global heavy_burst_cannon_amount

    global pulse_rifle_amount_label
    global plasma_rifle_amount_label
    global fusion_blaster_amount_label
    global missile_pod_amount_label
    global smart_missile_amount_label
    global heavy_burst_cannon_amount_label

    # print(f"""
    # pulse rifle         shooting  {pulse_rifle_shooting.get()},
    # plasma rifle        shooting  {plasma_rifle_shooting.get()},
    # fusion blaster      shooting  {fusion_blaster_shooting.get()},
    # missile pod         shooting  {missile_pod_shooting.get()},
    # smart missiles      shooting  {smart_missiles_shooting.get()},
    # Heavy burst cannon  shooting  {heavy_burst_cannon_shooting.get()}""")

    if pulse_rifle_shooting.get() == "True":
        pulse_rifle_sub_button = Button(tau_a, text="-", width=button_x, command=lambda: sub_shot("tau", "pulse_rifle"))
        pulse_rifle_sub_button.grid(row=1, column=1, sticky="w")
        pulse_rifle_amount_label["cajlito_army"] = f"{pulse_rifle_amount:02d}"
        # pulse_rifle_amount_label.grid(row=1, column=2, sticky="w")
        pulse_rifle_add_button = Button(tau_a, text="+", width=button_x, command=lambda: add_shot("tau", "pulse_rifle"))
        pulse_rifle_add_button.grid(row=1, column=3, sticky="w")
    if pulse_rifle_shooting.get() == "False":
        pulse_rifle_amount = 0
        pulse_rifle_sub_button = Button(tau_a, text="-", width=button_x, state=DISABLED)
        pulse_rifle_sub_button.grid(row=1, column=1, sticky="w")
        pulse_rifle_amount_label = Label(tau_a, text=f"{pulse_rifle_amount:02d}", state=DISABLED)
        pulse_rifle_amount_label.grid(row=1, column=2, sticky="w")
        pulse_rifle_add_button = Button(tau_a, text="+", width=button_x, state=DISABLED)
        pulse_rifle_add_button.grid(row=1, column=3, sticky="w")

    if plasma_rifle_shooting.get() == "True":
        plasma_rifle_sub_button = Button(tau_a, text="-", width=button_x,
                                         command=lambda: sub_shot("tau", "plasma_rifle"))
        plasma_rifle_sub_button.grid(row=2, column=1, sticky="w")
        plasma_rifle__amount_label = Label(tau_a, text=f"{plasma_rifle_amount:02d}")
        plasma_rifle__amount_label.grid(row=2, column=2, sticky="w")
        plasma_rifle__add_button = Button(tau_a, text="+", width=button_x,
                                          command=lambda: add_shot("tau", "plasma_rifle_"))
        plasma_rifle__add_button.grid(row=2, column=3, sticky="w")
    if plasma_rifle_shooting.get() == "False":
        plasma_rifle_amount = 0
        plasma_rifle_sub_button = Button(tau_a, text="-", width=button_x, state=DISABLED)
        plasma_rifle_sub_button.grid(row=2, column=1, sticky="w")
        plasma_rifle_amount_label = Label(tau_a, text=f"{plasma_rifle_amount:02d}", state=DISABLED)
        plasma_rifle_amount_label.grid(row=2, column=2, sticky="w")
        plasma_rifle_add_button = Button(tau_a, text="+", width=button_x, state=DISABLED)
        plasma_rifle_add_button.grid(row=2, column=3, sticky="w")

    if fusion_blaster_shooting.get() == "True":
        fusion_blaster_sub_button = Button(tau_a, text="-", width=button_x,
                                           command=lambda: sub_shot("tau", "fusion_blaster"))
        fusion_blaster_sub_button.grid(row=3, column=1, sticky="w")
        fusion_blaster_amount_label = Label(tau_a, text=f"{fusion_blaster_amount:02d}")
        fusion_blaster_amount_label.grid(row=3, column=2, sticky="w")
        fusion_blaster_add_button = Button(tau_a, text="+", width=button_x,
                                           command=lambda: add_shot("tau", "fusion_blaster"))
        fusion_blaster_add_button.grid(row=3, column=3, sticky="w")
    if fusion_blaster_shooting.get() == "False":
        fusion_blaster_amount = 0
        fusion_blaster_sub_button = Button(tau_a, text="-", width=button_x, state=DISABLED)
        fusion_blaster_sub_button.grid(row=3, column=1, sticky="w")
        fusion_blaster_amount_label = Label(tau_a, text=f"{fusion_blaster_amount:02d}", state=DISABLED)
        fusion_blaster_amount_label.grid(row=3, column=2, sticky="w")
        fusion_blaster_add_button = Button(tau_a, text="+", width=button_x, state=DISABLED)
        fusion_blaster_add_button.grid(row=3, column=3, sticky="w")

    if missile_pod_shooting.get() == "True":
        missile_pod_sub_button = Button(tau_a, text="-", width=button_x, command=lambda: sub_shot("tau", "missile_pod"))
        missile_pod_sub_button.grid(row=4, column=1, sticky="w")
        missile_pod_amount_label = Label(tau_a, text=f"{missile_pod_amount:02d}")
        missile_pod_amount_label.grid(row=4, column=2, sticky="w")
        missile_pod_add_button = Button(tau_a, text="+", width=button_x, command=lambda: add_shot("tau", "missile_pod"))
        missile_pod_add_button.grid(row=4, column=3, sticky="w")
    if missile_pod_shooting.get() == "False":
        missile_pod_amount = 0
        missile_pod_sub_button = Button(tau_a, text="-", width=button_x, state=DISABLED)
        missile_pod_sub_button.grid(row=4, column=1, sticky="w")
        missile_pod_amount_label = Label(tau_a, text=f"{missile_pod_amount:02d}", state=DISABLED)
        missile_pod_amount_label.grid(row=4, column=2, sticky="w")
        missile_pod_add_button = Button(tau_a, text="+", width=button_x, state=DISABLED)
        missile_pod_add_button.grid(row=4, column=3, sticky="w")

    if smart_missiles_shooting.get() == "True":
        smart_missiles_sub_button = Button(tau_a, text="-", width=button_x,
                                           command=lambda: sub_shot("tau", "smart_missiles"))
        smart_missiles_sub_button.grid(row=5, column=1, sticky="w")
        smart_missiles_amount_label = Label(tau_a, text=f"{smart_missiles_amount:02d}")
        smart_missiles_amount_label.grid(row=5, column=2, sticky="w")
        smart_missiles_add_button = Button(tau_a, text="+", width=button_x,
                                           command=lambda: add_shot("tau", "smart_missiles"))
        smart_missiles_add_button.grid(row=5, column=3, sticky="w")
    if smart_missiles_shooting.get() == "False":
        smart_missiles_amount = 0
        smart_missiles_sub_button = Button(tau_a, text="-", width=button_x, state=DISABLED)
        smart_missiles_sub_button.grid(row=5, column=1, sticky="w")
        smart_missiles_amount_label = Label(tau_a, text=f"{smart_missiles_amount:02d}", state=DISABLED)
        smart_missiles_amount_label.grid(row=5, column=2, sticky="w")
        smart_missiles_add_button = Button(tau_a, text="+", width=button_x, state=DISABLED)
        smart_missiles_add_button.grid(row=5, column=3, sticky="w")

    if heavy_burst_cannon_shooting.get() == "True":
        heavy_burst_cannon_sub_button = Button(tau_a, text="-", width=button_x,
                                               command=lambda: sub_shot("tau", "heavy_burst"))
        heavy_burst_cannon_sub_button.grid(row=6, column=1, sticky="w")
        heavy_burst_cannon_amount_label = Label(tau_a, text=f"{heavy_burst_cannon_amount:02d}")
        heavy_burst_cannon_amount_label.grid(row=6, column=2, sticky="w")
        heavy_burst_cannon_add_button = Button(tau_a, text="+", width=button_x,
                                               command=lambda: add_shot("tau", "heavy_burst"))
        heavy_burst_cannon_add_button.grid(row=6, column=3, sticky="w")
    if heavy_burst_cannon_shooting.get() == "False":
        heavy_burst_cannon_amount = 0
        heavy_burst_cannon_sub_button = Button(tau_a, text="-", width=button_x, state=DISABLED)
        heavy_burst_cannon_sub_button.grid(row=6, column=1, sticky="w")
        heavy_burst_cannon_amount_label = Label(tau_a, text=f"{heavy_burst_cannon_amount:02d}", state=DISABLED)
        heavy_burst_cannon_amount_label.grid(row=6, column=2, sticky="w")
        heavy_burst_cannon_add_button = Button(tau_a, text="+", width=button_x, state=DISABLED)
        heavy_burst_cannon_add_button.grid(row=6, column=3, sticky="w")


# spinefists, deathspitter, impaler cannon, shock cannon, brainleech devourer, Hheavy venom cannon
# def set_tiranids_weapons():
#     print(f"""
#     spinefists          shooting  {spinefists_shooting.get()},
#     deathspitter        shooting  {deathspitter_shooting.get()},
#     impaler cannon      shooting  {impaler_cannon_shooting.get()},
#     shock cannon        shooting  {shock_cannon_shooting.get()},
#     brainleech devourer shooting  {brainleech_devourer_shooting.get()},
#     heavy venom cannon  shooting  {heavy_venom_cannon_shooting.get()}""")


def add_shot(army, weapon, n):
    global bolter_amount
    global plasma_amount
    global melta_amount
    global flamer_amount
    global grav_cannon_amount
    global lasscannon_amount

    global bolter_amount_label
    global plasma_amount_label
    global melta_amount_label
    global flamer_amount_label
    global grav_cannon_amount_label
    global lasscannon_amount_label

    global pulse_rifle_amount
    global plasma_rifle_amount
    global fusion_blaster_amount
    global missile_pod_amount
    global smart_missile_amount
    global heavy_burst_cannon_amount

    global pulse_rifle_amount_label
    global plasma_rifle_amount_label
    global fusion_blaster_amount_label
    global missile_pod_amount_label
    global smart_missile_amount_label
    global heavy_burst_cannon_amount_label

    if army == "marines":

        if weapon == "bolter" and bolter_amount < 100:
            bolter_amount += n
            bolter_amount_label.grid_forget()

            bolter_amount_label = Label(marines_a, text=f'{bolter_amount:02d}')
            bolter_amount_label.grid(row=1, column=2, sticky="w")
            # print(bolter_amount)

        if weapon == "plasma" and plasma_amount < 100:
            plasma_amount += n
            plasma_amount_label.grid_forget()

            plasma_amount_label = Label(marines_a, text=f'{plasma_amount:02d}')
            plasma_amount_label.grid(row=2, column=2, sticky="w")
            # print(plasma_amount)

        if weapon == "melta" and melta_amount < 100:
            melta_amount += n
            melta_amount_label.grid_forget()

            melta_amount_label = Label(marines_a, text=f'{melta_amount:02d}')
            melta_amount_label.grid(row=3, column=2, sticky="w")
            # print(melta_amount)

        if weapon == "flamer" and flamer_amount < 100:
            flamer_amount += n
            flamer_amount_label.grid_forget()

            flamer_amount_label = Label(marines_a, text=f'{flamer_amount:02d}')
            flamer_amount_label.grid(row=4, column=2, sticky="w")
            # print(flamer_amount)

        if weapon == "grav_cannon" and grav_cannon_amount < 100:
            grav_cannon_amount += n
            grav_cannon_amount_label.grid_forget()

            grav_cannon_amount_label = Label(marines_a, text=f'{grav_cannon_amount:02d}')
            grav_cannon_amount_label.grid(row=5, column=2, sticky="w")
            # print(grav_cannon_amount)

        if weapon == "lasscannon" and lasscannon_amount < 100:
            lasscannon_amount += n
            lasscannon_amount_label.grid_forget()

            lasscannon_amount_label = Label(marines_a, text=f'{lasscannon_amount:02d}')
            lasscannon_amount_label.grid(row=6, column=2, sticky="w")
            # print(lasscannon_amount)

        if army == "tau":

            if weapon == "pulse_rifle" and pulse_rifle_amount < 100:
                pulse_rifle_amount += n
                pulse_rifle_amount_label.grid_forget()

                pulse_rifle_amount_label = Label(tau_a, text=f'{pulse_rifle_amount:02d}')
                pulse_rifle_amount_label.grid(row=1, column=2, sticky="w")

            if weapon == "plasma_rifle" and plasma_rifle_amount < 100:
                plasma_rifle_amount += n
                plasma_rifle_amount_label.grid_forget()

                plasma_rifle_amount_label = Label(tau_a, text=f'{plasma_rifle_amount:02d}')
                plasma_rifle_amount_label.grid(row=2, column=2, sticky="w")

            if weapon == "fusion_blaster" and fusion_blaster_amount < 100:
                fusion_blaster_amount += n
                fusion_blaster_amount_label.grid_forget()

                fusion_blaster_amount_label = Label(tau_a, text=f'{fusion_blaster_amount:02d}')
                fusion_blaster_amount_label.grid(row=3, column=2, sticky="w")

            if weapon == "missile_pod" and missile_pod_amount < 100:
                missile_pod_amount += n
                missile_pod_amount_label.grid_forget()

                missile_pod_amount_label = Label(tau_a, text=f'{missile_pod_amount:02d}')
                missile_pod_amount_label.grid(row=4, column=2, sticky="w")

            if weapon == "smart_missile" and smart_missile_amount < 100:
                smart_missile_amount += n
                smart_missile_amount_label.grid_forget()

                smart_missile_amount_label = Label(tau_a, text=f'{smart_missile_amount:02d}')
                smart_missile_amount_label.grid(row=5, column=2, sticky="w")
                # print(smart_missile_amount)

            if weapon == "heavy_burst_cannon" and heavy_burst_cannon_amount < 100:
                heavy_burst_cannon_amount += n
                heavy_burst_cannon_amount_label.grid_forget()

                heavy_burst_cannon_amount_label = Label(tau_a, text=f'{heavy_burst_cannon_amount:02d}')
                heavy_burst_cannon_amount_label.grid(row=6, column=2, sticky="w")
                # print(heavy_burst_cannon_amount)


def sub_shot(army, weapon, n):
    if army == "marines":
        global bolter_amount
        global plasma_amount
        global melta_amount
        global flamer_amount
        global grav_cannon_amount
        global lasscannon_amount

        global bolter_amount_label
        global plasma_amount_label
        global melta_amount_label
        global flamer_amount_label
        global grav_cannon_amount_label
        global lasscannon_amount_label

        if weapon == "bolter" and bolter_amount > n:
            bolter_amount -= n
            bolter_amount_label.grid_forget()
            bolter_amount_label = Label(marines_a, text=f'{bolter_amount:02d}')
            bolter_amount_label.grid(row=1, column=2, sticky="w")
            print(bolter_amount)

        if weapon == "plasma" and plasma_amount > n:
            plasma_amount -= n
            plasma_amount_label.grid_forget()
            plasma_amount_label = Label(marines_a, text=f'{plasma_amount:02d}')
            plasma_amount_label.grid(row=2, column=2, sticky="w")
            print(plasma_amount)

        if weapon == "melta" and melta_amount > n:
            melta_amount -= n
            melta_amount_label.grid_forget()
            melta_amount_label = Label(marines_a, text=f'{melta_amount:02d}')
            melta_amount_label.grid(row=3, column=2, sticky="w")
            print(melta_amount)
        if weapon == "flamer" and flamer_amount > n:
            flamer_amount -= n
            flamer_amount_label.grid_forget()
            flamer_amount_label = Label(marines_a, text=f'{flamer_amount:02d}')
            flamer_amount_label.grid(row=4, column=2, sticky="w")
            print(flamer_amount)

        if weapon == "grav_cannon" and grav_cannon_amount > n:
            grav_cannon_amount -= n
            grav_cannon_amount_label.grid_forget()
            grav_cannon_amount_label = Label(marines_a, text=f'{grav_cannon_amount:02d}')
            grav_cannon_amount_label.grid(row=5, column=2, sticky="w")
            print(grav_cannon_amount)

        if weapon == "lasscannon" and lasscannon_amount > n:
            lasscannon_amount -= n
            lasscannon_amount_label.grid_forget()
            lasscannon_amount_label = Label(marines_a, text=f'{lasscannon_amount:02d}')
            lasscannon_amount_label.grid(row=6, column=2, sticky="w")
            print(lasscannon_amount)

    if army == "tau":

        global pulse_rifle_amount
        global plasma_rifle_amount
        global fusion_blaster_amount
        global missile_pod_amount
        global smart_missile_amount
        global heavy_burst_cannon_amount

        global pulse_rifle_amount_label
        global plasma_rifle_amount_label
        global fusion_blaster_amount_label
        global missile_pod_amount_label
        global smart_missile_amount_label
        global heavy_burst_cannon_amount_label

        if weapon == "pulse_rifle" and pulse_rifle_amount > n:
            pulse_rifle_amount -= n
            pulse_rifle_amount_label.grid_forget()
            pulse_rifle_amount_label = Label(tau_a, text=f'{pulse_rifle_amount:02d}')
            pulse_rifle_amount_label.grid(row=1, column=2, sticky="w")
            print(pulse_rifle_amount)

        if weapon == "plasma_rifle" and plasma_rifle_amount > n:
            plasma_rifle_amount -= n
            plasma_rifle_amount_label.grid_forget()
            plasma_rifle_amount_label = Label(tau_a, text=f'{plasma_rifle_amount:02d}')
            plasma_rifle_amount_label.grid(row=2, column=2, sticky="w")
            print(plasma_rifle_amount)

        if weapon == "fusion_blaster" and fusion_blaster_amount > n:
            fusion_blaster_amount -= n
            fusion_blaster_amount_label.grid_forget()
            fusion_blaster_amount_label = Label(tau_a, text=f'{fusion_blaster_amount:02d}')
            fusion_blaster_amount_label.grid(row=3, column=2, sticky="w")
            print(fusion_blaster_amount)

        if weapon == "missile_pod" and missile_pod_amount > n:
            missile_pod_amount -= n
            missile_pod_amount_label.grid_forget()
            missile_pod_amount_label = Label(tau_a, text=f'{missile_pod_amount:02d}')
            missile_pod_amount_label.grid(row=4, column=2, sticky="w")
            print(missile_pod_amount)

        if weapon == "smart_missile" and smart_missile_amount > n:
            smart_missile_amount -= n
            smart_missile_amount_label.grid_forget()
            smart_missile_amount_label = Label(tau_a, text=f'{smart_missile_amount:02d}')
            smart_missile_amount_label.grid(row=5, column=2, sticky="w")
            print(smart_missile_amount)

        if weapon == "heavy_burst_cannon" and heavy_burst_cannon_amount > n:
            heavy_burst_cannon_amount -= n
            heavy_burst_cannon_amount_label.grid_forget()
            heavy_burst_cannon_amount_label = Label(tau_a, text=f'{heavy_burst_cannon_amount:02d}')
            heavy_burst_cannon_amount_label.grid(row=6, column=2, sticky="w")
            print(heavy_burst_cannon_amount)


shooting_dict = {}
shooting_list = []
previous_army = None


# Task:
# def make_list_of_shots(name, amount, gun):
#     global shooting_list
#     global shooting_dict
#     global previous_army
#
#     if not previous_army:
#         previous_army = name
#
#     elif previous_army == name:
#
#         shooting_dict[f"{gun}"] = amount
#
#         shooting_list.append(gun)
#
#     if gun in marines_armory:
#         print("ok")
#         shooting_list.append(gun, amount)
#         print(shooting_list)
#     if gun in tau_armory:
#         shooting_list.append((gun, amount))
#         print(shooting_list)


#
#
# def do_math(list_of_weapons_tuple, target):
#     pass

def update_target():
    # set the cajlito_army to the passed value
    current_target = Label(window, text=f"targeting at {target.get()}")
    current_target.grid(row=5, column=2)
    print(target.get())


# def display_shooting_weapons(amount, weapon, on):
#     """
#     this will recive a lis of all all_equipments active
#     :param amount:
#     :param weapon:
#     :param on:
#     :return:
#     """
#
#     if on:
#         # print the shooting in a label at the window
#         eval(f'Label(window, cajlito_army="{amount} {weapon}").grid(sticky="W")')
#
#     else:
#         eval(f'display_{weapon}.grid_forget')


# def undisplay_shooting_weapons(amount,weapon):
#     global display_weapon
# §
#     #print the shooting in a label at the window


# WIDGETS:

# buttons and label

# MARINES

# buttons in tab_ marines:['bolter', 'plasma', 'melta', 'flamer', 'grav cannon' 'lasscannon']
bolter_box = Checkbutton(marines_a, text="Bolter", variable=bolter_shooting, onvalue="True", offvalue="False",
                         command=marines_enable_buttons)
bolter_box.deselect()
bolter_box.grid(row=1, column=0, sticky="w")
plasma_box = Checkbutton(marines_a, text="plasma", variable=plasma_shooting, onvalue="True", offvalue="False",
                         command=marines_enable_buttons)
plasma_box.deselect()
plasma_box.grid(row=2, column=0, sticky="w")
melta_box = Checkbutton(marines_a, text="melta", variable=melta_shooting, onvalue="True", offvalue="False",
                        command=marines_enable_buttons)
melta_box.deselect()
melta_box.grid(row=3, column=0, sticky="w")
flamer_box = Checkbutton(marines_a, text="flamer", variable=flamer_shooting, onvalue="True", offvalue="False",
                         command=marines_enable_buttons)
flamer_box.deselect()
flamer_box.grid(row=4, column=0, sticky="w")
grav_cannon_box = Checkbutton(marines_a, text="grav cannon", variable=grav_cannon_shooting, onvalue="True",
                              offvalue="False", command=marines_enable_buttons)
grav_cannon_box.deselect()
grav_cannon_box.grid(row=5, column=0, sticky="w")
lasscannon_box = Checkbutton(marines_a, text="lasscannon", variable=lasscannon_shooting, onvalue="True",
                             offvalue="False", command=marines_enable_buttons)
lasscannon_box.deselect()
lasscannon_box.grid(row=6, column=0, sticky="w")
# radio b for marines units as target:['tactical', "intercessor", "terminator", "centurion", "predator", "landraider"]
tactical = Radiobutton(marines_d, text="tactical", variable=target, value='tactical', command=update_target)
tactical.grid(row=0, sticky="w")
intercessor = Radiobutton(marines_d, text="intercessor", variable=target, value='intercessor',
                          command=update_target)
intercessor.grid(row=1, sticky="w")
terminator = Radiobutton(marines_d, text="terminator", variable=target, value='terminator', command=update_target)
terminator.grid(row=2, sticky="w")
centurions = Radiobutton(marines_d, text="centurions", variable=target, value='centurion', command=update_target)
centurions.grid(row=3, sticky="w")
predator = Radiobutton(marines_d, text="predator", variable=target, value='predator', command=update_target)
predator.grid(row=4, sticky="w")
landraider = Radiobutton(marines_d, text="landraider", variable=target, value='landraider', command=update_target)
landraider.grid(row=5, sticky="w")
# TU
# buttons in tab_ Tau:[plasma rifle', 'pulse rifle', 'fusion blaster', 'missile pod','smart missiles', 'Heavy burst
# cannon']
pulse_rifle_box = Checkbutton(tau_a, text="pulse rifle", variable=pulse_rifle_shooting, onvalue="True",
                              offvalue="False", command=tau_enable_buttons)
pulse_rifle_box.deselect()
pulse_rifle_box.grid(row=1, column=0, sticky="w")
plasma_rifle_box = Checkbutton(tau_a, text="plasma rifle", variable=plasma_rifle_shooting, onvalue="True",
                               offvalue="False", command=tau_enable_buttons)
plasma_rifle_box.deselect()
plasma_rifle_box.grid(row=2, column=0, sticky="w")
fusion_blaster_box = Checkbutton(tau_a, text="fusion blaster", variable=fusion_blaster_shooting, onvalue="True",
                                 offvalue="False", command=tau_enable_buttons)
fusion_blaster_box.deselect()
fusion_blaster_box.grid(row=3, column=0, sticky="w")
missile_pod_box = Checkbutton(tau_a, text="missile pod", variable=missile_pod_shooting, onvalue="True",
                              offvalue="False", command=tau_enable_buttons)
missile_pod_box.deselect()
missile_pod_box.grid(row=4, column=0, sticky="w")
smart_missiles_box = Checkbutton(tau_a, text="smart missiles", variable=smart_missiles_shooting, onvalue="True",
                                 offvalue="False", command=tau_enable_buttons)
smart_missiles_box.deselect()
smart_missiles_box.grid(row=5, column=0, sticky="w")
heavy_burst_cannon_box = Checkbutton(tau_a, text="Heavy burst cannon", variable=heavy_burst_cannon_shooting,
                                     onvalue="True", offvalue="False", command=tau_enable_buttons)
heavy_burst_cannon_box.deselect()
heavy_burst_cannon_box.grid(row=6, column=0, sticky="w")
# tau units
fire_warrior = Radiobutton(tau_d, text="fire warrior", variable=target, value='fire warrior', command=update_target)
fire_warrior.grid(row=0, sticky="w")
shield_drone = Radiobutton(tau_d, text="shield drone", variable=target, value='shield drone', command=update_target)
shield_drone.grid(row=1, sticky="w")
stealh_suit = Radiobutton(tau_d, text="stealh suit", variable=target, value='stealh suit', command=update_target)
stealh_suit.grid(row=2, sticky="w")
crisis = Radiobutton(tau_d, text="crisis", variable=target, value='crisis', command=update_target)
crisis.grid(row=3, sticky="w")
broadside = Radiobutton(tau_d, text="broadside", variable=target, value='broadside', command=update_target)
broadside.grid(row=4, sticky="w")
riptide = Radiobutton(tau_d, text="riptide", variable=target, value='riptide', command=update_target)
riptide.grid(row=5, sticky="w")
# TRANIDS
# TYRANIDS:
# spinefists, deathspitter, impaler cannon, shock cannon, brainleech devourer, Hheavy venom cannon
spinefists_box = Checkbutton(tyranids, text="spinefists", variable=spinefists_shooting, onvalue="True",
                             offvalue="False", command=tyranids_enable_button)
spinefists_box.deselect()
spinefists_box.grid(row=1, column=0, sticky="w")
deathspitter_box = Checkbutton(tyranids, text="deathspitter", variable=deathspitter_shooting, onvalue="True",
                               offvalue="False", command=tyranids_enable_button)
deathspitter_box.deselect()
deathspitter_box.grid(row=2, column=0, sticky="w")
impaler_cannon_box = Checkbutton(tyranids, text="impaler_cannon", variable=impaler_cannon_shooting, onvalue="True",
                                 offvalue="False", command=tyranids_enable_button)
impaler_cannon_box.deselect()
impaler_cannon_box.grid(row=3, column=0, sticky="w")
shock_cannon_box = Checkbutton(tyranids, text="shock_cannon", variable=shock_cannon_shooting, onvalue="True",
                               offvalue="False", command=tyranids_enable_button)
shock_cannon_box.deselect()
shock_cannon_box.grid(row=4, column=0, sticky="w")
brainleech_devourer_box = Checkbutton(tyranids, text="brainleech_devourer", variable=brainleech_devourer_shooting,
                                      onvalue="True", offvalue="False", command=tyranids_enable_button)
brainleech_devourer_box.deselect()
brainleech_devourer_box.grid(row=5, column=0, sticky="w")
heavy_venom_cannon_box = Checkbutton(tyranids, text="heavy_venom_cannon", variable=heavy_venom_cannon_shooting,
                                     onvalue="True", offvalue="False", command=tyranids_enable_button)
heavy_venom_cannon_box.deselect()
heavy_venom_cannon_box.grid(row=6, column=0, sticky="w")
# radio b for tyranids def: ["reaper swarm", "gaunts", "warrior", "exocrine", "carnifex", "trygon"]
reaper_swarm = Radiobutton(tyranids_d, text="reaper swarm", variable=target, value='reaper swarm',
                           command=update_target)
reaper_swarm.grid(row=0, sticky="w")
gaunts = Radiobutton(tyranids_d, text="gaunts", variable=target, value='gaunts', command=update_target)
gaunts.grid(row=1, sticky="w")
warriors = Radiobutton(tyranids_d, text="warriors", variable=target, value='warriors', command=update_target)
warriors.grid(row=2, sticky="w")
exocrine = Radiobutton(tyranids_d, text="exocrine", variable=target, value='exocrine', command=update_target)
exocrine.grid(row=3, sticky="w")
carnifex = Radiobutton(tyranids_d, text="carnifex", variable=target, value='carnifex', command=update_target)
carnifex.grid(row=4, sticky="w")
trygon = Radiobutton(tyranids_d, text="trygon", variable=target, value='trygon', command=update_target)
trygon.grid(row=5, sticky="w")

# bolter
bolter_sub_button = Button(marines_a, text="-", width=button_x, state=DISABLED)
bolter_sub_button.grid(row=1, column=1, sticky="w")
bolter_amount_label = Label(marines_a, text=f'{bolter_amount:02d}', state=DISABLED)
bolter_amount_label.grid(row=1, column=2, sticky="w")
bolter_add_button = Button(marines_a, text="+", width=button_x, state=DISABLED)
bolter_add_button.grid(row=1, column=3, sticky="w")
bolter_sub10_button = Button(marines_a, text="-10", width=button_x, state=DISABLED)
bolter_sub10_button.grid(row=1, column=4, padx=5, sticky="w")
bolter_add10_button = Button(marines_a, text="+10", width=button_x, state=DISABLED)
bolter_add10_button.grid(row=1, column=5, sticky="w")
# plasma
plasma_sub_button = Button(marines_a, text="+", width=button_x, state=DISABLED)
plasma_sub_button.grid(row=2, column=3, sticky="w")
plasma_amount_label = Label(marines_a, text=f'{plasma_amount:02d}', state=DISABLED)
plasma_amount_label.grid(row=2, column=2, sticky="w")
plasma_add_button = Button(marines_a, text="-", width=button_x, state=DISABLED)
plasma_add_button.grid(row=2, column=1, sticky="w")
plasma_sub10_button = Button(marines_a, text="-10", width=button_x, state=DISABLED)
plasma_sub10_button.grid(row=2, column=4, padx=5, sticky="w")
plasma_add10_button = Button(marines_a, text="+10", width=button_x, state=DISABLED)
plasma_add10_button.grid(row=2, column=5, sticky="w")
# melta
melta_sub_button = Button(marines_a, text="+", width=button_x, state=DISABLED)
melta_sub_button.grid(row=3, column=3, sticky="w")
melta_amount_label = Label(marines_a, text=f'{melta_amount:02d}', state=DISABLED)
melta_amount_label.grid(row=3, column=2, sticky="w")
melta_add_button = Button(marines_a, text="-", width=button_x, state=DISABLED)
melta_add_button.grid(row=3, column=1, sticky="w")
melta_sub10_button = Button(marines_a, text="-10", width=button_x, state=DISABLED)
melta_sub10_button.grid(row=3, column=4, padx=5, sticky="w")
melta_add10_button = Button(marines_a, text="+10", width=button_x, state=DISABLED)
melta_add10_button.grid(row=3, column=5, sticky="w")
# flamer
flamer_sub_button = Button(marines_a, text="+", width=button_x, state=DISABLED)
flamer_sub_button.grid(row=4, column=3, sticky="w")
flamer_amount_label = Label(marines_a, text=f'{flamer_amount:02d}', state=DISABLED)
flamer_amount_label.grid(row=4, column=2, sticky="w")
flamer_add_button = Button(marines_a, text="-", width=button_x, state=DISABLED)
flamer_add_button.grid(row=4, column=1, sticky="w")
flamer_sub10_button = Button(marines_a, text="-10", width=button_x, state=DISABLED)
flamer_sub10_button.grid(row=4, column=4, padx=5, sticky="w")
flamer_add10_button = Button(marines_a, text="+10", width=button_x, state=DISABLED)
flamer_add10_button.grid(row=4, column=5, sticky="w")
# grav_cannon
grav_cannon_sub_button = Button(marines_a, text="+", width=button_x, state=DISABLED)
grav_cannon_sub_button.grid(row=5, column=3, sticky="w")
grav_cannon_amount_label = Label(marines_a, text=f'{grav_cannon_amount:02d}', state=DISABLED)
grav_cannon_amount_label.grid(row=5, column=2, sticky="w")
grav_cannon_add_button = Button(marines_a, text="-", width=button_x, state=DISABLED)
grav_cannon_add_button.grid(row=5, column=1, sticky="w")
grav_cannon_sub10_button = Button(marines_a, text="-10", width=button_x, state=DISABLED)
grav_cannon_sub10_button.grid(row=5, column=4, padx=5, sticky="w")
grav_cannon_add10_button = Button(marines_a, text="+10", width=button_x, state=DISABLED)
grav_cannon_add10_button.grid(row=5, column=5, sticky="W")
# lasscannon
lasscannon_sub_button = Button(marines_a, text="+", width=button_x, state=DISABLED)
lasscannon_sub_button.grid(row=6, column=3, sticky="W")
lasscannon_amount_label = Label(marines_a, text=f'{lasscannon_amount:02d}', state=DISABLED)
lasscannon_amount_label.grid(row=6, column=2, sticky="W")
lasscannon_add_button = Button(marines_a, text="-", width=button_x, state=DISABLED)
lasscannon_add_button.grid(row=6, column=1, sticky="W")
lasscannon_sub10_button = Button(marines_a, text="-10", width=button_x, state=DISABLED)
lasscannon_sub10_button.grid(row=6, column=4, padx=5, sticky="EW")
lasscannon_add10_button = Button(marines_a, text="+10", width=button_x, state=DISABLED)
lasscannon_add10_button.grid(row=6, column=5, sticky="W")
pulse_rifle_sub_button = Button(tau_a, text="-", width=button_x, state=DISABLED)
pulse_rifle_sub_button.grid(row=1, column=1, sticky="w")
pulse_rifle_amount_label = Label(tau_a, text=f'{bolter_amount:02d}', state=DISABLED)
pulse_rifle_amount_label.grid(row=1, column=2, sticky="w")
pulse_rifle_add_button = Button(tau_a, text="+", width=button_x, state=DISABLED)
pulse_rifle_add_button.grid(row=1, column=3, sticky="w")
pulse_rifle_sub10_button = Button(tau_a, text="-10", width=button_x, state=DISABLED)
pulse_rifle_sub10_button.grid(row=1, column=4, padx=5, sticky="w")
pulse_rifle_add10_button = Button(tau_a, text="+10", width=button_x, state=DISABLED)
pulse_rifle_add10_button.grid(row=1, column=5, sticky="w")
plasma_rifle_sub_button = Button(tau_a, text="-", width=button_x, state=DISABLED)
plasma_rifle_sub_button.grid(row=2, column=1, sticky="w")
plasma_rifle_amount_label = Label(tau_a, text=f'{bolter_amount:02d}', state=DISABLED)
plasma_rifle_amount_label.grid(row=2, column=2, sticky="w")
plasma_rifle_add_button = Button(tau_a, text="+", width=button_x, state=DISABLED)
plasma_rifle_add_button.grid(row=2, column=3, sticky="w")
plasma_rifle_sub10_button = Button(tau_a, text="-10", width=button_x, state=DISABLED)
plasma_rifle_sub10_button.grid(row=2, column=4, padx=5, sticky="w")
plasma_rifle_add10_button = Button(tau_a, text="+10", width=button_x, state=DISABLED)
plasma_rifle_add10_button.grid(row=2, column=5, sticky="w")
fusion_blaster_sub_button = Button(tau_a, text="-", width=button_x, state=DISABLED)
fusion_blaster_sub_button.grid(row=3, column=1, sticky="w")
fusion_blaster_amount_label = Label(tau_a, text=f'{bolter_amount:02d}', state=DISABLED)
fusion_blaster_amount_label.grid(row=3, column=2, sticky="w")
fusion_blaster_add_button = Button(tau_a, text="+", width=button_x, state=DISABLED)
fusion_blaster_add_button.grid(row=3, column=3, sticky="w")
fusion_blaster_sub10_button = Button(tau_a, text="-10", width=button_x, state=DISABLED)
fusion_blaster_sub10_button.grid(row=3, column=4, padx=5, sticky="w")
fusion_blaster_add10_button = Button(tau_a, text="+10", width=button_x, state=DISABLED)
fusion_blaster_add10_button.grid(row=3, column=5, sticky="w")
missile_pod_sub_button = Button(tau_a, text="-", width=button_x, state=DISABLED)
missile_pod_sub_button.grid(row=4, column=1, sticky="w")
missile_pod_amount_label = Label(tau_a, text=f'{bolter_amount:02d}', state=DISABLED)
missile_pod_amount_label.grid(row=4, column=2, sticky="w")
missile_pod_add_button = Button(tau_a, text="+", width=button_x, state=DISABLED)
missile_pod_add_button.grid(row=4, column=3, sticky="w")
missile_pod_sub10_button = Button(tau_a, text="-10", width=button_x, state=DISABLED)
missile_pod_sub10_button.grid(row=4, column=4, padx=5, sticky="w")
missile_pod_add10_button = Button(tau_a, text="+10", width=button_x, state=DISABLED)
missile_pod_add10_button.grid(row=4, column=5, sticky="w")
smart_missiles_sub_button = Button(tau_a, text="-", width=button_x, state=DISABLED)
smart_missiles_sub_button.grid(row=5, column=1, sticky="w")
smart_missiles_amount_label = Label(tau_a, text=f'{bolter_amount:02d}', state=DISABLED)
smart_missiles_amount_label.grid(row=5, column=2, sticky="w")
smart_missiles_add_button = Button(tau_a, text="+", width=button_x, state=DISABLED)
smart_missiles_add_button.grid(row=5, column=3, sticky="w")
smart_missiles_sub10_button = Button(tau_a, text="-10", width=button_x, state=DISABLED)
smart_missiles_sub10_button.grid(row=5, column=4, padx=5, sticky="w")
smart_missiles_add10_button = Button(tau_a, text="+10", width=button_x, state=DISABLED)
smart_missiles_add10_button.grid(row=5, column=5, sticky="w")
heavy_burst_cannon_sub_button = Button(tau_a, text="-", width=button_x, state=DISABLED)
heavy_burst_cannon_sub_button.grid(row=6, column=1, sticky="w")
heavy_burst_cannon_amount_label = Label(tau_a, text=f'{bolter_amount:02d}', state=DISABLED)
heavy_burst_cannon_amount_label.grid(row=6, column=2, sticky="w")
heavy_burst_cannon_add_button = Button(tau_a, text="+", width=button_x, state=DISABLED)
heavy_burst_cannon_add_button.grid(row=6, column=3, sticky="w")
heavy_burst_cannon_sub10_button = Button(tau_a, text="-10", width=button_x, state=DISABLED)
heavy_burst_cannon_sub10_button.grid(row=6, column=4, padx=5, sticky="w")
heavy_burst_cannon_add10_button = Button(tau_a, text="+10", width=button_x, state=DISABLED)
heavy_burst_cannon_add10_button.grid(row=6, column=5, sticky="w")

window.mainloop()
