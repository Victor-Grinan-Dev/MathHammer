import os
import csv
import functools

AMPERSAND = '&amp;'
LESS_THAN = '&lt;'
MORE_THAN = '&gt;'
APOSTROFE = '&#8217;'
ASTERISCO = '&#8226;'

ROLES = ['HQ', 'Troops', 'Elites', 'Fast Attack', 'Heavy Support', 'Flyer', 'Dedicated Transport', 'No Force Org Slot']

ANGELS_OF_DEATH = 'And They Shall Know No Fear, Bolter Discipline, Combat Doctrines'

KEY_WORDS_IN_RULES = ['When', 'Re-roll', 'During', 'If', 're-roll', 'Ballistic',
                      'target', 'suffer', 'to hit', 'Each', 'select', 'Instead', 'shooting', 'For the purposes',
                      'Each time', 'gain', 'controls', 'Roll', 'firing', 'You can', 'This model', 'cannot', 'must',
                      'subtract', 'rolls', 'The first time', 'roll', 'In addition', 'Models', ' If', 'can be included',
                      'preventing', 'After', 'At the start', 'each', 'Command phase', 'if', 'added', 'Can', 'Cannot',
                      'counts', 'number of dice', 'characteristic', 'model']

RULE_BOOKS = ['Codex:', 'Psychic Awakening']

MODELS_STAT = ['M', 'WS', 'BS', 'S', 'T', 'W', 'A', 'Ld', 'Save'], ['Inv', 'FNP']
WEAPONS_STATS = ['Range', 'Type', 'S', 'AP', 'D', 'Abilities']
PSY_POW_STATS = ['Psychic Power', 'Warp Charge', 'Range', 'Details']
PSY_MODEL_ABILITY_STATS = ['Cast', 'Deny', 'Powers Known', 'Other']


class ParseFromHtml:
    extension = '.txt'
    book_references_list = ['Psychic Awakening']
    serial_No = 10000
    path = os.getcwd()
    address = './ParsedData'
    own_dir = '/ready_data_'
    full_path = f'{address}{own_dir}'

    def __init__(self, battle_scribe_html_file):

        # Army data:
        self.name = None
        self.pts = None
        self.CP = 0
        self.battle_type = None
        self.detachment = None
        self.faction = None
        self.subfaction = None
        self.codex = None

        self.amount_of_units = None

        self.roles = []
        self.units = []
        self.psychic_powers = []
        self.army_rules = {}  # all of them
        self.warlord = None

        # METHODS TO CONSTRUCT OBJECT, this data is only useful for program insides
        self.file = battle_scribe_html_file
        self.raw_data_text = []  # all the html with out code in txt
        self.general_rules_text = []
        self.army_rules_names = []
        self.army_rules_list = []
        self.general_rules_text = list(zip(self.army_rules_names, self.army_rules_list))
        for rule in self.general_rules_text:
            self.army_rules[rule[0]] = rule[1]
        self.all_unit_chunks = []

        # system
        self.start_system()

        # all parse data organise in:
        self.create_general_dir()
        self.create_army_dir()

        # empty memory
        self.general_rules_text = []
        self.army_rules_names = []
        self.raw_units_text = []
        self.raw_psy_text = []

        #  todo: -weapon, stats ( + record, csv, sqlite)

    def __repr__(self):
        if not self.psychic_powers:
            self.psychic_powers = None
        return f"""
Army Name: {self.name}
Army Points: {self.pts}
Army Detachment: {self.detachment}
Army Faction: {self.faction}
Army CPs: {self.CP}
Army Battle Type: {self.battle_type}
Army Sub-Faction: {self.subfaction}
Army Rules: {self.army_rules}
Army Roles: {self.roles}
Army Amount of Units: {self.amount_of_units}
Army Psychic Powers: {self.psychic_powers}
Army Units: {self.units}"""

    def start_system(self):
        self.open_file_to_data()
        self.cut_first_part()  # up to HQ lines
        self.cut_last_part()
        self.cut_mid_size_tags_lines()
        self.mark_start_of_unit()
        self.deal_with_small_tags()

        self.erase_Categories_Configuration_lines()
        self.erase_Detachment_Command_Cost_lines()
        self.erase_configuration_CP_line()
        self.erase_blank_lines()
        self.emplace_more_les_than_signs()
        self.emplace_ampersand()
        self.emplace_apostrofe()
        self.emplace_asterisco()

        self.populate_general_rules_data()  # separates general rules and units

        self.get_army_name()
        self.get_army_pts()
        self.get_detachment()
        self.get_faction()
        self.get_CP()
        self.get_battle_type()
        self.get_first_line_rule()
        self.get_sub_faction()
        self.get_faction_ability()

        self.create_general_dir()
        self.create_army_dir()
        self.record_raw_data_in_txt()

        self.erase_pages_and_useless_data()
        self.fix_army_rules_names()
        self.get_the_rest_of_the_general_rules()
        self.make_general_rules_text_pair_odd_lines()
        self.get_the_damned_rules()
        self.record_rules_in_csv()
        # end of rules block

        self.get_psychic_powers()
        self.parse_psy_powers()
        self.record_psypow_in_csv()
        # end of psy pow block

        self.clean_unit_pages_references()
        self.how_many_each_roles_in_army()

        self.test()

    def create_general_dir(self):
        if not os.path.exists(f'{self.address}'):
            os.mkdir(f'{self.address}')

    def create_army_dir(self):
        address = f'{self.full_path}{self.name}'
        if not os.path.exists(address):
            os.mkdir(address)
        self.address = address

    # PREPARE RAW DATA BlOCK
    def open_file_to_data(self):
        with open(self.file, 'r') as file:
            data = file.readlines()

        for line in data:
            if line != '\n':
                self.raw_data_text.append(line.strip())

    def record_raw_data_in_txt(self):
        """inner method: prepare the html in txt format to be parsed"""

        filename = self.name.strip()
        name = filename + self.extension
        if not os.path.exists(f'{self.address}'):
            self.address = f'{self.address}/plain_text_data_{filename}'
            os.mkdir(self.address)

        with open(f'{self.address}/{name}', 'w') as file:
            for line in self.raw_data_text:
                file.writelines(line + '\n')

    def cut_first_part(self):  # ok 28.11.2021
        """inner method: get rid off all css lines"""

        index = 0
        data = None
        for item in self.raw_data_text:
            if item == '<body class="battlescribe">':
                data = self.raw_data_text[index + 1:]

            index += 1
        self.raw_data_text = data

    def cut_last_part(self):  # ok 28.11.2021
        """inner method: erases the "Created with Battlescribe" line"""

        end_index = 0
        for line in self.raw_data_text:
            if 'Created with' in line:
                end_index = self.raw_data_text.index(line)

        data = self.raw_data_text[:end_index]
        self.raw_data_text = data

    def cut_mid_size_tags_lines(self):  # ok 28.11.2021
        """inner method: erases the lines under lenth 12"""

        data = []

        for line in self.raw_data_text:
            if len(line) > 12:
                data.append(line)
        self.raw_data_text = data

    def mark_start_of_unit(self):  # ok 28.11.2021
        """inner method: add lines with marks where the units starts"""

        stop_str = '<li class="rootselection">'
        new_raw_data = []
        index = 0

        for line in self.raw_data_text:

            if index < len(self.raw_data_text) - 1:
                next_line = self.raw_data_text[index + 1]
                if stop_str in line and 'PL' in next_line and 'Battle Size [' not in next_line:
                    line = '__START OF A UNIT__'
            new_raw_data.append(line)
            index += 1
        self.raw_data_text = new_raw_data

    def deal_with_small_tags(self):  # ok 28.11.2021
        """inner method: exchanges table tags for spaces"""

        raw_data = []
        for line in self.raw_data_text:
            if '</th><th>' in line:
                line = line.replace('</th><th>', ' ')
            if '</td><td>' in line:
                line = line.replace('</td><td>', ' ')
            new_line = self.erase_tags_from_line(line)
            raw_data.append(new_line)

        self.raw_data_text = raw_data

    def erase_Categories_Configuration_lines(self):
        """inner method: erases lines that contain the word "Categories" & "Configuration" """

        raw_data = []
        for line in self.raw_data_text:
            if 'Categories: Configuration' not in line:
                raw_data.append(line)
        self.raw_data_text = raw_data

    def erase_Detachment_Command_Cost_lines(self):
        """inner method: erases lines that contain the word "Detachment Command Cost" """

        raw_data = []
        for line in self.raw_data_text:
            if 'Detachment Command Cost' not in line:
                raw_data.append(line)
        self.raw_data_text = raw_data

    def erase_configuration_CP_line(self):
        """inner method: erases lines that contain the word "configuration CP" """
        raw_data = []
        for line in self.raw_data_text:
            if 'Configuration [' not in line:
                raw_data.append(line)
        self.raw_data_text = raw_data

    def erase_blank_lines(self, data=None):
        """inner method: erases lines that contain newline signs and empty strs """
        if not data:
            data = self.raw_data_text
        raw_data = []
        for line in data:
            new_line = line.split('\n')
            if new_line[0]:
                raw_data.append(new_line[0])
        self.raw_data_text = raw_data

    def emplace_more_les_than_signs(self):
        """inner method: replaces code for right simbols"""

        new_data = []
        for line in self.raw_data_text:
            if MORE_THAN in line and LESS_THAN in line:
                line = self.more_les_than(line)

            new_data.append(line)
        self.raw_data_text = new_data

    def emplace_ampersand(self):
        """inner method: replaces code for right simbols"""

        new_data = []
        for line in self.raw_data_text:
            if AMPERSAND in line:
                line = self.ampersand(line)

            new_data.append(line)
        self.raw_data_text = new_data

    def emplace_apostrofe(self):
        """inner method: replaces code for right simbols"""

        new_data = []
        for line in self.raw_data_text:
            if APOSTROFE in line:
                line = self.apostrofe(line)

            new_data.append(line)
        self.raw_data_text = new_data

    def emplace_asterisco(self):
        """inner method: replaces code for right simbols"""

        new_data = []
        for line in self.raw_data_text:
            if ASTERISCO in line:
                # print(line)
                line = self.asterisco(line)
                # print(line)
            new_data.append(line)
        self.raw_data_text = new_data

    def populate_general_rules_data(self):
        """inner method: splits the raw text in general rules and unit rules to be parsed separately
        it modifies the raw text file"""

        index = 0
        new_raw_data = []

        while index < len(self.raw_data_text) - 1:
            line = self.raw_data_text[index]
            # get the top rules
            self.general_rules_text.append(line)

            # get the units data
            if 'No Force Org Slot [' in line:

                while 'Force Rules' not in line and index < len(self.raw_data_text) - 1:
                    line = self.raw_data_text[index]
                    if 'Force Rules' in line:
                        break
                    new_raw_data.append(line)
                    index += 1

            if 'HQ [' in line:
                while 'Force Rules' not in line and index < len(self.raw_data_text) - 1:
                    line = self.raw_data_text[index]
                    # self.raw_units_text.append(line)
                    if 'Force Rules' in line:
                        break
                    new_raw_data.append(line)

                    index += 1
            index += 1

        self.raw_units_text = new_raw_data

        # check if resume
        is_resume = False
        for line in self.raw_data_text:
            if 'Force Rules' in line or 'Selection Rules' in line:
                is_resume = True

        if is_resume:
            index = len(self.raw_data_text) - 1
            while index > 0:
                line = self.raw_data_text[index]
                if 'Force Rules' in line or 'Selection Rules' in line:
                    butt = self.raw_data_text[index:]
                    self.general_rules_text.extend(butt)
                    break
                index -= 1

    # GENERAL DATA GETTERS
    def get_army_name(self):  # ok 29.11.2021
        line = self.general_rules_text[0]
        self.name = line.split(' (')[0]
        self.general_rules_text.remove(line)

    def get_army_pts(self):  # ok 29.11.2021
        line = self.general_rules_text[0]
        pts_text = ''
        if 'CP, ' in line:
            a = line.split('CP, ')[1]
            pts_text = a.split(']')[0]

        elif ', , ' in line:
            a = line.split(', , ')[1]
            pts_text = a.split('pts]')[0]

        no_coma_pts = ''
        for char in pts_text:
            if char.isdigit():
                no_coma_pts += char
        self.pts = int(no_coma_pts)

    def get_detachment(self):  # ok 29.11.2022
        for line in self.general_rules_text:
            if 'Detachment' in line:
                self.detachment = line.split(' Detachment')[0]
                break

    def get_faction(self):
        for line in self.general_rules_text:

            if 'Detachment' in line and '(' in line:
                a = line.split('(')[1]
                faction = a.split(')')[0]
                self.faction = faction
                self.general_rules_text.remove(line)
                break

    def get_CP(self):  # ok 29.11.2021
        for line in self.general_rules_text:

            if 'Battle Size' in line:

                if '[' in line:
                    cp = line.split('[')[1]
                    cp = cp.split('CP]')[0]
                    self.CP = int(cp)
                    self.general_rules_text.remove(line)
                    break
                else:
                    print('CPs not specified in list')
                    print('I asume is 18CP')
                    self.CP = 18
                    self.general_rules_text.remove(line)
                    break

        for line in self.general_rules_text:
            if 'Configuration [' in line:
                cp = line.split('[')[1]
                cp = cp.split('CP]')[0]
                self.CP = int(cp)
                self.general_rules_text.remove(line)
                break

    def get_battle_type(self):  # ok 29.11.2021
        for line in self.general_rules_text:

            if 'Selection' in line and 'PL' in line:
                if '. ' in line:
                    a = line.split('. ')[1]
                    battle_size = a.split(' (')[0]
                    self.battle_type = battle_size
                    self.general_rules_text.remove(line)

    def get_first_line_rule(self):
        for line in self.general_rules_text:
            if 'Rules: ' in line:
                rules = line.split('Rules: ')[1]
                self.army_rules_names.append(rules)
                self.general_rules_text.remove(line)

    def get_sub_faction(self):
        subfaction_name = ''
        subfaction = ''

        for line in self.general_rules_text:

            if ' Choice' in line:
                subfaction_name = line.split(' Choice')[0]
                self.general_rules_text.remove(line)
                break
            if 'Selector' in line:
                subfaction_name = line.split('Selector')[0]
                subfaction_name = subfaction_name.split('**')[1]
                self.general_rules_text.remove(line)
                break
            else:
                subfaction_name = line.strip()
                self.general_rules_text.remove(line)
                break

        if ' / ' in subfaction_name:
            subfaction_name = subfaction_name.split(' / ')[0]

        for line in self.general_rules_text:
            if 'Selections:' in line:
                if 'Custom' in line:
                    subfaction = self.fix_succesor_chapter_order(line)
                    self.general_rules_text.remove(line)
                    break
                if 'Selections:' in line:
                    subfaction = line.split('Selections: ')[1]
                    self.general_rules_text.remove(line)
                    break

        self.subfaction = (subfaction_name, subfaction)

    def get_faction_ability(self):
        for line in self.general_rules_text:
            if 'Abilities: ' in line:
                faction_ability = line.split('Abilities: ')[1]
                if ', ' in faction_ability:
                    faction_ability = faction_ability.split(', ')
                    for item in faction_ability:
                        self.army_rules_names.append(item)
                    self.general_rules_text.remove(line)
                    break
                else:
                    self.army_rules_names.append(faction_ability)
                    self.general_rules_text.remove(line)
                    break

    @staticmethod
    def fix_succesor_chapter_order(line):
        """inner method: in the case of the marines, the sucessor chapter rules are not ordered, this function fixes
        that """
        new_line = ''
        arrange = []
        line_list = line.split(':')[1]
        line_list = line_list.split(',')

        # put succesor first in list
        for item in line_list:
            if 'Successor' in item:
                arrange.append(item)

        for item in line_list:
            if ' Custom Chapter' in item:
                arrange.append(item)

        for item in arrange:
            if item != arrange[-1]:
                new_line += item + ', '
            else:
                new_line += item
        return new_line

    def erase_pages_and_useless_data(self):
        """inner method: find rest of useless data to erase"""
        for line in self.general_rules_text:
            if self.condition1(line) and self.condition2(line):
                self.general_rules_text.remove(line)

        for line in self.general_rules_text:
            if line == 'Description':
                self.general_rules_text.remove(line)

        for line in self.general_rules_text:
            if 'Selection Rules' in line:
                self.general_rules_text.remove(line)

        for line in self.general_rules_text:
            if 'Force Rules' in line:
                self.general_rules_text.remove(line)

        for line in self.general_rules_text:
            if 'Codex:' in line:
                step1 = line.split('Codex: ')[1]
                self.codex = step1.split(' p')[0]
                self.general_rules_text.remove(line)

        for line in self.general_rules_text:
            for book_reference in self.book_references_list:
                if book_reference in line:
                    self.general_rules_text.remove(line)

        for line in self.general_rules_text:
            if 'This unit has the following abilities:' in line:
                self.general_rules_text.remove(line)

    @staticmethod
    def condition1(line):
        is_useless = False
        useless_data = ['[', '(', 'Abilities', 'Description', 'Selection Rules']
        for item in useless_data:
            if item in line:
                is_useless = True
        return is_useless

    @staticmethod
    def condition2(line):
        return len(line) < 40

    def fix_army_rules_names(self):

        new_list = []
        for item in self.army_rules_names:
            if ',' in item:
                subitems = item.split(', ')
                for sub_item in subitems:
                    new_list.append(sub_item.strip())
            else:
                new_list.append(item.strip())

        self.army_rules_names = new_list

    def get_the_rest_of_the_general_rules(self):

        for line in self.general_rules_text:
            if ':' in line and len(line) < 40:
                rule = line.split(':')[0]
                if rule not in self.army_rules_names:
                    self.army_rules_names.append(rule)

    def make_general_rules_text_pair_odd_lines(self):

        index = 0
        max_index = len(self.general_rules_text) - 1

        while index < max_index:
            current_line = self.general_rules_text[index]
            if 'Angels of Death' in current_line:
                self.general_rules_text.insert(index + 1, ANGELS_OF_DEATH)
            elif len(current_line) < 35:
                next_line = self.general_rules_text[index + 1]
                if len(next_line) < 35:
                    self.general_rules_text.insert(index + 1, 'NO DATA')
                    index += 1
            index += 1

    def get_the_damned_rules(self):

        self.general_rules_text = self.set_in_same_order(self.general_rules_text)

        new_dict = {}
        new_list = []
        index = 0
        max_index = len(self.general_rules_text) - 1
        key = ''
        value = ''

        while index < max_index:
            line = self.general_rules_text[index]
            if len(line) < 35:  # found new key
                if key and value:  # last key value is over, needs to record
                    new_dict[key] = value
                    new_list.append([key, value])
                # get new key
                key = line
                # reset value
                if value:
                    value = ''
                index += 1
            else:
                value += line
                index += 1
            if index == max_index:  # ends the text
                if not value:
                    value += self.general_rules_text[-1]
                new_dict[key] = value
                new_list.append([key, value])

        self.army_rules = new_dict
        self.army_rules_list = new_list

    def record_rules_in_csv(self):

        file_name = f'general rules {self.name}'
        fieldnames = ['Ability', 'Description']

        with open(f'{self.full_path}{self.name}/{file_name}.csv', 'w') as f:
            writer = csv.writer(f)

            writer.writerow(fieldnames)

            for item in self.army_rules_list:
                writer.writerow(item)

    # TOOLS
    @staticmethod
    def is_new_line_sign(line):
        if '\n' in line:
            print(line.count('\n'))

    @staticmethod
    def erase_tags_from_line(line):

        index = 0
        new_line = ''
        while index < len(line):
            if line[index] == '<':
                while line[index] != '>':
                    index += 1
            else:
                if line[index] != '>':
                    new_line += line[index]
                index += 1

        return new_line

    @staticmethod
    def set_in_same_order(some_list):

        unique_items = []

        for item in some_list:
            if item not in unique_items:
                unique_items.append(item)

        return unique_items

    @staticmethod
    def ampersand(line):
        """this is made to deal with 0ne str at the time"""

        if type(line) == list:
            for item in line:
                if AMPERSAND in item:
                    new_line = item.replace(AMPERSAND, '&')
                    return new_line
        elif type(line) == str:
            if AMPERSAND in line:
                new_line = line.replace(AMPERSAND, '&')
                return new_line

        return AMPERSAND in line

    @staticmethod
    def more_les_than(line):

        if type(line) == list:
            for item in line:
                if LESS_THAN in item and MORE_THAN in item:
                    new_line = item.replace(LESS_THAN, '<')
                    new_line = new_line.replace(MORE_THAN, '>')
                    return new_line
        elif type(line) == str:
            if LESS_THAN in line and MORE_THAN in line:
                new_line = line.replace(LESS_THAN, '<')
                new_line = new_line.replace(MORE_THAN, '>')
                return new_line

        return LESS_THAN in line and MORE_THAN in line

    @staticmethod
    def apostrofe(line):

        if type(line) == list:
            for item in line:
                if APOSTROFE in item:
                    new_line = item.replace(APOSTROFE, "'")
                    return new_line
        elif type(line) == str:
            if APOSTROFE in line:
                new_line = line.replace(APOSTROFE, "'")
                return new_line

        return APOSTROFE in line

    @staticmethod
    def asterisco(line):

        if type(line) == list:
            for item in line:
                if ASTERISCO in item:
                    new_line = item.replace(ASTERISCO, "*")
                    return new_line
        elif type(line) == str:
            if ASTERISCO in line:
                new_line = line.replace(ASTERISCO, "*")
                return new_line

        return ASTERISCO in line

    @staticmethod
    def is_item_of_list_in_line(line, list_of_items):

        for item in list_of_items:
            if item in line:
                return True
        return False

    @staticmethod
    def wich_item_is_in_line(line, list_of_items, return_index=False):

        if return_index:
            index = 0
            for item in list_of_items:
                if item in line:
                    return list_of_items.index(item)
                index += 1
            return None  # it returns None automatically

        else:
            for item in list_of_items:
                if item in line:
                    return item
            return None

    @staticmethod
    def move_next_line(index, data):

        index += 1
        line = data[index]
        return index, line

    @staticmethod
    def is_quote_or_dash(line):

        is_quote_or_dash = False

        if line[0].isdigit():
            for char in line:
                if char == '"':
                    is_quote_or_dash = True
                    break

        elif line[0] == '-':
            is_quote_or_dash = True

        return is_quote_or_dash

    # PREPARE UNIT TEXT DATA
    def clean_unit_pages_references(self):
        for line in self.raw_units_text:
            if ':' in line:
                for book in RULE_BOOKS:
                    if book in line:
                        self.raw_units_text.remove(line)

    def points_per_role(self):

        pts_list = []
        data = self.raw_units_text

        for line in data:
            is_role = self.is_item_of_list_in_line(line, ROLES)
            if is_role and ' [' in line:
                # role = self.wich_item_is_in_line(line, ROLES)
                step = line.split(', ')[1]
                pts = step.split('pts')[0]
                pts_list.append(pts)
                self.raw_units_text.remove(line)

        return pts_list

    def how_many_each_roles_in_army(self):
        index = 0
        max_index = len(self.raw_units_text) - 1
        new_list = []
        amounts = []
        data = self.raw_units_text
        line = data[index]
        role = None

        while index < max_index:
            is_role = self.wich_item_is_in_line(line, ROLES)

            if is_role and ' [' in line:  # found a role
                index, line = self.move_next_line(index, data)
                role = is_role

            elif '__START OF A UNIT__' in line and index < max_index:
                index, line = self.move_next_line(index, data)
                if role:
                    # print(role)
                    new_list.append(role)

            else:
                if index < max_index:
                    index, line = self.move_next_line(index, data)

        all_roles = self.set_in_same_order(new_list)

        for item in all_roles:
            amount = new_list.count(item)
            amounts.append(amount)

        self.amount_of_units = functools.reduce(lambda a, b: a + b, amounts)
        pts = self.points_per_role()
        roles_amount_pts = list(zip(all_roles, amounts, pts))
        self.roles = roles_amount_pts

        # create a stop '__START OF A UNIT__' for unit chunk parse
        self.raw_units_text.append('__START OF A UNIT__')

    # Psy powers parse and clean up
    def get_psychic_powers(self):

        # for line in self.raw_units_text:
        #     print(line)

        data = self.raw_units_text
        index = 0
        max_index = len(data) - 1
        new_raw_text = []
        psy_chunk = []

        while index < max_index:
            line = data[index]
            if 'Warp Charge Range Details' in line:
                index, line = self.move_next_line(index, data)
                while 'Cast Deny Powers Known Other' not in line:
                    if line == 'Psyker':
                        index, line = self.move_next_line(index, data)
                    else:
                        if 'If' in line:
                            begining = line[:6]
                            index_start = line.index('If')
                            line = begining + line[index_start:]
                        psy_chunk.append(line)
                        psy_chunk = self.set_in_same_order(psy_chunk)
                        index, line = self.move_next_line(index, data)
            else:
                new_raw_text.append(line)
                index += 1

        self.raw_psy_text = psy_chunk

    def parse_psy_powers(self):
        data = self.raw_psy_text
        index = 0
        max_index = len(data) - 1
        details = None
        name = None
        warp_charge = None
        pow_range = None

        # for line in self.raw_psy_text:
        #     print(line)

        while index < max_index:
            line = data[index]
            if index % 2 == 1:
                value = line
                # print(value)
                warp_charge = value[0]
                pow_range = value[2:5]
                pow_range = pow_range.split('"')[0]
                details = value[6:]
                index += 1
            else:
                if ')' in line:
                    line = line.split(') ')[1]
                if ' (' in line:
                    line = line.split(' (')[0]
                name = line
                index += 1
            if name and warp_charge and warp_charge and pow_range and details:
                self.psychic_powers.append([name, warp_charge, pow_range, details])
                name = None
                warp_charge = None
                pow_range = None
                details = None

        self.raw_psy_text = []

    def record_psypow_in_csv(self):
        # todo:
        file_name = f'Psy Powers {self.name}'
        fieldnames = PSY_POW_STATS

        with open(f'{self.address}/{file_name}.csv', 'w') as f:
            writer = csv.writer(f)

            writer.writerow(fieldnames)

            for item in self.psychic_powers:
                writer.writerow(item)

    def parse_weapon_stats_record_in_csv(self):
        for item in self.all_unit_chunks:
            print(item)
        pass

    def parse_models_stats_record_in_csv(self):
        pass

    # unit parse and clean up
    # def build_a_unit(self):
    #
    #     # TODO: find all inf build model by model first
    #
    #     fieldrole = ''
    #     name = ''
    #     models = []  # ['sgt', 'marine', 'marine' ...]
    #     categories = []  # list of names of categories
    #     equipments = []  # list of equipment names
    #     abilities = []  # list of abilities names
    #
    #     is_psyker = False
    #
    #     army = self.name
    #     stats = None
    #
    #     # THIS DATA NEEDS TO BE RECORDED INDIVIDUALY TO CSV DATABASE
    #     # TODO: Create model object with each model data
    #     model = [army, fieldrole, name, stats, categories, equipments, abilities]  # unit de tuple ('M', 6)...
    #     for category in categories:
    #         if category == 'Psyker':
    #             is_psyker = True
    #
    #     if is_psyker:
    #         cast = 2
    #         deny = 1
    #         power_known = 'Smite'
    #         other_powers = []
    #         psyker_model = [cast, deny, power_known, other_powers]
    #
    #         model.extend(psyker_model)
    #     # TODO: Add rules to the database
    #     rules = []  # pass this rules to the general rule pool
    #     # TODO: Create weapon objects
    #     weapon_stats = []
    #
    #     # TODO: Create a Unit object with all this models objects
    #     unit = [fieldrole, name, models, categories, equipments, abilities]
    #
    # def get_id(self):
    #     self.serial_No += 1
    #     return self.serial_No
    #
    # def parse_unit_name_pts_pl_erase_line(self, line):
    #     if '__START OF A UNIT__' in line:
    #
    #         index = self.raw_units_text.index(line)
    #         # erase_from = index
    #
    #         # moving to Name & pts line
    #         index, line = self.move_next_line(index, self.raw_units_text)
    #         unit_name = line.split(' [')[0]
    #         pl_step, pts_step = line.split(' PL, ')
    #         unit_PL = pl_step.split('[')[1]
    #         unit_pts = pts_step.split('pts]')[0]
    #         if 'CP, ' in unit_pts:
    #             unit_pts = unit_pts.split('CP, ')[1]
    #
    #         # moving to selection line
    #         index, line = self.move_next_line(index, self.raw_units_text)
    #         selection = line[12:]
    #         # print(line)
    #
    #         # fractioned_line = line.split(', ')
    #         # print(fractioned_line)
    #
    #         return unit_name, int(unit_pts), int(unit_PL)

    def split_unit_chunks(self):

        data = self.raw_units_text

        start_index = 0
        mid_index = 0
        # max_index = len(data) - 1
        chunk = []
        has_started = False

        for line in data:
            if '__START OF A UNIT__' in line:
                start_index = data.index(line)
                has_started = True
            else:
                if has_started:
                    chunk.append(line)
                    mid_index = start_index + 1

            if '__START OF A UNIT__' in line and mid_index > start_index:
                self.all_unit_chunks.append(chunk)
                self.raw_units_text.remove(line)

                for item in chunk:
                    if item in data:
                        self.raw_units_text.remove(item)
                break

    # todo: make this block more efective?
    @staticmethod
    def get_unit_name(unit):

        line_index = 0
        name = ''

        for line in unit:
            # print(line)
            if line_index == 0:
                if ' [Legends] [' in unit[line_index]:
                    name = line.split(' [Legends] [')[0]
                else:
                    name = unit[line_index].split(' [')[0]

        return name

    @staticmethod
    def get_unit_pl(unit):
        line_index = 0
        pl = None

        for line in unit:
            if ' [Legends] [' in unit[line_index]:
                _, line = line.split(' [Legends] [')

            else:
                _, line = unit[line_index].split(' [')

            pl = int(line.split(' PL')[0])

            break
        return pl

    @staticmethod
    def get_unit_cp(unit):

        cp = None

        for line in unit:
            if 'CP, ' in line:
                cp, _ = line.split('CP, ')
                cp = int(cp.split('PL, ')[1])
            break
        return cp

    @staticmethod
    def get_unit_pts(unit):

        pts = None

        for line in unit:
            line = line.split('PL, ')[1]
            if 'CP, ' in line:
                line = line.split('CP, ')[1]
            pts = int(line.split('pts]')[0])
            break
        return pts

    @staticmethod
    def get_unit_weapons(unit):

        weapons = []

        for line in unit:
            if 'Selections:' in line:
                print(line)
            if ', Weapon: ' in line:
                print(line)
            #     line, weapon = line.split(', Weapon: ')
            #     weapons = weapon.split(', ')

        return weapons

    @staticmethod
    def get_unit_models_in_unit(unit):

        models_in_unit = None

        for line in unit:
            if 'Unit: ' in line:
                line, models_in_unit = line.split(', Unit: ')

                if models_in_unit and '[1]' not in line:

                    if ',' in models_in_unit:
                        if ', Warlord Trait: ' in models_in_unit:
                            models_in_unit, warlord_trait = models_in_unit.split(', Warlord Trait: ')
                        else:
                            models_in_unit = models_in_unit.split(', ')

        return models_in_unit

    @staticmethod
    def get_unit_warlord_trait(unit):

        warlord_trait = None

        for line in unit:
            if 'Unit: ' in line:
                line, models_in_unit = line.split(', Unit: ')

                if models_in_unit and '[1]' not in line:

                    if ',' in models_in_unit:
                        if ', Warlord Trait: ' in models_in_unit:
                            _, warlord_trait = models_in_unit.split(', Warlord Trait: ')

        return warlord_trait

    @staticmethod
    def get_unit_categories(unit):
        categories = None
        nueva_lista = []

        for line in unit:
            if 'Categories:' in line:
                a = line.split('Categories: ')[1]
                categories = a.split('Faction: ')

        if categories:
            for item in categories:
                if item:
                    # print(item.split(', '))
                    sub_item = item.split(', ')
                    for fraction in sub_item:
                        if fraction:
                            # print(fraction)
                            nueva_lista.append(fraction)

        categories = nueva_lista
        return categories

    @staticmethod
    def get_unit_wound_track(unit):

        for line in unit:
            if 'wounds' in line or 'Wound Track: ' in line or 'wounds' in line or '[1]' in line:
                wound_track = line
                # models_in_unit = line  # ???

    @staticmethod
    def get_unit_is_psyker(unit):

        is_psyker = False

        for line in unit:
            if ' Psyker: ' in line:
                # lista = line.split(', Psyker: ')[0]
                is_psyker = True

        return is_psyker

    @staticmethod
    def get_unit_psy_pow(unit):
        psy_pow = []

        for _ in unit:

            if ', Psychic Power: ' in unit:
                lista, psy_pow = unit.split(', Psychic Power: ')

        return psy_pow

    @staticmethod
    def get_unit_abilities(unit):

        abilities = []

        for line in unit:
            abilities = line.split('Abilities: ')[1]
            if ', ' in abilities:
                abilities = abilities.split(', ')

        return abilities

    def take_rules_from_units(self, unit):
        """here the 'unit' argument comes forlooped from 'test' func"""

        line_index = 0

        unit_list = []

        # name = self.get_unit_name(unit)
        # unit_list.append(name)
        # print(name)
        # pl = self.get_unit_pl(unit)
        # unit_list.append(pl)
        # cp = self.get_unit_cp(unit)
        # unit_list.append(cp)
        # pts = self.get_unit_pts(unit)
        # unit_list.append(pts)
        # categories = self.get_unit_categories(unit)
        # unit_list.append(categories)

        # weapons = self.get_unit_weapons(unit)
        # print(weapons)

        # warlord_trait = self.get_unit_warlord_trait(unit)
        # print(warlord_trait)
        # models_in_unit = self.get_unit_models_in_unit(unit)
        # print(models_in_unit)
        # abilities = self.get_unit_abilities(unit)
        # print(abilities)
        # is_psyker = self.get_unit_is_psyker(unit)
        # print(is_psyker)
        # psy_pow = self.get_unit_psy_pow(unit)
        # print(psy_pow)

        model_and_stats = self.model_stats(unit)
        # print(next(model_and_stats))

        # weapon_stats = self.weapon_stats(unit)
        index = 0
        max_index = len(unit) - 1

        description = []
        unit_data = []

        while index <= max_index:
            line = unit[index]
            # print(line)
            if line == 'Description' or line == 'Abilities' or line == 'Unit':
                pass

            else:
                unit_data.append(line)

            if line == 'Description' or len(line) < 10 and 'Unit' in line:
                while index < max_index:
                    index += 1
                    line = unit[index]
                    description.append(line)

                    # inside description there are stats for Unit, psyker, weapon. parse separatly

            index += 1
        #
        # for line in unit:
        #     print(line)

    @staticmethod
    def fix_weapon_rules(fractions):  # ['60"', 'Heavy', '4D3', '4', '0', '1', 'This', 'weapon', 'can', 'target', ...
        max_index = len(fractions) - 1
        rule_start_index = 6
        fixed_rules = ''

        if len(fractions) > 9:
            if not fractions[rule_start_index].isdigit():
                while rule_start_index <= max_index:
                    fixed_rules += fractions[rule_start_index]
                    rule_start_index += 1
                    if rule_start_index <= max_index:
                        fixed_rules += ' '
        if fixed_rules:
            new_stats = fractions[:6]
            new_stats.append(fixed_rules)
            return new_stats
        return fractions

    @staticmethod
    def fix_weapon_type(fractions):
        for fraction in fractions:
            if fraction == 'Rapid':
                at_index = fractions.index('Rapid')
                fractions.remove(fraction)
                fraction = 'Rapid Fire'
                fractions.insert(at_index, fraction)

            if fraction == 'Fire':
                fractions.remove(fraction)
        return fractions

    @staticmethod
    def model_stats(unit):
        index = 0
        max_index = len(unit) - 1
        models = []

        while index <= max_index:
            model_chunk = []
            line = unit[index]
                                                    # - M S A ends at # [4 PL, 85pts] or unit
            if line == 'M WS BS S T W A Ld Save':   # Razorback [3] (1-2 wounds remaining) 3" 6+ 5+ 6 7 N/A 1 8 3+
                                                    # f'{name} [counter] ({wounds} wounds remaining) * 6+ * 6 7 10 * 8 3+' exchange
                                                    # * 6+ * 6 7 10 * 8 3+
                                                    # Chaos Rhino3  1-2 3" 5+ 1

                index += 1

                while index <= max_index:
                    line = unit[index]
                    if line == 'Weapon':
                        break
                    model_chunk.append(line)
                    index += 1

            if model_chunk:
                # print(model_chunk)
                yield model_chunk
                # models.append(model_chunk)

            index += 1

        # return models

    def weapon_stats(self, unit):

        index = 0
        max_index = len(unit) - 1

        weapon = []

        while index <= max_index:
            line = unit[index]
            print(line)
            if 'Unit: ' in line and line[:4] == 'Unit' and '[1]' in line:
                # print(line[6:41])  # Whirlwind [1] (6+ wounds remaining)
                pass
            if line == 'Unit':
                index, line = self.move_next_line(index, unit)
                index, line = self.move_next_line(index, unit)
                # print(line)  # models name
                # while index <= max_index:
                #     index, line = self.move_next_line(index, unit)

                # if line[0] != '-' or not line[0].isdigit():
                #     break
            if line == 'Weapon':
                pass
            if self.is_quote_or_dash(line):
                fractions = line.split(' ')
                fractions = self.fix_weapon_rules(fractions)
                fraction = self.fix_weapon_type(fractions)

                # print(fractions, len(fractions)) #stats
                # index, line = self.move_next_line(index, unit)

                # print(line)

            index += 1

        return weapon

    def test(self):

        # units_headings = ['Name', 'Pts', 'PL']

        # self.unit_chunks()

        for _ in range(0, self.amount_of_units):
            self.split_unit_chunks()

        # print()
        # print(f'{self.name}')
        # print('↓ units of below army ↓')

        "↓ turn this on"
        for unit_chunk in self.all_unit_chunks:
            for line in unit_chunk:
                print(line)
                pass
            self.take_rules_from_units(unit_chunk)

        # units = []
        # for line in self.raw_units_text:
        #     unit = self.parse_unit_name_pts_pl_erase_line(line)
        #
        #     units.append(unit)
        # todo: fix error (missing units in self.raw_unit_text)


if __name__ == '__main__':
    directory = './files_in_html'

    cajlito = f'{directory}/Cajlito (HTML).html'
    machete = f'{directory}/1000pts test tau (HTML).html'
    machete2 = f'{directory}/1000pts las perras test (HTML).html'
    victor = f'{directory}/1000 BloodClaws rush (HTML).html'
    victor2 = f'{directory}/1000pts thunder rush (HTML).html'
    victor3 = f'{directory}/1000 jump rush (HTML).html'

    angels = f'{directory}/500pts DA green wing (HTML).html'
    orks = f'{directory}/4000 Orks test (HTML).html'
    orks2 = f'{directory}/6000 Orks test (HTML).html'
    tyranids = f'{directory}/1000pts Tyranids test (HTML).html'
    necrons = f'{directory}/1000pts necrons test (HTML).html'
    astra = f'{directory}/1000 pts astra militarum test (HTML).html'
    astra2 = f'{directory}/500 astra (HTML).html'
    smurf = f'{directory}/1500 Smurfs test (HTML).html'
    scars = f'{directory}/500pts white scars (HTML).html'

    all_army_list = [cajlito, machete, machete2, victor, victor2, victor3, angels, orks, orks2, tyranids, necrons,
                     astra, astra2, smurf, scars]

    data_colected_so_far = ['name', 'pts', 'CP', 'battle_type', 'detachment', 'faction', 'subfaction', 'codex',
                            'amount_of_units', 'roles', 'psychic_powers', 'units']

    # for item_ in all_army_list:
    #     try:
    #         current_army = ParseFromHtml(item_)
    #     #         print(current_army)
    #     except IndexError as e:
    #         print(f" IndexError {e}: {item_.split('/')[-1]}")
    #     except Exception as e:
    #         print(f" {Exception} {e}: {item_.split('/')[-1]}")

    current_army = ParseFromHtml(cajlito)

    # for item_ in all_army_list:
    #     current_army = ParseFromHtml(item_)
    # print(current_army)
