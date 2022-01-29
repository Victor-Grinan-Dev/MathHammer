from objects_models.a_weapon import Weapon, MeleeWeapon
from objects_models.an_equipment import Equipment
bolt_pistol = Weapon("bolt pistol", "12", "pistol", "1", "4", "0", "1", "pistol: if model_in_combat == True and "
                                                                        "shooting_Phase: range_attack(pistol)")
bolter = Weapon("Bolter", "24", "rapid fire", "1", "4", "0", "1", "rapid fire: if target distance < weapon_range/2: "
                                                                  "attacks *= 2")
flamer = Weapon("flamer", "12", "auto hits", "d6", "4", "0", "1")
storm_bolter = Weapon("storm bolter", "24", "rapid fire", "2", "4", "0", "1", "rapid fire: if target distance < "
                                                                              "weapon_range/2: attacks = 2")
hurricane_bolter = Weapon("hurricane bolter", "24", "rapid fire", "6", "4", "0", "1", "rapid fire: if target distance "
                                                                                      "< weapon_range/2: attacks = 2")

vengance_launcher = Weapon("vengance whirlwind", "48", "heavy", "2d3", "7", "1", "2")
castellan_launcher = Weapon("castellan whirlwind", "48", "heavy", "4d6", "6", "0", "1")
grav_cannon = Weapon("grav cannon", "24", "heavy", "4", "5", "3", "1", "grav: if target.save <= 3: self.D = 2")

storm_shield = Equipment("storm shield", "inv = 4/save += 1")

thunder_hammer = MeleeWeapon("thunder hammer", "x2", "2", "3", "unwieldy: ws - 1")

marines_armoury = [bolt_pistol, bolter, flamer, storm_bolter, hurricane_bolter, vengance_launcher, castellan_launcher,
                   grav_cannon, storm_shield]