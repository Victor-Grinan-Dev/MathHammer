from objects_models.a_weapon import Weapon, MeleeWeapon
from objects_models.an_equipment import Equipment


class Model:
    # real_arguments = ["movement", "ballistic_skill", "weapon_skill", "strength", "toughness", "attacks", "wounds",
    #                   "leadership", "abilities", "other_equipments"]
    # for the moment arguments
    arguments = ["name", "roll", "Bs", "Ws", "T", "wounds", "save", "special_ability"]
    quote = ""
    HELP = """first add equipment, then you can equip them, then you can print them"""

    def __init__(self, name, unit_roll: str, Bs, Ws, T, save, wounds, special_ability: str = None):

        self.name = name
        self.unit_roll = unit_roll
        self.bs = Bs
        self.ws = Ws
        self.t = T
        self.save = save
        self.wounds = wounds
        self.ability = special_ability

        self.attributes = [self.name, self.unit_roll, self.bs, self.ws, self.t, self.wounds, self.save, self.ability]

        # equipment handling
        self.main_hand_weapon = None
        self.secondary_hand_weapon = None
        self.side_weapon = None
        self.other_equipments = []

        self.currently_equipped = None

        self.all_equipments = []

        # equip the first available option to equip
        for item in self.all_equipments:
            if not self.currently_equipped:
                self.currently_equipped = item

    def __repr__(self, heading=True):

        if heading:  # handles the heading
            index = 0
            for arg in self.arguments:
                if index == 0:
                    total_spaces = 20
                elif index == 2 or index == 3 or index == 4:
                    total_spaces = 4
                else:
                    total_spaces = 8
                blanks = total_spaces - len(arg)
                if arg:
                    self.quote += arg.upper() + (" " * blanks)
                index += 1
            self.quote += "\n"

        index = 0
        for att in self.attributes:
            if att:
                if index == 0:
                    total_spaces = 20
                elif index == 2 or index == 3 or index == 4:
                    total_spaces = 4
                else:
                    total_spaces = 8
                blanks = total_spaces - len(att)
                self.quote += att.title() + (" " * blanks)
            index += 1
        self.quote += "\n"

        x = list()

        for item in self.all_equipments:
            if item:
                x.append(item.__repr__())
        x = set(x)
        x = list(x)

        for item in x:
            if "NAME" in item:
                print(f"{item} yeah")

        for item in x:
            if item:
                self.quote += item

        # self.display_equipments()

        return self.quote

    def add_equipment(self, equipment):
        if equipment not in self.all_equipments:  # and available slots
            self.all_equipments.append(equipment)

    def equip_main_hand_weapon(self, weapon):
        if weapon in self.all_equipments:
            self.main_hand_weapon = weapon

    def equip_secondary_hand_weapon(self, weapon):
        if weapon in self.all_equipments:
            self.secondary_hand_weapon = weapon

    def swap_weapon(self, weapon):  # one hand
        self.currently_equipped = weapon

    def add_side_weapon(self, weapon):
        if weapon not in self.all_equipments:
            self.all_equipments.append(weapon)

    def display_equipments(self):
        index = 0
        last_index = len(self.other_equipments) - 1
        for item in self.all_equipments:
            if item:
                if index != last_index:
                    print(item.__repr__(), end="")
                else:
                    print(item.__repr__())
            else:
                print(item)

            index += 1


# dummy_db = []
if __name__ == '__main__':
    bolt_pistol = Weapon("bolt pistol", "12", "pistol", "1", "4", "0", "1", "pistol: if model_in_combat == True and "
                                                                            "shooting_Phase: range_attack(pistol)")
    storm_shield = Equipment("storm shield", "inv = 4/save += 1")
    thunder_hammer = MeleeWeapon("thunder hammer", "x2", "2", "3", "unwieldy: ws - 1")

    captain = Model("Thelonius", "hq", "2", "2", "4", "3", "6")
    captain.add_equipment(thunder_hammer)
    captain.equip_main_hand_weapon(thunder_hammer)
    captain.add_equipment(storm_shield)
    captain.equip_secondary_hand_weapon(storm_shield)
    captain.add_side_weapon(bolt_pistol)

    print(captain.HELP)
    print(captain)

    # bolt_pistol = Weapon("bolt pistol", 1, 4, 0, 1)
    # # boltgun = Weapon("boltgun", 1, 4, 0, 1, ["rapid fire: if target distance < weapon_range/2: attacks = 2"])
    # # flamer = Weapon("flamer", "d6", 4, 0, 1, ["auto hits"])
    # # storm_bolter = Weapon("storm bolter", 2, 4, 0, 1, ["rapid fire: if target distance < weapon_range/2: attacks = 2"])
    # # hurricane_bolter = Weapon("hurricane bolter", 6, 4, 0, 1, ["rapid fire: if target distance < weapon_range/2:"
    # #                                                            " attacks = 2"])
    # thunder_hammer = Weapon("thunder hammer", 4, 8, 2, 3)
    # # vengance_laucher = Weapon("vengance whirlwind", "2d3", 7, 1, 2)
    # # grav_cannon = Weapon("grav cannon", 4, 5, 3, 1, ["grav: if target.save <= 3: self.D = 2"])
    # #
    # storm_shield = Equipment("storm shiel", ["inv: 4", "save + 1"])
    # #
    # # marines_armoury = (bolt_pistol, boltgun, flamer, vengance_laucher, storm_shield)
    # #
    # # captain = Model("hq", 2, 4, 3, 6)
    # # captain.other_equipments = [thunder_hammer, storm_shield]
    # #
    # # sgt = Model("sgt", 3, 4, 3, 1)
    # # sgt.other_equipments = [storm_bolter, bolt_pistol]
    # # marine1 = Model("marine 1", 3, 4, 3, 1)
    # # marine1.other_equipments = [boltgun, bolt_pistol]
    # # marine2 = Model("marine 2", 3, 4, 3, 1)
    # # marine2.other_equipments = [boltgun, bolt_pistol]
    # # marine3 = Model("marine 3", 3, 4, 3, 1)
    # # marine3.other_equipments = [boltgun, bolt_pistol]
    # # marine_specialist = Model("marine 3", 3, 4, 3, 1, )
    # # marine_specialist.other_equipments = [flamer, bolt_pistol]
    # #
    # # whirlwind = Model("liberatus whirlwind", 3, 7, 3, 11)
    # # whirlwind.other_equipments = [storm_bolter, vengance_laucher]
    # #
    # # sgt_cent_dev = Model("sgt", 3, 5, 2, 4)
    # # sgt_cent_dev.other_equipments = [hurricane_bolter, grav_cannon]
    # # cent_dev1 = Model("cent_dev1", 3, 5, 2, 4)
    # # cent_dev1.other_equipments = [hurricane_bolter, grav_cannon]
    # # cent_dev2 = Model("cent_dev2", 3, 5, 2, 4)
    # # cent_dev2.other_equipments = [hurricane_bolter, grav_cannon]
    # #
    # # thelonius = Unit([captain], "hq")
    # # alfa = [sgt, marine1, marine2, marine3, marine_specialist]
    # # alfa_squad = Unit(alfa, "troops", "Alfa")
    # # cent_dev_list = [sgt_cent_dev, cent_dev1, cent_dev2]
    # # fist_of_doom = Unit(cent_dev_list, "heavy support", "fist of doom")
    # # liberatus = Unit([whirlwind], "heavy support", "liberatus")
    # #
    # # marines_formation = Patrol("emperor's finest", thelonius, alfa_squad, heavy_1=liberatus, heavy_2=fist_of_doom)
    # #
    # # # TAU EMPIRE
    # # pulse_rifle = Weapon("pulse rifle", 1, 5, 0, 1, ["rapid fire: if target distance < weapon_range/2: attacks = 2"])
    # # heavy_burst_cannon = Weapon("heavy burst cannon", 12, 6, 1, 2, ["nova reactor: if nova_charged: self.attacks = 18"])
    # # cycling_ion_blaster = Weapon("cycling ion blaster", 4, 7, 1, "d3", ["overcharge: if overcharge: self.D = d3,"
    # #                                                                     " self.w_str = 8"])
    # # fusion_blaster = Weapon("fusion blasster", 1, 8, 4, "d6+1")
    # # # missile_pod = Weapon("missile pods", 4)
    # #
    # # shield = Equipment("shield", ["inv: 5"])
    # # ion_shield = Equipment("ion shield", "inv: 4")
    # #
    # # tau_armoury = (pulse_rifle, heavy_burst_cannon, cycling_ion_blaster)
    # #
    # # enforcerrer_commander = Model("hq", 2, 5, 2, 6)
    # # enforcerrer_commander.other_equipments = [cycling_ion_blaster, cycling_ion_blaster, cycling_ion_blaster,
    # #                                                  cycling_ion_blaster]
    # #
    # # cold_star_commander = Model("hq", 2, 5, 2, 6)
    # # cold_star_commander.other_equipments = [fusion_blaster, fusion_blaster, fusion_blaster, ion_shield]
    # #
    # # shasui = Model("sha'sui", 4, 3, 4, 1)
    # # shasui.other_equipments = [pulse_rifle]
    # # fire_warrior_1 = Model("fire warrior", 4, 3, 4, 1)
    # # fire_warrior_1.other_equipments = [pulse_rifle]
    # # fire_warrior_2 = Model("fire warrior", 4, 3, 4, 1)
    # # fire_warrior_2.other_equipments = [pulse_rifle]
    # # fire_warrior_3 = Model("fire warrior", 4, 3, 4, 1)
    # # fire_warrior_3.other_equipments = [pulse_rifle]
    # # fire_warrior_4 = Model("fire warrior", 4, 3, 4, 1)
    # # fire_warrior_4.other_equipments = [pulse_rifle]
    # # fire_warrior_5 = Model("fire warrior", 4, 3, 4, 1)
    # # fire_warrior_5.other_equipments = [pulse_rifle]
    # # fire_warrior_6 = Model("fire warrior", 4, 3, 4, 1)
    # # fire_warrior_6.other_equipments = [pulse_rifle]
    # # fire_warrior_7 = Model("fire warrior", 4, 3, 4, 1)
    # # fire_warrior_7.other_equipments = [pulse_rifle]
    # # fire_warrior_8 = Model("fire warrior", 4, 3, 4, 1)
    # # fire_warrior_8.other_equipments = [pulse_rifle]
    # # fire_warrior_9 = Model("fire warrior", 4, 3, 4, 1)
    # # fire_warrior_9.other_equipments = [pulse_rifle]
    # #
    # # fire_warriors_list = [shasui, fire_warrior_1, fire_warrior_2, fire_warrior_3, fire_warrior_4, fire_warrior_5,
    # #                       fire_warrior_6, fire_warrior_7, fire_warrior_8, fire_warrior_9]
    # #
    # # riptide = Model("elite", 4, 6, 2, 16, [heavy_burst_cannon, shield])
    # # .other_equipments =
    # #
    # # enforcerrer_commander_unit = Unit([enforcerrer_commander], "hq")
    # # cold_star_commander_unit = Unit([cold_star_commander], "hq")
    # # fire_warriors_unit = Unit(fire_warriors_list, "troops")
    # # riptide_unit = Unit([riptide], "elite")
    # #
    # # tau_formation = Patrol("fish faces", enforcerrer_commander_unit, fire_warriors_unit,
    # #                        second_hq=cold_star_commander_unit, elite_1=riptide_unit)
    # #
    # # print(captain.main_hand_weapon)
    #
    # captain = Model("hq", 2, 4, 3, 6)
    # # captain.equip_main_weapon(thunder_hammer)
    # # captain.equip_second_hand(storm_shield)
    # captain.add_extra_equipment(bolt_pistol)
    # # print(captain.main_hand_weapon)
    # # print(captain.second_hand)
    # captain.display_equipments()
    # # print(captain.other_equipments)
