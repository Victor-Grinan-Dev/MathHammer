class Weapon:
    arguments = ["name", "range", "type", "shots", "S", "AP", "D", "special abilities"]
    quote = ""

    def __init__(self, name: str, w_range: str, w_type: str, shots: str, strength: str, armor_penetration: str,
                 damage: str, abilities: str = None):
        """

        :param name: descriptive name
        :param w_range: str of an int eg."24"
        :param w_type: descriptive type.
        :param shots: str of an int eg."2"
        :param strength: str of an int eg."4" or random code eg."2d3+1"
        :param armor_penetration: str of an absolute int eg."1" (even if originally is -1)
        :param damage: str of an int eg."3" or random code eg."d6+2"
        :param abilities: str, each ability mas be sepparated with /
        """
        self.name = name
        self.w_range = w_range
        self.w_type = w_type
        self.shots = shots
        self.s = strength
        self.ap = armor_penetration
        self.d = damage
        self.abs = abilities

        self.attributes = [self.name, self.w_range, self.w_type, self.shots, self.s, self.ap, self.d, self.abs]

    def __repr__(self, heading=False):

        if heading:
            index = 0
            for arg in self.arguments:
                if index == 0:
                    total_spaces = 20
                elif index == 2:
                    total_spaces = 12
                elif index == 4 or index == 5 or index == 6:
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
            if index == 0:
                total_spaces = 20
            elif index == 2:
                total_spaces = 12
            elif index == 4 or index == 5 or index == 6:
                total_spaces = 4
            else:
                total_spaces = 8
            if att:
                blanks = total_spaces - len(att)
                self.quote += att.title() + (" " * blanks)
            index += 1

        self.quote += "\n"

        return self.quote


class MeleeWeapon:
    arguments = ["name", "range", "type", "shots", "S", "AP", "D", "special abilities"]
    quote = ""

    def __init__(self, name: str, strength: str, armor_penetration: str,
                 damage: str, abilities: str = None):
        """

        :param name: descriptive name
        :param strength: str of an int eg."4" or random code eg."2d3+1"
        :param armor_penetration: str of an absolute int eg."1" (even if originally is -1)
        :param damage: str of an int eg."3" or random code eg."d6+2"
        :param abilities: str, each ability mas be sepparated with /
        """
        self.name = name
        self.w_range = "-"
        self.w_type = "melee"
        self.attacks = "user"
        self.s = strength
        self.ap = armor_penetration
        self.d = damage
        self.abs = abilities

        self.attributes = [self.name, self.w_range, self.w_type, self.attacks, self.s, self.ap, self.d, self.abs]

    def __repr__(self):

        index = 0
        for arg in self.arguments:
            if index == 0:
                total_spaces = 20
            elif index == 2:
                total_spaces = 12
            elif index == 4 or index == 5 or index == 6:
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
            if index == 0:
                total_spaces = 20
            elif index == 2:
                total_spaces = 12
            elif index == 4 or index == 5 or index == 6:
                total_spaces = 4
            else:
                total_spaces = 8
            if att:
                blanks = total_spaces - len(att)
                self.quote += att.title() + (" " * blanks)
            index += 1

        self.quote += "\n"

        return self.quote


if __name__ == '__main__':
    # todo  cant find the error in melee inheritance
    thunder_hammer = MeleeWeapon("thunder hammer", "x2", "2", "3", "unwieldy: ws - 1")

    print(thunder_hammer)