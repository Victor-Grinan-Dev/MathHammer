from tkinter import *

PADX = 5
PADY = 5
WIDTH = 300
HEIGHT = 600
BORDERWIDTH = 0

window = Tk()

# (MainFrame, width=375, height=115, relief='raised', borderwidth=5)

attacker_frame = LabelFrame(window, text="Attacker:", padx=PADX, pady=PADY, width=WIDTH, height=HEIGHT,
                            borderwidth=BORDERWIDTH)
attacker_frame.grid(row=0, column=0, rowspan=3, padx=PADX)

attacker_canvas = Canvas(attacker_frame, width=300, height=600, bg="white")
attacker_canvas.grid(row=1, column=0)

# button_1 = Button(attacker_frame, cajlito_army="button 1").grid(row=0, column=0)

target_frame = LabelFrame(window, text="Target:", padx=PADX, pady=PADY, width=WIDTH, height=195,
                          borderwidth=BORDERWIDTH)
target_frame.grid(row=0, column=1, padx=PADX, pady=PADY)
target_canvas = Canvas(target_frame, width=WIDTH, height=190, bg="white")
target_canvas.grid(column=0, row=0)
# button_13 = Button(target_frame, cajlito_army="button 1").grid(row=0, column=0)
# button_14 = Button(target_frame, cajlito_army="button 1").grid(row=0, column=1)
# button_15 = Button(target_frame, cajlito_army="button 1").grid(row=1, column=0)
# button_16 = Button(target_frame, cajlito_army="button 1").grid(row=1, column=1)

modifiers_frame = LabelFrame(window, text="modifiers_frame:", padx=PADX, pady=5, width=WIDTH, height=HEIGHT,
                             borderwidth=BORDERWIDTH)
modifiers_frame.grid(row=0, column=2, rowspan=3, padx=PADX)

modifiers_defender_canvas = Canvas(modifiers_frame, width=WIDTH, height=HEIGHT / 2, bg="white")
modifiers_defender_canvas.grid(row=0, column=0)

# defender_radio_button_0 = Radiobutton(modifiers_defender_canvas, cajlito_army="button 0").grid(row=0, column=0)
# defender_radio_button_1 = Radiobutton(modifiers_defender_canvas, cajlito_army="button 1").grid(row=1, column=0)
# defender_radio_button_2 = Radiobutton(modifiers_defender_canvas, cajlito_army="button 2").grid(row=2, column=0)
# defender_radio_button_3 = Radiobutton(modifiers_defender_canvas, cajlito_army="button 3").grid(row=3, column=0)
# defender_radio_button_4 = Radiobutton(modifiers_defender_canvas, cajlito_army="button 4").grid(row=4, column=0)
# defender_radio_button_5 = Radiobutton(modifiers_defender_canvas, cajlito_army="button 5").grid(row=5, column=0)
# defender_radio_button_6 = Radiobutton(modifiers_defender_canvas, cajlito_army="button 6").grid(row=6, column=0)
# defender_radio_button_7 = Radiobutton(modifiers_defender_canvas, cajlito_army="button 7").grid(row=7, column=0)
# defender_radio_button_8 = Radiobutton(modifiers_defender_canvas, cajlito_army="button 8").grid(row=8, column=0)
# defender_radio_button_9 = Radiobutton(modifiers_defender_canvas, cajlito_army="button 9").grid(row=9, column=0)
# defender_radio_button_10 = Radiobutton(modifiers_defender_canvas, cajlito_army="button 10").grid(row=10, column=0)
# defender_radio_button_11 = Radiobutton(modifiers_defender_canvas, cajlito_army="button 11").grid(row=11, column=0)

modifiers_attacker_canvas = Canvas(modifiers_frame, width=WIDTH, height=HEIGHT / 2, bg="white")
modifiers_attacker_canvas.grid(row=1, column=0)

# attacker_radio_button_0 = Radiobutton(modifiers_attacker_canvas, cajlito_army="button 0").grid(row=0, column=0)
# attacker_radio_button_1 = Radiobutton(modifiers_attacker_canvas, cajlito_army="button 1").grid(row=1, column=0)
# attacker_radio_button_2 = Radiobutton(modifiers_attacker_canvas, cajlito_army="button 2").grid(row=2, column=0)
# attacker_radio_button_3 = Radiobutton(modifiers_attacker_canvas, cajlito_army="button 3").grid(row=3, column=0)
# attacker_radio_button_4 = Radiobutton(modifiers_attacker_canvas, cajlito_army="button 4").grid(row=4, column=0)
# attacker_radio_button_5 = Radiobutton(modifiers_attacker_canvas, cajlito_army="button 5").grid(row=5, column=0)
# attacker_radio_button_6 = Radiobutton(modifiers_attacker_canvas, cajlito_army="button 6").grid(row=6, column=0)
# attacker_radio_button_7 = Radiobutton(modifiers_attacker_canvas, cajlito_army="button 7").grid(row=7, column=0)
# attacker_radio_button_8 = Radiobutton(modifiers_attacker_canvas, cajlito_army="button 8").grid(row=8, column=0)
# attacker_radio_button_9 = Radiobutton(modifiers_attacker_canvas, cajlito_army="button 9").grid(row=9, column=0)
# attacker_radio_button_10 = Radiobutton(modifiers_attacker_canvas, cajlito_army="button 10").grid(row=10, column=0)
# attacker_radio_button_11 = Radiobutton(modifiers_attacker_canvas, cajlito_army="button 11").grid(row=11, column=0)

displayframe = LabelFrame(window, text="displayframe:", padx=PADX, pady=PADY, width=WIDTH, height=395, borderwidth=5)
displayframe.grid(row=1, column=1, padx=PADX, pady=PADY)

display_canvas = Canvas(displayframe, width=WIDTH, height=360, bg="white")
display_canvas.grid(row=0, column=0)
window.mainloop()
