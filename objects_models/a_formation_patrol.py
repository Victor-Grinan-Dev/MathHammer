class FormationPatrol:

    def __init__(self, name):
        self.name = name
        self.hq_1 = None
        self.hq_2 = None
        self.troop_1 = None
        self.troop_2 = None
        self.troop_3 = None
        self.troop_4 = None
        self.elite_1 = None
        self.elite_2 = None
        self.fast_1 = None
        self.fast_2 = None
        self.heavy_1 = None
        self.heavy_2 = None
        self.list_of_units = []

        if not self.hq_1 or not self.troop_1:
            self.illegal_army()
        else:
            pass  # start with the stuff... what stuff?

    @staticmethod
    def illegal_army():
        return "Illegal name, must have at least 1 hq and 1 troop"