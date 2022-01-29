from bs4 import BeautifulSoup


path_html = 'C:\\Users\\victo\Desktop\projects\math_hammer(p)\database\\files_in_html\\'
html_BloodClaws = '1000 BloodClaws rush (HTML).html'
html_tau = './files_in_html/1000pts test tau (HTML).html'
html_cajlito = './files_in_html/1000pts Cajlito (HTML).html'

path_txt = 'C:\\Users\\victo\Desktop\projects\math_hammer(p)\database\\files_in_txt\\'
army_blackmane = './files_in_txt/1000pts blackmane (Plain Text).txt'
army_cajlito = './files_in_txt/Cajlito (Plain Text).txt'
army_tau = './files_in_txt1000pts/test tau (Plain Text).txt'
army_bloodclaws = './files_in_txt/1000 BloodClaws rush (Plain Text).txt'


class PlainTxtParser:

    def __init__(self, army_file):
        """
        general idea: take an cajlito_army list and turn it into MathHammer objects and populate the database
        :param army_file: a plain text from BattleScribe app
        """
        self.data = None
        with open(army_file, 'r') as file:
            self.data = file.readlines()
            for item in self.data:
                if item == '\n':
                    self.data.remove(item)

        self.army_file = army_file  # Physical file name
        self.detachment = self.extract_detachment()
        self.faction = self.extract_faction()
        self.pts = self.extract_pts()
        self.CP = self.extract_CP()
        self.game_type = self.extract_game_type()

        self.one_model_units = []

        # TODO:
        # DATA CONSTRUCTOR
        self.general_data = None
        self.all_weapons = []
        self.units = []
        self.all_equipments = []

        # TODO:
        # ARMY ANALYZER (PANDAS?)
        self.all_data = """"
        % vs light armor
        % vs heavy armor
        
        % vs light infantry
        % vs heavy infantry
        
        % vs fliers
        % melee power
        % fire power
        % support (psykers, chaplain, banner, etc)  
        % transports
        % overall speed
        etc, etc, etc    
        """

    def __repr__(self):

        quote = ''
        for line in self.data:
            quote += line
        return quote

    def extract_faction(self):

        start = self.data[0].find('(')
        end = self.data[0].find(')')
        return self.data[0][start + 1:end]

    def extract_detachment(self):

        words = self.data[0].split()
        detachment = words[1] + ' ' + words[2]
        return detachment

    def extract_pts(self):

        ends = self.data[0].find('pts') - 1
        value = ''
        while self.data[0][ends].isdigit():
            value += str(self.data[0][ends])
            ends -= 1
        return value[::-1]

    def extract_CP(self):

        start_bracket = self.data[0].find('[')
        end_bracket = self.data[0].find(']')
        section = self.data[0][start_bracket + 1: end_bracket]
        ends = section.find('CP') - 1

        value = ''
        while section[ends].isdigit():
            value += str(section[ends])
            ends -= 1
        return value[::-1]

    def extract_game_type(self):

        game_name = ''
        for line in self.data:
            if 'Battle Size' in line:
                _, new_line = line.split('.')
                for char in new_line:
                    if char == '(':
                        break
                    game_name += char
                game_name = game_name.strip()

                points = ''
                ends = line.find('Points') - 2

                while line[ends].isdigit():
                    points += line[ends]
                    ends -= 1
                points = points[::-1]
                game_type = game_name + ' ' + points
                return game_type

    def extract_army_subfaction(self):
        # TODO:
        pass

    def extract_one_model_unit_name(self, line):
        unit_name = ''
        end = line.find('[') - 2
        while end >= 0:
            unit_name += line[end]
            end -= 1
        unit_name = unit_name[::-1]
        self.one_model_units.append(unit_name)
        return unit_name

    def extract_SingleModelUnit_equipment(self, line):

        equipped = line.split(':')[1]
        equipped = equipped.split(', ')
        for item in equipped:
            if '.' in item:
                _, equipped[equipped.index(item)] = item.split('.')
            if '\n' in item:
                equipped[equipped.index(item)] = item.strip('\n')
            if '(' in item:
                part = item.split('(')
                part = part[0]
                part = part.split(')')
                for fragment in part:
                    if '.' in fragment:
                        part = fragment.split('.')[1]
                if len(part) == 2:
                    part = part[1]
                item = part.strip()
            if '.' in item:
                equipped = [item.split('.')[1] for item in equipped if '.' in item]
            if ')' in item:
                equipped = [item.split(')')[1] for item in equipped if ')' in item]

        for item in equipped:
            if item not in self.all_equipments:
                self.all_equipments.append(equipped)

        return [item.strip() for item in equipped]

    def extract_multi_model_unit_name(self, line):
        unit_name = line.split('[')[0]
        unit = unit_name.strip()
        self.units.append(unit)
        return unit

    @staticmethod
    def extract_roll(line):
        roll = line.replace('+', ' ')
        roll = roll.strip()
        return roll

    @staticmethod
    def extract_unit_pts_cost(line):
        pts_cost = ''
        end = line.find('pts') - 1
        while line[end].isdigit():
            pts_cost += line[end]
            end -= 1
        pts_cost = pts_cost[::-1]
        return pts_cost

    @staticmethod
    def extract_multi_unit_general_equipment(line):
        general_equipped = line.split(':')[1]
        general_equipped = general_equipped.split(', ')[0]
        general_equipped = general_equipped.split('\n')[0]
        general_equipped = general_equipped.strip()  # if more than 1
        return general_equipped

    @staticmethod
    def split_the_newLine(equipped):

        new_equipped = []

        for item in equipped:
            if '\n' in item:
                new_item = item.split('\n')[0]
                equipped.remove(item)
                new_equipped.append(new_item)

        return new_equipped

    @staticmethod
    def split_the_x(equipped):

        new_equipped = []

        for item in equipped:
            if item[1] == 'x' and item[0].isdigit():
                new_item = item.split('x')[1]
                new_item = new_item.strip()
                new_equipped.append(new_item)
        return new_equipped

    @staticmethod
    def split_the_dot(model_name):
        model_name = model_name.split('.')[1]
        return model_name

    @staticmethod
    def extract_multi_model_unit_pts(line):
        pts = ''
        ends = line.find('pts') - 1
        while line[ends].isdigit():
            pts += line[ends]
            ends -= 1

        pts = pts[::-1]
        return pts

    def extract_models_from_units(self, line):
        unit = []
        models = []

        model_name, _ = line.split(': ')

        model_name = self.split_the_dot(model_name)

        if 'w/' in model_name:
            model_name = model_name.split('w/')[0]
        model_name = model_name.strip()
        # todo: add it to the relevant list

        if 'x' in model_name:
            amount, model_name = model_name.split('x')
            amount = amount.strip()
            amount = int(amount)
            model_name = model_name.strip()
            for i in range(amount):
                models.append(model_name)
                unit.append(models)
                # todo: add it to the relevant list

        return models

    def extract_models_equipment(self, line):

        _, equipped = line.split(': ')

        equipped = equipped.split(', ')

        equipped = self.split_the_newLine(equipped)

        equipped = self.split_the_x(equipped)
        return equipped
        # todo: add it to the relevant list

    def extract_units(self):
        line_index = 0
        next_line = 0

        for line in self.data:

            model = []

            # check if this is the last line
            if self.data.index(line) + 1 <= len(self.data) - 1:
                next_index = self.data.index(line) + 1
                next_line = self.data[next_index]

            # check if this is the army_roll line
            if '+' in line and line_index > 3 and '++' not in line:
                roll = self.extract_roll(line)
                model.append(roll)
                # todo: add "roll" to the relevant list
                # print(roll)

            # check if this is a single model unit line
            elif line[0] != '.' and line_index > 3 and '++' not in line and 'BattleScribe' not in line:
                unit_name = self.extract_one_model_unit_name(line)
                model.append(unit_name)
                # print(unit_name, end=" ")

                pts_cost = self.extract_unit_pts_cost(line)
                model.append(pts_cost)
                # print(pts_cost, end=" ")

                if ':' in line and next_line[0] != '.' and '[' in line:
                    equipped = self.extract_SingleModelUnit_equipment(line)
                    model.append(equipped)
                # print(equipped)
                # todo: add "name", "pts_cost" and "equipped" to the relevant list

            # check if this is a multi model unit
            if '[' in line and next_line[0] == '.' and line[0] != '.':  # unit name

                unit_name = self.extract_multi_model_unit_name(line)
                print(unit_name, end=' ')

                unit_pts = self.extract_multi_model_unit_pts(line)
                print(unit_pts)

                if ':' in line:  # finding general unit equipment
                    general_equipped = self.extract_multi_unit_general_equipment(line)
                    # todo: add it to the relevant list

            elif line[0] == '.':

                models = self.extract_models_from_units(line)
                models_equipment = self.extract_models_equipment(line)

            line_index += 1


class ParseFromHtml:

    def __init__(self, html_file):
        self.file = html_file

        with open(html_file, 'r') as file:
            self.data = BeautifulSoup(file, 'lxml')

        print(self.data)

    def extract_faction(self):
        pass

    def extract_detachment(self):
        pass

    def extract_pts(self):
        pass

    def extract_CP(self):
        pass

    def extract_game_type(self):
        pass

    def extract_army_subfaction(self):
        pass

    def extract_one_model_unit_name(self, line):
        pass

    def extract_SingleModelUnit_equipment(self, line):
        pass

    def extract_multi_model_unit_name(self, line):
        pass

    def extract_models_from_units(self, line):
        pass

    def extract_models_equipment(self, line):
        pass

    def extract_units(self):
        pass

    @staticmethod
    def extract_roll(line):
        pass

    @staticmethod
    def extract_unit_pts_cost(line):
        pass

    @staticmethod
    def extract_multi_unit_general_equipment(line):
        pass

    @staticmethod
    def split_the_newLine(equipped):
        pass

    @staticmethod
    def split_the_x(equipped):
        pass

    @staticmethod
    def split_the_dot(model_nam):
        pass

    @staticmethod
    def extract_multi_model_unit_pts(line):
        pass


if __name__ == '__main__':
    cajlito_army = PlainTxtParser(path_txt + army_cajlito)
    print()
    print(cajlito_army.army_file)
    print(cajlito_army.detachment)
    print(cajlito_army.faction)
    print(cajlito_army.pts)
    print(cajlito_army.CP)

    cajlito_army.extract_units()
    new_object = ParseFromHtml(html_BloodClaws)