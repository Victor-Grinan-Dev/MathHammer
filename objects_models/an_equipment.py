class Equipment:
    arguments = ["name", "range", "type", "shots", "S", "AP", "D", "special abilities"]
    quote = ""

    def __init__(self, name, special_abilities):
        self.name = name
        self.abilities = special_abilities

        self.attributes = [self.name, "-", "-", "-", "-", "-", "-", self.abilities]

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


if __name__ == '__main__':
    storm_shield = Equipment("storm shield", "inv = 4/save += 1")
    iron_halo = Equipment("iron halo", "inv = 4")
    combat_shield = Equipment("combat shield", "inv = 5")
    print(storm_shield)