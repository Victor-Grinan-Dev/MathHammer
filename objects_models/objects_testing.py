from objects_models.little_db import *
from objects_models.a_model import Model

# from objects_models.a_unit import Unit
# from objects_models.a_formation_patrol import FormationPatrol as Patrol

# SPACE MARINES

captain = Model("Thelonius", "hq", "2", "2", "4", "3", "6")
captain.add_equipment(thunder_hammer)
captain.equip_main_hand_weapon(thunder_hammer)
captain.add_equipment(storm_shield)
captain.equip_secondary_hand_weapon(storm_shield)
captain.add_side_weapon(bolt_pistol)

print(captain)

# sgt = Model("sgt", 3, 4, 3, 1)
# sgt.other_equipments = [storm_bolter, bolt_pistol]
# marine1 = Model("marine 1", 3, 4, 3, 1)
# marine1.other_equipments = [boltgun, bolt_pistol]
# marine2 = Model("marine 2", 3, 4, 3, 1)
# marine2.other_equipments = [boltgun, bolt_pistol]
# marine3 = Model("marine 3", 3, 4, 3, 1)
# marine3.other_equipments = [boltgun, bolt_pistol]
# marine_specialist = Model("marine 3", 3, 4, 3, 1, )
# marine_specialist.other_equipments = [flamer, bolt_pistol]
#
# whirlwind = Model("liberatus whirlwind", 3, 7, 3, 11)
# whirlwind.other_equipments = [storm_bolter, vengance_laucher]
#
# sgt_cent_dev = Model("sgt", 3, 5, 2, 4)
# sgt_cent_dev.other_equipments = [hurricane_bolter, grav_cannon]
# cent_dev1 = Model("cent_dev1", 3, 5, 2, 4)
# cent_dev1.other_equipments = [hurricane_bolter, grav_cannon]
# cent_dev2 = Model("cent_dev2", 3, 5, 2, 4)
# cent_dev2.other_equipments = [hurricane_bolter, grav_cannon]

# thelonius = Unit([captain], "hq")
# alfa = [sgt, marine1, marine2, marine3, marine_specialist]
# alfa_squad = Unit(alfa, "troops", "Alfa")
# cent_dev_list = [sgt_cent_dev, cent_dev1, cent_dev2]
# fist_of_doom = Unit(cent_dev_list, "heavy support", "fist of doom")
# liberatus = Unit([whirlwind], "heavy support", "liberatus")
#
# marines_formation = Patrol("emperor's finest", thelonius, alfa_squad, heavy_1=liberatus, heavy_2=fist_of_doom)

# # TAU EMPIRE
# pulse_rifle = Weapon("pulse rifle", 1, 5, 0, 1, ["rapid fire: if target distance < weapon_range/2: attacks = 2"])
# heavy_burst_cannon = Weapon("heavy burst cannon", 12, 6, 1, 2, ["nova reactor: if nova_charged: self.attacks = 18"])
# cycling_ion_blaster = Weapon("cycling ion blaster", 4, 7, 1, "d3", ["overcharge: if overcharge: self.D = d3,"
#                                                                     " self.w_str = 8"])
# fusion_blaster = Weapon("fusion blasster", 1, 8, 4, "d6+1")
# # missile_pod = Weapon("missile pods", 4)

# shield = Equipment("shield", ["inv: 5"])
# ion_shield = Equipment("ion shield", "inv: 4")
#
# tau_armoury = (pulse_rifle, heavy_burst_cannon, cycling_ion_blaster)
#
# enforcerrer_commander = Model("hq", 2, 5, 2, 6)
# enforcerrer_commander.other_equipments = [cycling_ion_blaster, cycling_ion_blaster, cycling_ion_blaster,
#                                                  cycling_ion_blaster]
#
# cold_star_commander = Model("hq", 2, 5, 2, 6)
# cold_star_commander.other_equipments = [fusion_blaster, fusion_blaster, fusion_blaster, ion_shield]
#
# shasui = Model("sha'sui", 4, 3, 4, 1)
# shasui.other_equipments = [pulse_rifle]
# fire_warrior_1 = Model("fire warrior", 4, 3, 4, 1)
# fire_warrior_1.other_equipments = [pulse_rifle]
# fire_warrior_2 = Model("fire warrior", 4, 3, 4, 1)
# fire_warrior_2.other_equipments = [pulse_rifle]
# fire_warrior_3 = Model("fire warrior", 4, 3, 4, 1)
# fire_warrior_3.other_equipments = [pulse_rifle]
# fire_warrior_4 = Model("fire warrior", 4, 3, 4, 1)
# fire_warrior_4.other_equipments = [pulse_rifle]
# fire_warrior_5 = Model("fire warrior", 4, 3, 4, 1)
# fire_warrior_5.other_equipments = [pulse_rifle]
# fire_warrior_6 = Model("fire warrior", 4, 3, 4, 1)
# fire_warrior_6.other_equipments = [pulse_rifle]
# fire_warrior_7 = Model("fire warrior", 4, 3, 4, 1)
# fire_warrior_7.other_equipments = [pulse_rifle]
# fire_warrior_8 = Model("fire warrior", 4, 3, 4, 1)
# fire_warrior_8.other_equipments = [pulse_rifle]
# fire_warrior_9 = Model("fire warrior", 4, 3, 4, 1)
# fire_warrior_9.other_equipments = [pulse_rifle]

# fire_warriors_list = [shasui, fire_warrior_1, fire_warrior_2, fire_warrior_3, fire_warrior_4, fire_warrior_5,
#                       fire_warrior_6, fire_warrior_7, fire_warrior_8, fire_warrior_9]

# riptide = Model("elite", 4, 6, 2, 16, [heavy_burst_cannon, shield])
#
#
# enforcerrer_commander_unit = Unit([enforcerrer_commander], "hq")
# cold_star_commander_unit = Unit([cold_star_commander], "hq")
# fire_warriors_unit = Unit(fire_warriors_list, "troops")
# riptide_unit = Unit([riptide], "elite")
#
# tau_formation = Patrol("fish faces", enforcerrer_commander_unit, fire_warriors_unit,
#                        second_hq=cold_star_commander_unit, elite_1=riptide_unit)

# print(captain.main_hand_weapon)
#
# captain = Model("hq", 2, 4, 3, 6)
# captain.equip_main_weapon(thunder_hammer)
# captain.equip_second_hand(storm_shield)
# captain.add_extra_equipment(bolt_pistol)
# print(captain.main_hand_weapon)
# print(captain.second_hand)
# captain.display_equipments()
# print(captain.other_equipments)
