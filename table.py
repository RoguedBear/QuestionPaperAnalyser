# File to Table Reader
import os


try:
    from prettytable import PrettyTable
except ModuleNotFoundError:
    print("Pretty Table module is needed to display the tables.\n\tInstall it using  pip3 install PrettyTable")


def table(dictionary, title_of_table=''):
    """
    Prints ASCII table using PrettyTable Module
    :param dictionary: Dictionary
    :param title_of_table:  Title
    :return: None
    """
    pt = PrettyTable()
    pt.field_names = ["S.no", "Chapter Name", "Number Of Questions", "Marks", "Weightage"]
    pt.align['Chapter Name'] = 'l'
    for a in range(1, len(dictionary) + 1):
        pt.add_row(
            [
             f'{a}.', dictionary[a]['name'],
             dictionary[a]['questions'],
             dictionary[a]['total marks'],
             f'{dictionary[a]["weightage"]:5.2f}%'
             ]
        )
    print(pt.get_string(title=title_of_table.title()))


# Listing all files in the Saved Directory.
if __name__ == '__main__':
    from json import load
    path = os.getcwd() + '/Saved/'
    all_files = os.listdir(path)

    for i in range(0, len(all_files) + 1, 2):
        try:
            print(f"{all_files[i]:>50} 	 {all_files[i + 1]:<50}")
        except IndexError:
            print(f'{all_files[i]:^100}')

    # Taking the file name user wants to open
    # While for exception handling
    while True:
        try:
            file = input("Enter the name of the file you wish to open...\n")
            if file[-4:].lower() != 'json':  # txt':
                file_path = path + file + '.json'  # '.txt'
            else:
                file_path = path + file
            main_ = load(open(file_path))
            break
        except FileNotFoundError:
            print("File not found. Maybe did a typo?\n")
            continue

    Title = ''
    main = {int(i): main_[i] for i in main_}

    new = ''
    # Formatting Title [removing \n]
    for a in range(len(Title) - 2):
        new += Title[a]


    # TABLE
    table(main, title_of_table=new)
