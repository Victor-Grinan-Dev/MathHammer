class Unit:

    def __init__(self, name, unit_size: int = 1):
        self.name = name

        self.unit_size = unit_size

        # mandatory models S
        self.leader = None
        self.member_1 = None
        self.member_2 = None

        # mandatory models M
        self.member_3 = None
        self.member_4 = None

        # extra/mandatory models L
        self.member_5 = None
        self.member_6 = None
        self.member_7 = None
        self.member_8 = None
        self.member_9 = None

        # mega size units
        self.member_10 = None
        self.member_11 = None
        self.member_12 = None
        self.member_13 = None
        self.member_14 = None

        self.list_of_models = []
