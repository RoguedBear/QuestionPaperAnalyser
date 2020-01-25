import os
from json import load


def loaddict():
    """
    Purpose: Loads dictionary from json file
    :return: dictionary, title
    """
    path = os.getcwd() + '/Saved/'
    all_files = os.listdir(path)

    for i in range(0, len(all_files) + 1, 2):
        try:
            print(f"{all_files[i]:>50} 	 {all_files[i + 1]:<50}")
        except IndexError:
            try:
                print(f'{all_files[i]:^100}')
            except IndexError:
                pass

    # Taking the file name user wants to open
    # While for exception handling
    while True:
        try:
            file = input("Enter the name of the file you wish to open...\n")
            if file[-4:].lower() != 'json':
                file_path = path + file + '.json'
            else:
                file_path = path + file
                file = file.rstrip('.json')  # To make it Title-Ready
            with open(file_path, 'r') as read_data:
                read_dictionary = load(read_data)
                # print("text is:", read_dictionary)  # Debug
            # Because JSON maps 1, 1.0, '1' as the same thing in keys, so converting str to int keys
            parsed_dictionary = {int(a): read_dictionary[a] for a in read_dictionary.keys()}
            # print(parsed_dictionary)  # Debug

            return parsed_dictionary, file

        except FileNotFoundError:
            print("File not found. Maybe did a typo?\n")
            continue

if __name__ == '__main__':
    x = loaddict()
    print('And the dictionary:', x)