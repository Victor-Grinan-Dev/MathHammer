import csv
from database import os_funcs as system


def open_read_csv(filename):
    filename = check_extension(filename)
    data = []
    if system.check_if_exist_path(filename):
        with open(filename, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)

            for line in csv_reader:
                data.append(line)
                print(line)
        return data
    return False


def create_line_from_list(list_of_items):
    line = ""
    for item in list_of_items:
        line += str(item) + ","
    return line


def check_extension(filename):
    if '.csv' not in filename:
        filename += '.csv'
    return filename


def create_csv(path_to_filename, headings, list_of_data):
    path_to_filename = check_extension(path_to_filename)
    if not system.check_if_exist_path_file(path_to_filename):
        with open(path_to_filename, 'w') as f:
            writer = csv.writer(f)

            writer.writerow(headings)

            for item in list_of_data:
                writer.writerow(item)
    return False


def add_line(path_to_file, headings, arguments):
    headings = check_extension(headings)

    if type(arguments) == list:
        arguments = create_line_from_list(arguments)

    if not system.check_if_exist_path_file(headings):
        create_csv(path_to_file, headings, arguments)

    with open(path_to_file, 'a') as file:
        file.write(arguments)
    return True


def remove_csv(path_to_filename):
    if system.check_if_exist_path(path_to_filename):
        system.delete_file(path_to_filename)


def remove_line_from_csv(path_to_filename, line_to_remove):
    new_data = []
    headings = path_to_filename[0]
    data = open_read_csv(path_to_filename)
    for line in data:
        if data != line_to_remove:
            new_data.append(line)
    create_csv(path_to_filename, headings, new_data)


def read_from_csv_as_dictionary(filename):
    with open(filename, 'r') as file:
        data = csv.DictReader(file)
        return data


def create_csv_from_dictionary(filename, fieldnames, data):
    with open(filename, "w") as new_file:
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)
        csv_writer.writeheader()

        for line in data:
            csv_writer.writerow(line)

    return True


def find_fieldnames_from_dict(dictionary):
    fieldnames = []

    for _, data in dictionary.items():
        for key in data.keys():
            fieldnames.append(key)

        break
    return fieldnames


def insert_fieldname(fieldnames, new_fieldname, position=0):
    """
    for list of fieldname strings, insert a new one.
    :param fieldnames:
    :param new_fieldname:
    :param position:
    :return:
    """
    fieldnames.insert(position, new_fieldname)


def append_to_csv_from_dictionary(filename, fieldnames, data):
    filename = check_extension(filename)

    if system.check_if_exist_path(filename):
        with open(filename, "a") as new_file:
            csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)

            for line in data:
                csv_writer.writerow(line)
    else:
        create_csv_from_dictionary(filename, fieldnames, data)

    return True


if __name__ == '__main__':
    import database.dictionary_type_old_db as test_db

    bullet_point = ['•']

    weapon_heading = ["name", "range", "type", "shots", "strength", "AP", "damage", "special rules"]

    model_heading = ["name", "roll", "Bs", "Ws", "T", "wounds", "save", "special_ability"]

    fieldnames_ = find_fieldnames_from_dict(test_db.armoury)

    insert_fieldname(fieldnames_, 'name')
    print(fieldnames_)
    for weapon, caracteristacs in test_db.armoury.items():

        print(weapon, end=" ")
        for fieldname_, data_ in caracteristacs.items():
            print(data_, end=" ")

        print("\n")
